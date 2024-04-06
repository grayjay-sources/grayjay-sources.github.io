function generateCard(data) {
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
                        <a href="grayjay://plugin/${encodeURIComponent(data.sourceUrl)}" target="_blank" rel="noopener noreferrer"><<button type="button" class="btn btn-sm btn-outline-secondary">Install</button></a>
                        <a href="${data.repositoryUrl}" target="_blank" rel="noopener noreferrer"><button type="button" class="btn btn-sm btn-outline-secondary">Source</button></a>
                        </div>
                        <small class="text-body-secondary">${data.author}</small>
                    </div>
                </div>
            </div>
        </div>
    `;
    return html;
}
async function populateCardsContainer(url) {
    try {
        const response = await fetch(url);
        const data = await response.json();
        const cardsContainer = document.getElementById('cards-container');
        cardsContainer.innerHTML = "";
        data.forEach(item => {
            const cardHtml = generateCard(item);
            cardsContainer.innerHTML += cardHtml;
        });
    } catch (error) {
        console.error('Error fetching data:', error);
    }
}
document.addEventListener('DOMContentLoaded', () => {
    const url = 'https://raw.githubusercontent.com/grayjay-sources/repo/main/sources.json';
    populateCardsContainer(url);
});
