document.getElementById('uploadForm').addEventListener('submit', function(event) {
    event.preventDefault();
    const fileInput = document.getElementById('imageUpload');
    const resultDiv = document.getElementById('result');
    const file = fileInput.files[0];
    
    if (file) {
        const reader = new FileReader();
        reader.onload = function(e) {
            const img = new Image();
            img.src = e.target.result;
            img.onload = function() {
                // Simulasi proses deteksi penyakit gigi
                const detectionResult = detectToothDisease(img);
                resultDiv.innerHTML = `<p>${detectionResult}</p>`;
            }
        }
        reader.readAsDataURL(file);
    } else {
        resultDiv.innerHTML = `<p>Silakan unggah gambar terlebih dahulu.</p>`;
    }
});

function detectToothDisease(image) {
    // Simulasi deteksi penyakit gigi
    // Gantilah logika ini dengan algoritma deteksi yang sebenarnya
    return "Penyakit gigi terdeteksi: Karies";
}
