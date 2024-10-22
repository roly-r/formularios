from flask import Flask, render_template, request, session, redirect, url_for

app = Flask(__name__)
app.secret_key = 'unaclavesecreta'

@app.route("/")
def index():
    return render_template('index.html')

# Página de inscripción
@app.route("/inscripcion")
def inscripcion():
    if 'inscripcion' not in session:
        session['inscripcion'] = []
    return render_template('inscripcion.html')

@app.route("/inscripcion_resultado", methods=['POST'])
def inscripcion_resultado():
    nombre = request.form['nombre']
    apellidos = request.form['apellidos']
    curso = request.form['curso']

    if 'inscripcion' not in session:
        session['inscripcion'] = []

    session['inscripcion'].append({'nombre': nombre, 'apellidos': apellidos, 'curso': curso})
    session.modified = True
    return redirect(url_for('inscripcion'))

@app.route("/mostrar_inscripcion")
def mostrar_inscripcion():
    inscripciones = session.get('inscripcion', [])
    return render_template('inscripcion_resultado.html', inscripciones=inscripciones)

# Página de registro de usuario
@app.route("/registro_usuario")
def registro_usuario():
    if 'usuarios' not in session:
        session['usuarios'] = []
    return render_template('registro_usuario.html')

@app.route("/registro_usuario_resultado", methods=['POST'])
def registro_usuario_resultado():
    nombre = request.form['nombre']
    apellidos = request.form['apellidos']
    correo = request.form['correo']

    if 'usuarios' not in session:
        session['usuarios'] = []

    session['usuarios'].append({'nombre': nombre, 'apellidos': apellidos, 'correo': correo})
    session.modified = True
    return redirect(url_for('mostrar_usuarios'))

@app.route("/mostrar_usuarios")
def mostrar_usuarios():
    usuarios = session.get('usuarios', [])
    return render_template('registro_usuario_resultado.html', usuarios=usuarios)

# Página de registro de producto
@app.route("/registro_producto")
def registro_producto():
    if 'productos' not in session:
        session['productos'] = []
    return render_template('registro_producto.html')

@app.route("/registro_producto_resultado", methods=['POST'])
def registro_producto_resultado():
    producto = request.form['producto']
    categoria = request.form['categoria']
    existencia = request.form['existencia']
    precio = request.form['precio']

    if 'productos' not in session:
        session['productos'] = []

    session['productos'].append({
        'producto': producto, 'categoria': categoria, 
        'existencia': existencia, 'precio': precio
    })
    session.modified = True
    return redirect(url_for('mostrar_productos'))

@app.route("/mostrar_productos")
def mostrar_productos():
    productos = session.get('productos', [])
    return render_template('registro_producto_resultado.html', productos=productos)

# Página de registro de libro
@app.route("/registro_libro")
def registro_libro():
    if 'libros' not in session:
        session['libros'] = []
    return render_template('registro_libro.html')

@app.route("/registro_libro_resultado", methods=['POST'])
def registro_libro_resultado():
    titulo = request.form['titulo']
    autor = request.form['autor']
    resumen = request.form['resumen']
    medio = request.form['medio']

    if 'libros' not in session:
        session['libros'] = []

    session['libros'].append({
        'titulo': titulo, 'autor': autor, 
        'resumen': resumen, 'medio': medio
    })
    session.modified = True
    return redirect(url_for('mostrar_libros'))

@app.route("/mostrar_libros")
def mostrar_libros():
    libros = session.get('libros', [])
    return render_template('registro_libro_resultado.html', libros=libros)

# Ruta para vaciar todos los datos
@app.route("/vaciar")
def vaciar():
    session.clear()  
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
