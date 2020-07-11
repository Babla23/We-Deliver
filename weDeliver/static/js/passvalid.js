function pswrd() {
    passw = document.getElementById('pass').value
    cpass = document.getElementById('cpass').value
    const button = document.querySelector('button')
    if (passw == cpass)
    {
        button.disabled = false
        document.getElementById('alert').innerText = ''
    }
    else
    {
        document.getElementById('alert').innerText = 'Password Does Not Match.'
        button.disabled= true
    }
}