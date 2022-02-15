const formulario = document.querySelector('#formulario')
const codigo = document.querySelector('#codigo')







formulario.addEventListener('submit', async (e) => {
  e.preventDefault()
  if (codigo.value != '') {




    axios.post('http://localhost:8000/api/v1/cupones/canjear', {
      codigo: codigo.value,
    })
      .then(function (response) {
  
        console.log(response);
      })
      .catch(function (error) {
       
      

        const mensajeError = error.response.data['mensaje']
        Swal.fire({

          icon: 'error',
          title:mensajeError ,
          showConfirmButton: false,
          timer: 1500
        })
      })



    Swal.fire({
      position: 'bottom-end',
      icon: 'success',
      title: 'Codigo de descuento generado',
      showConfirmButton: false,
      timer: 1500
    })



  }

  Swal.fire({

    icon: 'error',
    title: 'Ingrese  un codigo',
    showConfirmButton: false,
    timer: 1500
  })



})