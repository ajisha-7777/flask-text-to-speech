function speakText() {
    let text = document.getElementById("textInput").value;
    let voiceSelect = document.getElementById("voiceSelect").value;

    if (!text) {
        alert("Please enter text to convert.");
        return;
    }

    let speech = new SpeechSynthesisUtterance(text);
    let voices = window.speechSynthesis.getVoices();
    
    // Voice selection based on male/female
    if (voiceSelect === "female") {
        speech.voice = voices.find(voice => voice.name.includes("Female")) || voices[0];
        speech.pitch = 1.5;  // Female voice high pitch
    } else {
        speech.voice = voices.find(voice => voice.name.includes("Male")) || voices[0];
        speech.pitch = 1;  // Male voice deep pitch
    }

    speech.lang = "en-US";
    speech.rate = 1;
    
    window.speechSynthesis.speak(speech);
}

function downloadAudio() {
    let text = document.getElementById("textInput").value;
    let voice = document.getElementById("voiceSelect").value;

    if (!text) {
        alert("Please enter text to download.");
        return;
    }

    fetch('/download_audio', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ text: text, voice: voice })
    })
    .then(response => response.blob())
    .then(blob => {
        let url = window.URL.createObjectURL(blob);
        let a = document.createElement("a");
        a.href = url;
        a.download = "speech.mp3";
        document.body.appendChild(a);
        a.click();
        document.body.removeChild(a);
    })
    .catch(error => console.error("Error:", error));
}