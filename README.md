# Subir-Archivos-Al-Servidor-Flask
Métodos para subir archivos con Flask.

Hola amigos de Internet, mi nombre es Luis, y les doy la bienvenida a Mi Diario Python.
En el articulo de hoy nos dedicaremos a conocer los métodos para subir archivos con Flask.
Cuando subimos una foto a Facebook, Facebook la sube a su servidor para poder mostrarla en nuestro muro. Mega, Mediafire, Github, todos ello toman nuestros archivos y los almacenan en su servidor para que luego las otras personas puedan acceder a este, y puedan descargarlo. Creo que se entendió el punto ¿No?.
En muchas ocasiones tendremos que guardar y subir archivos a nuestro servidor. Y hoy te enseñare lo fácil que es hacerlo con Flask.
Prepárate, ponte cómodo, taza de café en mano, y comencemos.

## Formulario de Subida.
Comencemos por el inicio. Lo primero que haremos sera crear el formulario desde donde el usuario seleccionara el archivo a subir.
Crearemos una plantilla, un cuerpo HTML con don entradas: selección del archivo, y enviar.
Recordemos que todas las plantillas que seran renderizadas con Flask deberan estar en un directorio llamado templates.
Aprende más sobre el renderizado de plantillas con Flask: http://www.pythondiario.com/2018/10/renderizar-plantillas-en-flask.html
Así que dentro del directorio templates creare mi archivo HTML:

```html
<form action="/upload" method="POST" enctype="multipart/form-data">
 <input type="file" name="archivo">
 <input type="submit">
</form>
```

Como pueden observar, es un formulario muy sencillo. Cuando presionemos enviar, la información se enviara a /upload con método POST y tipo de encriptación multipart/form-data. Luego tenemos el input de tipo file con nombre archivo (este nombre archivo lo utilizaremos más tarde).
Muy bien, ya tenemos nuestra plantilla. Es muy simple. Es hora de escribir el script.

## Escribiendo el Script
Muy bien es hora de escribir el Script. Mostrare el código completo y luego lo explicare. Y no te asustes, podrá verse complicado, pero es muy simple:
```python 
# Importamos todo lo necesario
import os
from flask import Flask, render_template, request
from werkzeug import secure_filename

# instancia del objeto Flask
app = Flask(__name__)
# Carpeta de subida
app.config['UPLOAD_FOLDER'] = './Archivos PDF'

@app.route("/")
def upload_file():
 # renderiamos la plantilla "formulario.html"
 return render_template('formulario.html')

@app.route("/upload", methods=['POST'])
def uploader():
 if request.method == 'POST':
  # obtenemos el archivo del input "archivo"
  f = request.files['archivo']
  filename = secure_filename(f.filename)
  # Guardamos el archivo en el directorio "Archivos PDF"
  f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
  # Retornamos una respuesta satisfactoria
  return "<h1>Archivo subido exitosamente</h1>"

if __name__ == '__main__':
 # Iniciamos la aplicación
 app.run(debug=True)
 
 ```
 
Comenzamos importando lo necesario. os para subir los archivos en la ruta que deseemos. render_template, Flask, request, ya sabemos para que sirven cada uno de ellos. Y secure_filename
Creamos el objeto Flask. Y hacemos una configuración. En este caso app.config[‘UPLOAD_FOLDER’], aquí especificaremos la carpeta en donde se guardaran los archivos que el usuario elija subir. En mi caso, subiré archivos PDF, así que la carpeta se llama Archivos PDF, sí, lo se, soy muy original.

Luego renderizamos la plantilla formulario.html.
Ahora definimos el route de la ruta /uploader y especificamos que en esta ruta se recibirá la información, enviada a través de método POST. Como recordaras, a esta ruta es donde el formulario envía la información.
Luego la aplicación accede al archivo desde el diccionario filesen el objeto de solicitud request.
Obtenemos el nombre del archivo subido por el usuario. Y luego utilizando el método save.
Por ultimo retornamos una respuesta. En este caso, un mensaje diciendo que el archivo se ha subido exitosamente.
