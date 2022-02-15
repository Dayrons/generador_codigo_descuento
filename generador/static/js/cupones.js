const formulario = document.querySelector('#formulario')
const codigo = document.querySelector('#codigo')
const listaCodigos = document.querySelector('#lista-cupones')


window.onload = async () => {

  await obtenerCupones()

}




formulario.addEventListener('submit', async (e) => {
  e.preventDefault()
  if (codigo.value != '') {


    axios.post('http://localhost:8000/api/v1/cupones/canjear', {
      'codigo': codigo.value
    })
      .then(async (response) => {
   
        const datos = response.data

        Swal.fire({
          icon: 'success',
          title: `Cupon cajeado tienes un %${datos.valor} de descuento en tu contratacion`,
          showConfirmButton: false,
          timer: 2000
        })

        await obtenerCupones()

      })
      .catch(async (error)=> {

        await obtenerCupones()

        const mensajeError = error.response.data['mensaje']

          Swal.fire({
            icon: 'error',
            title: mensajeError,
            showConfirmButton: false,
            timer: 1500
          })
      })

      Swal.fire({
        icon: 'error',
        title: 'Error al canjear el cupon',
        showConfirmButton: false,
        timer: 1500
      })

    return null
  }

  Swal.fire({
    icon: 'error',
    title: 'Ingrese  un codigo',
    showConfirmButton: false,
    timer: 1500
  })



})



async function obtenerCupones() {
  listaCodigos.innerHTML = ` <i class='bx bx-loader bx-spin' style="font-size: 40px;"></i>`
  const respuesta = await axios.get('http://localhost:8000/api/v1/cupones')

  const cupones = respuesta.data


  let cuponesHTML = ''
  cupones.forEach(cupon => {
    cuponesHTML +=
      `
            <div class="col-4 ">
                <div class="card">
                <div class="card-header" style="background: ${cupon.usado ? '#ff4757' : '#1e90ff'}">
                  CUPON
                </div>
                <div class="card-body">
                  <h5 class="card-title">${cupon.codigo}</h5>
                </div>
              </div>
            </div>
         
            `
  });
  listaCodigos.innerHTML = cuponesHTML


}