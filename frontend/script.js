const boton = document.querySelector("#clickBoton");
const pregunta = document.querySelector('#pregunta');
const textArea = document.querySelector('#tArea');
const accesibilidad = document.querySelector('#botonAccesibilidad');
let bandera = false;
let cajon = '';

function accion() {
    cajon += '\nTu: ' + pregunta.value;
    textArea.innerHTML = cajon;

    fetch("http://localhost:8000/openai/", {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            mensaje: pregunta.value,
        }),
    }).then(respuesta => {
        return respuesta.json();
    }).then(res => {
        // console.log(res['mensaje']);
        cajon += '\nChatbot: ' + res['mensaje'];
        textArea.innerHTML = '';
        textArea.innerHTML = cajon;
        pregunta.value = '';
    });
};

function activarAccesibilidad() {
    const pregunta = document.querySelector('#pregunta');

    if (bandera === false) {
        accesibilidad.innerHTML = "Accesibilidad = ON";
        pregunta.placeholder = "Esperando entrada de voz..."
        boton.style.display = "none";
    } else {
        accesibilidad.innerHTML = "Accesibilidad = OFF";
        pregunta.placeholder = "Inserte el siguiente prompt"
        boton.style.display = "block";
    }

    bandera = !bandera;
    // const pregunta = document.querySelector('#pregunta');
    // pregunta.placeholder = "Esperando entrada de voz...";
    // boton.style.display = "none";
}

accesibilidad.addEventListener("click", activarAccesibilidad);
boton.addEventListener("click", accion);