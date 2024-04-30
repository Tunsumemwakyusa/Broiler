console.log('Hello from this side')

function validationform(event){
    const form = event.target;
    const inputs = form.querySelectorAll('input');
    let isValid = true;

    inputs.forEach(inputs => {
        if (!inputs.checkValidity()){
            isValid = false;
            inputs.classList.add('invalid');
        }else{
            inputs.classList.remove('invalid');
        }
    });
    if(!isValid){
        event.preventDefault();
    }
}
    document.querySelectorAll('form').forEach(form=>{
        form.addEventListener('submit', validateForm);
    });
