const formUser = document.getElementById('formUser');
const inputName = document.getElementById('name');
const inputLastname = document.getElementById('lastname');
const inputUser = document.getElementById('user');
const inputEmail = document.getElementById('email');
const inputPassword = document.getElementById('password');
const inputRepeatPass = document.getElementById('repeatpassword');
const btnUpdate = document.querySelector('.btnUpdate');


btnUpdate.disabled = true;

window.onload = function validaciones() {
    
    // formUser.addEventListener('submit', function (e) {
    //     let name = String(inputName.value).trim();
    //     let lastname = String(inputLastname.value).trim();
    //     let user = String(inputUser.value).trim();
    //     let email = String(inputEmail.value).trim();
    //     if (name.length === 0 ) {
    //         alert('no  puede ir vacio el nombre del usuario');
    //         e.preventDefault();
    //     }
    //     if (lastname.length === 0) {
    //         alert('no  puede ir vacio el apellido del usuario');
    //         e.preventDefault();
    //     }
    //     if (user.length === 0) {
    //         alert('no  puede ir vacio el usuario');
    //         e.preventDefault();
    //     }

    // });

    //esto es para el nombre y apellido
    const validateEmptyField = (e) => {
        const field = e.target;
        const fieldValue = e.target.value;

        if (fieldValue.trim().length === 0) {
            
            field.classList.add('falla');
            field.nextElementSibling.classList.add('error');
            field.nextElementSibling.innerText = `${field.name} requerido`;
            btnEnviar.disabled = true;
        }else if (/^\d+$/.test(fieldValue) || /\d/.test(fieldValue)) {
            field.classList.add('falla');
            field.nextElementSibling.classList.add('error');
            field.nextElementSibling.innerText = `El ${field.name} no debe contener números`;
            btnEnviar.disabled = true;
        }else {
            field.classList.remove('falla')
            field.nextElementSibling.classList.remove('error');
            field.nextElementSibling.innerText = '';
            btnEnviar.disabled = false;
        }
    }

    //esto es para el usuario
    const validateEmptyField2 = (e) => {
        const field = e.target;
        const fieldValue = e.target.value;

        if (fieldValue.trim().length === 0) {
            
            field.classList.add('falla');
            field.nextElementSibling.classList.add('error');
            field.nextElementSibling.innerText = `${field.name} requerido`;
            btnEnviar.disabled = true;
        }else {
            field.classList.remove('falla')
            field.nextElementSibling.classList.remove('error');
            field.nextElementSibling.innerText = '';
            btnEnviar.disabled = false;
        }
    }

     //validacion para el correo
    const validateEmailFormat = (e) => {
        const field = e.target;
        const fieldValue = field.value.trim();
        const regex = new RegExp(/^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/)
        if (fieldValue.length > 0 && !regex.test(fieldValue)) {

            field.classList.add('falla')
            field.nextElementSibling.classList.add('error');
            field.nextElementSibling.innerText = `please enter a valid email`;
            btnUpdate.disabled = true;
        }else {
            field.classList.remove('falla');
            field.nextElementSibling.classList.remove('error');
            field.nextElementSibling.innerText = '';
            btnUpdate.disabled = false;
        }
    }
    
    inputName.addEventListener('blur', validateEmptyField);
    inputLastname.addEventListener('blur', validateEmptyField);
    inputUser.addEventListener('blur', validateEmptyField2);
    inputEmail.addEventListener('blur', validateEmailFormat);



}