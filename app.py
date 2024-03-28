from flask import Flask, render_template, request, send_from_directory, jsonify
import os
from convert import myconvertfunc, getresponse

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



# @app.route('/chat', methods=['POST'])
# def chat():
#     user_message = request.form['message']
#     # Process user_message and generate bot_response
#     bot_response = process_user_message(user_message)
#     return bot_response

@app.route('/send_message', methods=['POST'])
def send_message():
    message = request.form['message']
    # Process the message (you can implement your chatbot logic here)
    # For demonstration purposes, we'll simply echo the message back
    return jsonify({'message': ("Bot: " + process_user_message(message))})

def process_user_message(user_message):
    # Add your chatbot logic here
    # For demonstration purposes, echo the user's message
    filename = 'pdfFile.pdf'
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    return (getresponse(user_message, file_path))['answer']
    # return "hello i am chatbot"

if __name__ == '__main__':
    app.run(debug=True)
