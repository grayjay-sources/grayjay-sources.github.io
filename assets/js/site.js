function generateCard(data) {
    // Assuming the data object has the following structure:
    // {
    //     title: 'Card Title',
    //     text: 'Card Text',
    //     time: '9 mins'
    // }

    // Generate the HTML
    const html = `
        <div class="col">
            <div class="card shadow-sm">
                <svg class="bd-placeholder-img card-img-top" width="100%" height="225" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Placeholder: Thumbnail" preserveAspectRatio="xMidYMid slice" focusable="false">
                    <title>Placeholder</title>
                    <img width="100%" height="100%" fill="#55595c" src="${data.iconUrl}"></img>
                    <text x="50%" y="50%" fill="#eceeef" dy=".3em">${data.name}</text>
                </svg>
                <div class="card-body">
                    <p class="card-text">${data.description}</p>
                    <div class="d-flex justify-content-between align-items-center">
                        <div class="btn-group">
                            <button type="button" class="btn btn-sm btn-outline-secondary">View</button>
                            <button type="button" class="btn btn-sm btn-outline-secondary">Edit</button>
                        </div>
                        <small class="text-body-secondary">${data.author}</small>
                    </div>
                </div>
            </div>
        </div>
    `;

    // Return the generated HTML
    return html;
}

// Function to fetch JSON data and populate the cards container
async function populateCardsContainer(url) {
    try {
        // Fetch JSON data from the provided URL
        const response = await fetch(url);
        // Parse the JSON data
        const data = await response.json();

        // Get the cards container element
        const cardsContainer = document.getElementById('cards-container');

        cardsContainer.innerHTML = "";

        // Loop through the data and generate cards
        data.forEach(item => {
            // Assuming the data object has the necessary properties for generateCard
            const cardHtml = generateCard(item);
            // Insert the generated card HTML into the cards container
            cardsContainer.innerHTML += cardHtml;
        });
    } catch (error) {
        console.error('Error fetching data:', error);
    }
}

// Call the function on page load
document.addEventListener('DOMContentLoaded', () => {
    const url = 'https://raw.githubusercontent.com/grayjay-sources/repo/main/sources.json';
    populateCardsContainer(url);
});
