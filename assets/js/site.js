function removeLast(inputString, separator) {
    var lastIndex = inputString.lastIndexOf(separator);
    if (lastIndex > 0) return inputString.substring(0, lastIndex);
    else return "";
}
function isQueryParamSet(paramName) {
    const searchParams = new URLSearchParams(window.location.search);
    return searchParams.has(paramName);
}
function isRelativeUrl(url) {
    return url.startsWith("./");
}
function getAbsoluteUrl(url, baseUrl) {
    if (isRelativeUrl(url)) {
        return url.replace("./", baseUrl);
    }
    return url;
}
function fixData(data) {
    data["baseUrl"] = removeLast(data.sourceUrl, "/") + "/";
    for (const [key, value] of Object.entries(data)) {
        if (key.toLowerCase().includes("url")) {
            if (Array.isArray(value)) continue;
            if (isRelativeUrl(value)) {
                data[key+"_"] = value;
                data[key] = getAbsoluteUrl(value, data["baseUrl"]);
            }
        }
    }
    console.log(data);
    return data;
}
function generateQrCode(url) {
    var qr = new QRious({ value: url });
    return `<img class="source-qrcode" alt="QR Code" src="${qr.toDataURL()}" style="display:none"></img>`;
}
function generateCard(data) {
    // const sourceUrlEncoded = encodeURIComponent(data.sourceUrl);
    const installUrl = `grayjay://plugin/${data.sourceUrl}`;
    const repoUrl = data.repositoryUrl ?? data.configUrl;
    /*  */
    let html = `
        <div class="col">
            <div class="card shadow-sm">
            <div class="card-header"><b>${data.name}</b></div>`;
    if (data.iconUrl) {
        html += `<img class="source-icon" alt="${data.name}" src="${data.iconUrl}" width="auto" height="auto"></img>`;
    }
        // html += `<svg class="bd-placeholder-img card-img-top" width="auto" height="auto" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Source Icon" preserveAspectRatio="xMidYMid slice" focusable="false">
        // <title>${data.name} Source Icon</title>
        // <rect width="auto" height="auto" fill="#55595c"></rect>
        // <text x="50%" y="50%" fill="#eceeef" dy=".3em"><b>${data.name}</b></text>
        // </svg>`;
        html += generateQrCode(installUrl);
    }
    html +=`<div class="card-body">
                    <p class="card-text">${data.description}</p>
                    <div class="d-flex justify-content-between align-items-center">
                        <div class="btn-group">
                        <a href="${installUrl}" target="_blank" rel="noopener noreferrer"><button type="button" class="btn btn-sm btn-primary">Install</button></a>&nbsp;
                        <a href="${repoUrl}" target="_blank" rel="noopener noreferrer"><button type="button" class="btn btn-sm btn-outline-secondary">Source</button></a>
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
            const fixedItem = fixData(item);
            const showNsfw = isQueryParamSet("nsfw");
            if (showNsfw || !fixedItem.nsfw) {
                const cardHtml = generateCard(fixedItem);
                cardsContainer.innerHTML += cardHtml;
            }
        });
    } catch (error) {
        console.error('Error fetching data:', error);
    }
}
document.addEventListener('DOMContentLoaded', () => {
    const url = 'https://raw.githubusercontent.com/grayjay-sources/repo/main/sources.json';
    populateCardsContainer(url);
});
