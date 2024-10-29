document.addEventListener('DOMContentLoaded', postData);

const data = document.location.search;
const params = new URLSearchParams(data);

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
let mostElement = 0;
let colorString = "";
let imgPath = "";
let description = "";

function weightsFromArrays(input) {
    input.forEach(element => {
        weightsFromString(element);
    });
}

function weightsFromString(input) {
    if (input == "red") { colorWeights[0] += 1; }
    if (input == "yellow") { colorWeights[1] += 1; }
    if (input == "green") { colorWeights[2] += 1; }
    if (input == "blue") { colorWeights[3] += 1; }
    if (input == "purple") { colorWeights[4] += 1; }
}

function updateWeights() {
    weightsFromArrays(q1);
    weightsFromArrays(q3);
    weightsFromArrays(q5);
    weightsFromArrays(q7);
    weightsFromString(q2);
    weightsFromString(q4);
    weightsFromString(q6);
}

function colorFromWeights() {
    min = -1
    for (let index = 0; index < colorWeights.length; index++) {
        const element = colorWeights[index];
        if (element > min) {
            min = element;
            mostElement = index;
        }
    }
    if (mostElement == 0) { colorString = "Red" }
    if (mostElement == 1) { colorString = "Yellow" }
    if (mostElement == 2) { colorString = "Green" }
    if (mostElement == 3) { colorString = "Blue" }
    if (mostElement == 4) { colorString = "Purple" }
}

function postData() {
    const container = document.getElementById("results");
    const bigContainer = document.getElementById("resultsPage");
    const imgContainer = document.getElementById("resultsImg");
    const descContainer = document.getElementById("resultsDesc");
    const titleContainer = document.getElementById("resultsTitle");
    updateWeights();
    colorFromWeights();
    switch (colorString) {
        case 'Red':
            bigContainer.style.backgroundColor = '#ff4d4d';
            bigContainer.style.textDecorationColor = '#ffffff'
            imgPath = 'images/red.jpg';
            descContainer.innerHTML = `<p class="spaced1">
<strong>Personality Traits:</strong> Bold, energetic, passionate, and determined.</p><p class="spaced">
<strong>Impression:</strong> Red conveys confidence, excitement, and a high level of energy. People who resonate with red often come across as leaders, action-oriented, and driven by goals. </p><p class="spaced">
<strong>Ideal For:</strong> Roles that require leadership, enthusiasm, or the ability to take initiative. Great for someone who wants to emphasize their passion and commitment.</p>`
            break;
        case 'Yellow':
            bigContainer.style.backgroundColor = '#ffd633';
            imgPath = 'images/orange.jpg';
            descContainer.innerHTML = `<p class="spaced1">
<strong>Personality Traits:</strong> Optimistic, cheerful, creative, and open-minded.</p><p class="spaced">
<strong>Impression:</strong> Yellow reflects positivity, curiosity, and an inventive spirit. It’s the color of ideas, intellect, and joy.</p><p class="spaced">
<strong>Ideal For:</strong> Positions that value innovation, creativity, or an upbeat approach to problem-solving. Ideal for showing a sunny disposition and a unique perspective.</p>`
            break;
        case 'Green':
            bigContainer.style.backgroundColor = '#85e085';
            imgPath = 'images/green.jpg';
            descContainer.innerHTML = `<p class="spaced1">
<strong>Personality Traits:</strong> Calm, balanced, nurturing, and growth-oriented.</p><p class="spaced">
<strong>Impression:</strong> Green represents harmony, sustainability, and reliability. It’s often associated with growth and stability.</p><p class="spaced">
<strong>Ideal For:</strong> Roles emphasizing teamwork, patience, and a methodical approach. Perfect for someone who values balance, collaboration, and supporting others.</p>`
            break;
        case 'Blue':
            bigContainer.style.backgroundColor = '#4da6ff';
            imgPath = 'images/blue.jpg';
            descContainer.innerHTML = `<p class="spaced1">
<strong>Personality Traits:</strong> Trustworthy, calm, analytical, and reliable.</p><p class="spaced">
<strong>Impression:</strong> Blue gives off a dependable, trustworthy vibe. It’s associated with logic, stability, and calm problem-solving.</p><p class="spaced">
<strong>Ideal For:</strong> Analytical roles or positions requiring precision and reliability. Great for conveying trustworthiness, thoughtfulness, and a methodical mindset.</p>`
            break;
        case 'Purple':
            bigContainer.style.backgroundColor = '#c299ff';
            imgPath = 'images/purple.jpg';
            descContainer.innerHTML = `<p class="spaced1">
<strong>Personality Traits:</strong> Imaginative, wise, introspective, and insightful.</p><p class="spaced">
<strong>Impression:</strong> Purple combines the energy of red and the calm of blue, symbolizing creativity, luxury, and depth. It’s a color for those with big ideas and thoughtful approaches.</p><p class="spaced">
<strong>Ideal For:</strong> Roles valuing innovation, creativity, and strategic thinking. Great for someone who wants to come across as insightful and original.</p>`
            break;
        default:
            container.style.backgroundColor = '#ffffff'; // Default to white if no match
    }
    titleContainer.innerHTML = `<h2>${namee}, Your personality color is:</h2>`
    container.innerHTML = `<h1>${colorString}!</h1>`;
    imgContainer.innerHTML = `<img src="${imgPath}" alt="personalityImg">`
    console.log(colorWeights);
}










