document.getElementById('matchForm').onsubmit = function(event) {
    event.preventDefault();

    // Display loading message
    document.getElementById('matchResult').innerHTML = '<p>Finding your match...</p>';

    let formData = new FormData(this);

    fetch('/match', {
        method: 'POST',
        body: formData,
    })
    .then(response => response.json())
    .then(data => {
        if(data.error) {
            document.getElementById('matchResult').innerHTML = `<p>${data.error}</p>`;
        } else {
            document.getElementById('matchResult').innerHTML = 
                `<p>${data.name} (${data.gender}, Age: ${data.age}, Height: ${data.height} inches) is your best match! Have fun, but not too much fun! </p>`;
        }
    })
    .catch(error => {
        console.error('Error:', error);
        document.getElementById('matchResult').innerHTML = '<p>Error finding match. Please try again.</p>';
    });
};
