async function fetchData() {
    const response = await fetch('http://localhost/api/data'); // Update this URL if necessary
    const data = await response.json();
    const dataContainer = document.getElementById('data-container');

    if (Array.isArray(data)) {
        data.forEach(item => {
            const div = document.createElement('div');
            div.textContent = JSON.stringify(item);
            dataContainer.appendChild(div);
        });
    } else {
        dataContainer.textContent = 'No data available';
    }
}

fetchData();
