const pais = document.querySelector('#pais');
const empresa = document.querySelector('#empresa');
const capital = document.querySelector('#capital');
const formulario = document.querySelector('#formulario');

formulario.addEventListener('submit', async (e) => {
    e.preventDefault()
    if (empresa.value != '' && empresa.value != '' && capital.value) {


        let peticion = await axios.post('http://localhost:8000/api/v1/empresa', {
            nombre: empresa.value,
            pais: pais.value,
            capital: capital.value
        });

        const datos = peticion.data
        if (!datos['error']) {
            Swal.fire({
                icon: 'success',
                title: datos['mensaje'],
                showConfirmButton: false,
                timer: 1500
            })
        } else {
            Swal.fire({
                icon: 'error',
                title: 'Error al registrar la empresa',
                showConfirmButton: false,
                timer: 1500
            })
        }


    }
})