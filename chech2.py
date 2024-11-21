from flask import Flask, render_template, request, redirect, url_for
import os
import subprocess

app = Flask(__name__)

# Directory to save uploaded files
UPLOAD_FOLDER = os.path.join('static', 'uploads')
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    # Render the HTML form
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    # Handle file upload
    if 'file' not in request.files:
        return "No file part in the request.", 400

    file = request.files['file']
    if file.filename == '':
        return "No selected file.", 400

    # Save the uploaded file
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(filepath)

    # Run app2.py after the file is uploaded
    try:
        subprocess.run(['python3', 'app2.py'], check=True)
    except subprocess.CalledProcessError as e:
        return f"Error running app2.py: {e}", 500

    return f"File uploaded successfully to {filepath}. app2.py executed!"

if __name__ == '__main__':
    app.run(debug=True)
