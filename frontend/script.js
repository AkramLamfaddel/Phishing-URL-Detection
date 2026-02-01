async function checkURL() {
    const url = document.getElementById("urlInput").value;
    const resultDiv = document.getElementById("result");

    if (!url) {
        resultDiv.innerText = "Please enter a URL!";
        return;
    }

    const response = await fetch("http://127.0.0.1:8000/predict", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({ url: url })
    });

    const data = await response.json();
    resultDiv.innerText = `Prediction: ${data.prediction} (Confidence: ${data.confidence})`;
}