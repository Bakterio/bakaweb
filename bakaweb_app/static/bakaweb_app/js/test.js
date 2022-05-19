function test() {
    console.log("test print");
}

function send() {
    console.log("form");
}
const form = document.getElementById('id_url')

form.addEventListener('change', ()=> {
    console.log("changed!!!")
})