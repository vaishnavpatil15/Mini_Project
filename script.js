document.getElementById('cropForm').addEventListener('submit', function(event) {
    event.preventDefault();

    const nitrogen = document.getElementById('nitrogen').value;
    const phosphorus = document.getElementById('phosphorus').value;
    const potassium = document.getElementById('potassium').value;
    const temperature = document.getElementById('temperature').value;
    const humidity = document.getElementById('humidity').value;
    const ph = document.getElementById('ph').value;
    const rainfall = document.getElementById('rainfall').value;

    const data = {
        nitrogen,
        phosphorus,
        potassium,
        temperature,
        humidity,
        ph,
        rainfall
    };

    fetch('/api/predict', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(data => {
        console.log('API Response:', data);
        const resultDiv = document.getElementById('result');
        if (data.recommended_crop) {
            resultDiv.innerHTML = `<p>Recommended Crop: <strong>${data.recommended_crop}</strong></p>`;
        } else {
            resultDiv.innerHTML = `<p>Error: ${data.error || 'Unknown error occurred'}</p>`;
        }
        resultDiv.style.display = 'block';
    })
    .catch(error => {
        console.error('Error:', error);
    });
});
