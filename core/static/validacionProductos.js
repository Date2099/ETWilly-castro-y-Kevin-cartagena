function validarProducto(inputn,msj) {
    var nombre = document.querySelector(inputn);
    const mensaje = document.querySelector(msj);
    var min = nombre.value.length >= 3
    var max = nombre.value.length <= 20

    if (min && max) {
        nombre.classList.remove("error");
        mensaje.classList.add("errorP")
    } else {
        nombre.classList.add("error");
        mensaje.classList.remove("errorP")
    }
}


function validarPrecio(inputn,msj) {
    console.log(inputn)
    var precio = document.querySelector(inputn).value.trim();
    const mensaje3 = document.querySelector(msj);

    if (precio >= 5 && precio <= 10) {
        document.querySelector(inputn).classList.remove("error");
        mensaje3.classList.add("errorP")
    } else {
        document.querySelector(inputn).classList.add("error");
        mensaje3.classList.remove("errorP")
    }
}


function validarDescripcion(inputn,msj) {
    var descripcion = document.querySelector(inputn);
    const mensaje2 = document.querySelector(msj);
    var min = descripcion.value.length >= 5
    var max = descripcion.value.length <= 10

    if (min && max) {
        descripcion.classList.remove("error");
        mensaje2.classList.add("errorP")
    } else {
        descripcion.classList.add("error");
        mensaje2.classList.remove("errorP")
    }
}


function validarStock(inputn,msj) {

    var stock = document.querySelector(inputn).value.trim();
    const mensaje3 = document.querySelector(msj);

    if (stock >= 5 && stock <= 10) {
        document.querySelector(inputn).classList.remove("error");
        mensaje3.classList.add("errorP")
    } else {
        document.querySelector(inputn).classList.add("error");
        mensaje3.classList.remove("errorP")
    }
}


function validar(editar = false){
    let valor = '#agregar'
    let msj = "#msj"

    if (editar){
        valor = '#editar'
        msj = "#msjE"
    }

    const form = document.querySelector(valor);
    const inputs = form.querySelectorAll('input');
    console.log(inputs[4].value.length);
    for (var i of inputs){
        if (i.classList.contains("error") || i.value.length === 0){
            document.querySelector("#" + i.id).classList.add("error")
            document.querySelector("#p-" + i.id).classList.remove("errorP")
            document.querySelector(msj).innerHTML = "Revise el campo " + i.name.toUpperCase();
            return false;
        }
    }
    return true;
}



function validarImagen(inputn,msj){
    const imagen = document.querySelector(inputn);
    const mensaje = document.querySelector(msj)

    if (imagen.value){
        imagen.classList.remove("error");
        mensaje.classList.add("errorP")
    }else{
        imagen.classList.add("error");
        mensaje.classList.remove("errorP")
    }


}



