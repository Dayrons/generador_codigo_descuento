const valor = document.querySelector('#valor');
const empresa = document.querySelector('#empresa');
const formulario = document.querySelector('#formulario');

formulario.addEventListener('submit',async (e)=>{
    e.preventDefault()
    if(Number(valor.value) > 0 && empresa.value != ''){


        let peticion =  await axios.post('http://localhost:8000/api/v1/cupones/create',{
        valor: Number(valor.value),
        empresa: empresa.value
        });

        Swal.fire({
            icon: 'success',
            title: 'Codigo de descuento generado',
            showConfirmButton: false,
            timer: 1500
          })
    }   
})