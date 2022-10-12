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
                return redirect(url_for('Adm', id = respuesta[0][5], nombre = respuesta[0][1], rol = respuesta[0][2]))
            if rol == "Usuario":
                return redirect(url_for('Usuario'))
            if rol == "SuperAdm":
                return redirect(url_for('Superadm', id = respuesta[0][5], nombre = respuesta[0][1], rol = respuesta[0][2]))
            else:
                return ("<center> <h1> Tu rol no esta validado correctamente, habla con un superior <h1>")
        
    else:
        return render_template("index.html")


@app.route("/Adm/<id>/<nombre>/<rol>",methods=['GET', 'POST'])
def Adm(id,nombre, rol):
    return render_template("Adm.html", data={"id": id,"nombre":nombre, "rol": rol})

@app.route("/Usuario",methods=["get"])
def Usuario():
    return render_template("usuario4.html")

@app.route('/Superadm/<id>/<nombre>/<rol>',methods=['GET', 'POST'])
def Superadm(id,nombre, rol):
    return render_template("Super_Adm.html",data={"id": id,"nombre":nombre, "rol": rol})


@app.route("/Superadm2",methods=["get"])
def Superadm2():
    return render_template("Super_Adm2B.html")


    
app.run(debug=True)