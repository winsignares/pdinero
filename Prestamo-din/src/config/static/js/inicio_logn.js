function ingresar(){
      
    const user = document.getElementById("usuario").value;
    const password = document.getElementById("contraseña").value; 
    
    axios.post('/fronted/verificarlogin', {
        usuario: user,
        contraseña: password
    
    }, {
        headers: {
        'Content-Type': 'multipart/form-data'

        }
    }
    ).then((res) => {
        console.log(res.data)
        window.location.href="/fronted/indexindex"
        
    })
    .catch((error) => {
        console.error(error)
        alert(error)
        
    })

var form = document.getElementById("formulario"); 
// Limpiar los campos del formulario
form.reset();
}