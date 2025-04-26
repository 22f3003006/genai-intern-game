let score = 0;
let userId = '1';  // fake session
started=false

backend=window.location.hostname.includes('localhost') 
? "http://127.0.0.1:8000" 
: "https://genai-intern-game.up.railway.app";

function toggleInputs(enabled) {
    document.getElementById("guessInput").disabled = !enabled;
    document.getElementById("personaInput").disabled = !enabled;
    document.getElementById("guess").disabled = !enabled;
}

function clearInputs() {
    document.getElementById("guessInput").value = "";
    document.getElementById("feedback").innerText = "";
    document.getElementById("verdict").innerText = "";
    document.getElementById("score").innerText = "";
    document.getElementById("history").innerHTML = "";
    document.getElementById("total").innerHTML = "";
}

if (!started) { toggleInputs(false) }

async function startGame() {
    started=true
    toggleInputs(true)
    clearInputs()
    document.getElementById("start").disabled = true;
    userId = '1';  // Set your fake or real user ID
    const res = await fetch(`${backend}/start`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({ id: userId }),
    });
    const data = await res.json();
    console.log(data)
}

async function restartGame() {
    await startGame();
}

async function makeGuess() {
    const guess = document.getElementById("guessInput").value;
    const persona = document.getElementById("personaInput").value;
    document.getElementById("feedback").innerText = "Loading...";
    document.getElementById("verdict").innerText = "";
    const res = await fetch(`${backend}/guess`, {
                    method: "POST",
                    headers: {
                    "Content-Type": "application/json",
                    },
                    body: JSON.stringify({
                    id: userId,
                    guess: guess,
                    persona: persona
                    }),
                });       
    const data = await res.json();
    console.log(data)
    document.getElementById("feedback").innerText = data.message;
    document.getElementById("total").innerText = `Total Global Count of this Guess: ${data.total}`;
    if (data.verdict) {
        document.getElementById("verdict").innerText = data.verdict;
    }
    if (data.score !== undefined) {
        score=data.score
        document.getElementById("score").innerText = score;
        const list = document.getElementById("history");
        list.innerHTML = "";
        data.history.forEach(word => {
            const li = document.createElement("li");
            li.textContent = word;
            list.appendChild(li);
        });
    }
}
