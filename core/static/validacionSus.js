function validarSus(){
    let switchCheck = document.querySelector("#suscripcion").checked;

    if (switchCheck){
        document.querySelector("#msj").innerHTML = "Suscripcion activada" 
    }else{
        document.querySelector("#msj").innerHTML = "Suscripcion desactivada " 
    }
}