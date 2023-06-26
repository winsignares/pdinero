axios
.post(
  'historial',
  {
    id: ontide.value,
    nombre: name.value,
    apellido: Apellidos.value,
    monto: monto.value,
    interes: interes.value,
    tiempo: tiempo.value


  },
  {
    headers: {
      'Content-Type': 'multipart/form-data'
    }
  }
)
.then((res) => {
  console.log(res.data)
  Swal.fire({
    position: 'top-center',
    icon: 'success',
    title: '¡Datos guardados Exitosamente!',
    showConfirmButton: false,
    timer: 2000,
    
  })
  document.getElementById("nombre").value = "";
  document.getElementById("Apellido").value = "";
  document.getElementById("monto").value = "";
  document.getElementById("interes").value = "";
  document.getElementById("tiempo").value = "";
  mostrar()

})
.catch((error) => {
  console.error(error)
  
})
