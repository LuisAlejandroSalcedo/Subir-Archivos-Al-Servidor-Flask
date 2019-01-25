import os
from flask import Flask, render_template, request
from werkzeug import secure_filename

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = "./Archivos PDF"

@app.route("/")
def upload_file():
	return render_template('formulario.html')

@app.route("/uploader", methods=['POST'])
def uploader():
	if request.method == "POST":
		f = request.files['archivo']
		filename = secure_filename(f.filename)
		f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
		return "Archivo subido exitosamente"

if __name__ == '__main__':
	app.run(debug=True)

