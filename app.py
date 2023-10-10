from flask import Flask, render_template

app = Flask(__name__)

# Configuración para servir archivos estáticos desde la carpeta 'static'
app.config['STATIC_FOLDER'] = 'static'

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()