async function displayConfidence() {
    const file = document.getElementById("image-input").files[0];

    const formData = new FormData();
    formData.append("file", file);

    document.getElementById("result").innerText = "Analyzing...";
    document.getElementById("healing-score").innerText = "";
    document.getElementById("advice").innerText = "";

    const res = await fetch("http://127.0.0.1:8000/upload-image", {
        method: "POST",
        body: formData
    });

    const data = await res.json();

    document.getElementById("result").innerText = data.result;
    document.getElementById("healing-score").innerText = "Healing Score: " + data.healing_score;
    document.getElementById("advice").innerText = data.advice;
}

function previewImage() {
    const file = document.getElementById("image-input").files[0];
    document.getElementById("preview").src = URL.createObjectURL(file);
}