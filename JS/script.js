function login(form) {
    const usuarios = [
        {
            "email": 'superadmin@gmail.com',
            "contraseña": 'superadmin',
            "usuario": 'superadmin',
        }, {
            "email": 'admin@gmail.com',
            "contraseña": 'admin',
            "usuario": 'admin',
        }, {
            "email": 'usuario@gmail.com',
            "contraseña": 'usuario',
            "usuario": 'usuario',
        }
    ]
    var email = form.email.value;
    var pass = form.password.value;

    for (var i = 0; i < usuarios.length; i++) {
        if((email =! '') && (pass =! '')){
            if (usuarios[i].email == email) {
                console.log('entre')
            } 
        }
    }
}