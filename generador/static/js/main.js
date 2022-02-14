const formulario = document.querySelector('#formulario')





formulario.addEventListener('onsubmit',(e)=>{
    e.preventDefault()
    
    console.log(e.target.childNodes)

})