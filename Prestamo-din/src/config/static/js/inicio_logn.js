function ingresar() {
    const user = document.getElementById("usuario").value;
    const password = document.getElementById("contraseña").value;
  
    axios
      .post(
        '/fronted/verificarlogin',
        {
          usuario: user,
          contraseña: password
        },
        {
          headers: {
            'Content-Type': 'multipart/form-data'
          }
        }
      )
      .then((res) => {
        console.log(res.data);
        // Check if the login verification was successful
        if (res.data === "Correcto") {
          window.location.href = "/fronted/indexindex";
        } else {
          console.log("Invalid credentials");
          // Handle invalid login, such as displaying an error message
        }
      })
      .catch((error) => {
        console.error(error);
        alert(error);
      });
  
    var form = document.getElementById("formulario");
    form.reset();

  }
