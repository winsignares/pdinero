function guardar() {
    const monto1 = document.getElementById('monto').value;
    const tiempo1 = document.getElementById('tiempo').value;
    const interes1 = document.getElementById('interes').value;
    console.log(monto1, interes1, tiempo1);

    axios.post('/fronted/guardarmonton', {
        monto: monto1,
        interes: interes1,
        tiempo: tiempo1

    }, {
        headers: {
            'Content-Type': 'multipart/form-data'

        }
    }
    ).then((res) => {
        console.log(res.data)
    })
        .catch((error) => {
            console.error(error)
        })
}

function calcularCuota() {
    var monto = document.getElementById("monto").value;
    var interes = document.getElementById("interes").value;
    var tiempo = document.getElementById("tiempo").value;

    var llenarTabla = document.querySelector('#lista-tabla tbody');

    while (llenarTabla.firstChild) {
        llenarTabla.removeChild(llenarTabla.firstChild);
    }

    let fechas = [];
    let fechaActual = Date.now();
    let mes_actual = moment(fechaActual);
    mes_actual.add(1, 'month');

    let pagoInteres = 0, pagoCapital = 0, cuota = 0;

    cuota = monto * (Math.pow(1 + interes / 100, tiempo) * interes / 100) / (Math.pow(1 + interes / 100, tiempo) - 1);

    for (let i = 1; i <= tiempo; i++) {
        pagoInteres = parseFloat(monto * (interes / 100));
        pagoCapital = cuota - pagoInteres;
        monto = parseFloat(monto - pagoCapital);

        // Formato fechas
        fechas[i] = mes_actual.format('DD-MM-YYYY');
        mes_actual.add(1, 'month');

        const row = document.createElement('tr');
        row.innerHTML = `
            <td class="lista">${fechas[i]}</td>
            <td class="lista">${cuota.toFixed(2)}</td>
            <td class="lista">${pagoCapital.toFixed(2)}</td>
            <td class="lista">${pagoInteres.toFixed(2)}</td>
            <td class="lista">${monto.toFixed(2)}</td>
        `;
        llenarTabla.appendChild(row);
    }
}

calcularCuota();


function generarResultado() {
    const monto = document.getElementById('monto').value;
    const interes = document.getElementById('interes').value;
    const tiempo = document.getElementById('tiempo').value;

    // Realizar el cálculo y obtener los valores necesarios para el resultado

    const resultado = `Monto: ${monto}\nInterés: ${interes}\nTiempo: ${tiempo}`;

    // Mostrar el resultado en una ventana emergente con SweetAlert
    Swal.fire({
        title: 'Cálculos del préstamo',
        html: resultado,
        icon: 'info',
        confirmButtonText: 'Cerrar'
    });
}


var modal = document.querySelector('.modal1');
var closeBtn = document.querySelector('.close1');

// Añade un evento click a cualquier parte del modal para cerrarlo también
modal.addEventListener('click', function (event) {
  if (event.target === modal) {
    modal.style.display = 'none';
  }
});

//Función para abrir el modal CASTIGO 
function openModal(id) {
  const ontide = document.getElementById('id-e')
  ontide.value = id
  modal.style.display = 'block';
}


