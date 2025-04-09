from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'file' not in request.files:
            return "❌ No file part in the request."
        file = request.files['file']
        if file.filename == '':
            return "⚠️ No selected file."
        return f"✅ File <strong>{file.filename}</strong> uploaded successfully!"
    return '''
        <form method="POST" enctype="multipart/form-data">
            <input type="file" name="file">
            <input type="submit" value="Upload">
        </form>
    '''

if __name__ == '__main__':
    app.run(debug=True)