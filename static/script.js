function getCropInfo() {
    let cropName = document.getElementById("crop-name").value.trim();

    if (cropName === "") {
        alert("Please enter a crop name.");
        return;
    }
    
    fetch(`http://localhost:5000/crop-info?name=${encodeURIComponent(cropName)}`)
        .then(response => response.json())
        .then(data => {
            if (data.error) {
                document.getElementById("crop-details").innerHTML = `<p>${data.error}</p>`;
            } else {
                document.getElementById("crop-details").innerHTML = `
                    <h3>${data.name}</h3>
                    <p>Best Season: ${data.season}</p>
                    <p>Soil Type: ${data.soil}</p>
                    <p>Water Requirement: ${data.water}</p>
                    <p>Pests & Diseases: ${data.pests}</p>
                `;
            }
        })
        .catch(error => console.error("Error fetching crop info:", error));
}