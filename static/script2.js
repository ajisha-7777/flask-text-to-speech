document.getElementById("play-btn").addEventListener("click", function () {
    let text = document.getElementById("text-input").value;

    if (!text.trim()) {
        alert("Please enter text!");
        return;
    }

    fetch("/convert", {
        method: "POST",
        body: new URLSearchParams({ text: text }),
        headers: { "Content-Type": "application/x-www-form-urlencoded" }
    })
    .then(response => response.text())
    .then(data => {
        if (data === "success") {
            let audio = new Audio("/static/audio/output.mp3");
            audio.play();
        }
    })
    .catch(error => console.error("Error:", error));
});