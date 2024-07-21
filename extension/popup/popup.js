document.getElementById('analyze').addEventListener('click', () => {
  fetch('http://localhost:5000/api/scrape')
    .then(response => response.json())
    .then(data => {
      document.getElementById('result').innerText = JSON.stringify(data);
    })
    .catch(error => {
      console.error('Error:', error);
    });
});
