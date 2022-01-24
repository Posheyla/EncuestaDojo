from flask import Flask,render_template, redirect,request,session

app = Flask(__name__)
app.secret_key="Clave secreta"

listausuarios=[]

@app.route('/')
def inicioPagina():
    if 'contador' not in session:
        return render_template('index.html')
    return render_template('index.html')

@app.route('/registro', methods=['POST'])
def registrar():
    usuario={
        "nombre":request.form['nombre'],
        "location":request.form['location'],
        "language":request.form['language'],
        "comment":request.form['comment'],
    }
    if usuario['nombre']=='':
        return redirect('/')
    session['contador']=1
    listausuarios.append(usuario)
    return redirect('/datos')

@app.route('/datos')
def mostrar():
    if 'contador' in session:
        return render_template('datos.html',usuarios=listausuarios)
    else:
        return redirect('/')

@app.route('/logout')
def salir():
    session.clear()
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)
