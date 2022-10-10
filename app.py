from flask import Flask, render_template, request, redirect, url_for
import controlador
import hashlib

app=Flask(__name__)

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login',methods=['GET', 'POST'])
def login():
    if request.method =='POST':
        usu = request.form['email']
        passw = request.form['password']
        
        respuesta = controlador.validar_usuario(usu, passw)
        print(respuesta[0])
        if len(respuesta) == 0:
            return "<center> <h1>El usuario no existe <h1>"       
        else:
            rol = respuesta[0][2]
            if rol == "ADMINISTRADOR":
                return redirect(url_for('Adm', id = respuesta[0][5], nombre = respuesta[0][1]))
            if rol == "Usuario":
                return redirect(url_for('Usuario'))
            if rol == "SuperAdm":
                return redirect(url_for('Superadm'))
            else:
                return ("<center> <h1> Tu rol no esta validado correctamente, habla con un superior <h1>")
        
    else:
        return render_template("index.html")


@app.route("/Adm/<id>/<nombre>",methods=['GET', 'POST'])
def Adm(id,nombre):
    return render_template("Adm.html", data={"id": id,"nombre":nombre})

@app.route("/Usuario",methods=["get"])
def Usuario():
    return render_template("usuario4.html")

@app.route('/Superadm',methods=['GET', 'POST'])
def Superadm():
    return render_template("Super_Adm.html")


@app.route("/Superadm2",methods=["get"])
def Superadm2():
    return render_template("Super_Adm2B.html")


    
app.run(debug=True)