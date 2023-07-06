function validarNombre(inputn,msj) {
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


function validarApellido(inputn,msj) {

    var apellido = document.querySelector(inputn);
    const mensaje1 = document.querySelector(msj);

    if (apellido.value.length >= 3 && apellido.value.length <= 20) {
        apellido.classList.remove("error");
        mensaje1.classList.add("errorP")
    } else {
        apellido.classList.add("error");
        mensaje1.classList.remove("errorP")
    }           
}



function validarEdad(inputn,msj) {

    var edad = document.querySelector(inputn).value.trim();
    const mensaje3 = document.querySelector(msj);

    if (edad >= 18 && edad <= 30) {
        document.querySelector(inputn).classList.remove("error");
        mensaje3.classList.add("errorP")
    } else {
        document.querySelector(inputn).classList.add("error");
        mensaje3.classList.remove("errorP")
    }
}



function validarContraseña(){
    var contra1 = document.querySelector("#contraseña");
    var contra2 = document.querySelector("#confirmar-contraseña");
    const mensaje4 = document.querySelector("#p-contraseña");
    const mensaje5 = document.querySelector("#p-confirmar-contraseña");

    if (contra1.value.length >= 4 && contra1.value.length <= 10){
        contra1.classList.remove("error");
        mensaje4.classList.add("errorP")
    }else{
        contra1.classList.add("error");
        mensaje4.classList.remove("errorP")
    }

    if (contra1.value != contra2.value){
        contra2.classList.add("error");
        mensaje5.classList.remove("errorP")
    }else{
        contra2.classList.remove("error");
        mensaje5.classList.add("errorP")
    }
}

function validarRut(){
        var rut = document.querySelector("#rut");
        const mensaje2 = document.querySelector("#p-rut")
        rut1 = rut.value.replaceAll(".","").replaceAll("-",""); // eliminar puntos
        var dv = rut1.slice(-1); // extraer dígito verificador
        var rutSinDV = rut1.slice(0,-1); // extraer número del RUT sin dígito verificador
        var suma = 0;
        var multiplo = 2;

        for(var i = rutSinDV.length - 1; i >= 0; i--) {
            suma += rutSinDV.charAt(i) * multiplo;
            multiplo = (multiplo + 1) % 8 || 2;
        }
        var dvCalculado = (11 - (suma % 11)).toString();
        if(dvCalculado === '10') dvCalculado = 'K';
        if(dvCalculado === '11') dvCalculado = '0';
        var esValido = dv === dvCalculado;

    if(esValido){
        rut.classList.remove("error");
        mensaje2.classList.add("errorP")
    }else{
        rut.classList.add("error");
        mensaje2.classList.remove("errorP")
    }
}


function validarFhone(inputn,msj) {


    const phone = document.querySelector(inputn);
    const firstNumber = phone.value.at(0);
    const length = phone.value.length
    const mensaje7 = document.querySelector(msj);

    if (firstNumber != 9 || length != 9) {
        phone.classList.add("error");
        mensaje7.classList.remove("errorP")
    }else{
        phone.classList.remove("error");
        mensaje7.classList.add("errorP")
    }
}


function validarCorreo(){
    const correo = document.querySelector("#correo");
    const prueba = correo.value.indexOf("@");
    const punto = correo.value.indexOf(".");
    const mensaje6 = document.querySelector("#p-correo");

     if (prueba === -1 || punto === -1 ) {
        correo.classList.add("error");
        mensaje6.classList.remove("errorP")
     }else{
        correo.classList.remove("error");
        mensaje6.classList.add("errorP")
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
    console.log(inputs);
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
