function Guardarusuario() {
    
    const user = document.getElementById("usuario").value;
    const password = document.getElementById("contraseña").value; 
    const password2 = document.getElementById("confirmar_contraseña").value; 
    
    console.log(user,password,password2)
    axios.post('/fronted/saveregistro', {
        usuario1: user,
        contrasena1: password,
        confirmar1 : password2
    
    }, {
        headers: {
        'Content-Type': 'multipart/form-data'

        }
    }
    ).then((res) => {
        console.log(res.data)
        alert(res.data)
    })
    .catch((error) => {
        
        console.error(error)
        alert(error)
    })

    var form = document.getElementById("formulario");
        
// Limpiar los campos del formulario
form.reset();
}

