function validarCodigo() {
    console.log("compraLength")
    const compra = document.querySelector('#compra');
    const mensaje = document.querySelector('#p-compra');
    const compraLength = compra.value.length

    if (compraLength >= 1 ) {
        compra.classList.remove("error");
        mensaje.style.display = "none"
    } else {
        compra.classList.add("error");
        mensaje.style.display = "block"
    }
}






function validar(){
    const codigo = document.querySelector("#compra");
    const mensaje = document.querySelector("#p-compra");
    const msj = document.querySelector("#msje")

    if (codigo.value === "" || codigo.classList.contains("error")){
        codigo.classList.add("error");
        mensaje.style.display = "block"
    }else{
        msj.innerHTML = 'Su producto con el codigo ' + codigo.value + ' esta en camino'
    }

}