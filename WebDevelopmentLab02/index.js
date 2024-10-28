console.log(document.location.search);

document.addEventListener('DOMContentLoaded', postData)


const data = document.location.search;
const params = new URLSearchParams();

const name = params.get('fname');
const amount = params.get('amount');
const genre = params.getAll('genre');
const medical = params.get('medical');
const thriller = params.get('thriller')

let characters;

if (medical == "ER" && thriller == "a") {
    characters = 'er and a'
}
else if (medical == "greys" && thriller == "asdf") {
    characters = 'greys and asdf'
}
else if (medical == "chicago-med" && thriller == "b") {
    characters = 'chicago and b'
}
else {
    characters = 'everything else'
}

console.log(characters)

function postData() {
    const container = document.getElementById("results");
    container.innerHTML = `<h1>${characters} asfd</h1>`;
}
