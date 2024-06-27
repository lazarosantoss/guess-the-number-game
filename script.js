function makeGuess() {
    const guess = document.getElementById('guessInput').value;
    fetch(`/guess?number=${guess}`)
        .then(response => response.json())
        .then(data => {
            document.getElementById('result').textContent = data.message;
        });
}
