async function checkURL() {
    const url = document.getElementById("urlInput").value;
    const resultDiv = document.getElementById("result");

    if (!url) {
        resultDiv.innerText = "Please enter a URL!";
        return;
    }

    try {
        const baseURL = window.location.origin;
        const response = await fetch(`${baseURL}/predict`, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ url: url })
        });

        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }

        const data = await response.json();
        resultDiv.innerText = `Prediction: ${data.prediction} (Confidence: ${data.confidence})`;
    } catch (error) {
        console.error("Error fetching prediction:", error);
        resultDiv.innerText = "Failed to fetch prediction. Check console for details.";
    }
}
