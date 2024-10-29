console.log(document.location.search);

document.addEventListener('DOMContentLoaded', postData);


const data = document.location.search;
const params = new URLSearchParams(data);

console.log(params)

const namee = params.get('fname');
const age = params.get('age');
const q1 = params.getAll('question1');
const q3 = params.getAll('question3');
const q5 = params.getAll('question5');
const q7 = params.getAll('question7');
const q2 = params.get('question2');
const q4 = params.get('question4');
const q6 = params.get('question6');


let colorWeights = [0, 0, 0, 0, 0];
console.log(namee);
console.log("name");
console.log(q1);
console.log("q1");
function weightsFromArrays(input){
    console.log(input);
    input.forEach(element => {
        weightsFromString(element);
    });
}

function weightsFromString(input){
    console.log(input);
    if (input == "red"){
        colorWeights[0] += 1;
    }
    if (input == "yellow"){
        colorWeights[1] += 1;
    }
    if (input == "green"){
        colorWeights[2] += 1;
    }
    if (input == "blue"){
        colorWeights[3] += 1;
    }
    if (input == "purple"){
        colorWeights[4] += 1;
    }
}

function updateWeights(){
    console.log("hello");
    weightsFromArrays(q1);
    weightsFromArrays(q3);
    weightsFromArrays(q5);
    weightsFromArrays(q7);
    weightsFromString(q2);
    weightsFromString(q4);
    weightsFromString(q6);
    console.log("hello2");
}

function postData() {
    const container = document.getElementById("results");
    updateWeights();
    container.innerHTML = `<h1>${q1} asfd</h1>`;
    console.log(colorWeights);
}
