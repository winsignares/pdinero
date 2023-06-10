function Guardarusuario() {
    
    const user = document.getElementById("usuario").value;
    const password = document.getElementById("contraseña").value; 
    
    axios.post('/fronted/savelogins', {
        usuario: user,
        contraseña: password
    
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

