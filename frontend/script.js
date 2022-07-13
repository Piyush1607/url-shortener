const form = document.querySelector('form')
const body = document.querySelector('.main-form')
const shortDiv = document.querySelector('.shorted-url')

const handleSubmit = async (e) =>{
    shortDiv.innerHTML = ''
    e.preventDefault()
    const longUrl = form.querySelector('input').value
    if(longUrl.length === 0)
        return

    form.querySelector('input').value = ''

    const b = { 
        "url" : longUrl
    }

    const res = await fetch('http://127.0.0.1:8000/',{
        method : 'POST',
        body :JSON.stringify(b),
        headers: {
            'Content-Type': 'application/json'
        },
    })

    const data = await res.json()
    console.log(data)
    const op = `The shortened URL is <a href=${data.short_url} target ='_blank' >${data.short_url}</a> <br>`
    shortDiv.insertAdjacentHTML('beforeend' ,op )
}

form.addEventListener('submit' , handleSubmit)