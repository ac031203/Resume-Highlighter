from flask import Flask, render_template, request, send_from_directory
import os
from convert import myconvertfunc

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
OUTPUT_FOLDER = 'output'

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['OUTPUT_FOLDER'] = OUTPUT_FOLDER

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return 'No file part'
    
    file = request.files['file']
    query = request.form['query']

    if file.filename == '':
        return 'No selected file'

    if file:
        filename = 'pdfFile.pdf'
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)
        
        output_pdf_path = os.path.join(app.config['OUTPUT_FOLDER'], 'outputpdf.pdf')

        # Process the PDF
        myconvertfunc(file_path, query, output_pdf_path)

        # Return the processed PDF
        return send_from_directory(app.config['OUTPUT_FOLDER'], 'outputpdf.pdf', as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
