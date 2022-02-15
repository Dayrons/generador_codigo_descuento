const valor = document.querySelector('#valor');
const empresa = document.querySelector('#empresa');

formulario.addEventListener('submit',async (e)=>{
    e.preventDefault()
    if(Number(valor.value) > 0 && empresa.value != ''){

        console.log(valor,empresa)
        let peticion =  await axios.post('http://localhost:8000/api/v1/cupones/create', {
        valor: Number(valor.value),
        empresa: empresa.value
        });

        console.log(peticion.data)

        Swal.fire({
            position: 'bottom-end',
            icon: 'success',
            title: 'Codigo de descuento generado',
            showConfirmButton: false,
            timer: 1500
          })
    }   
})