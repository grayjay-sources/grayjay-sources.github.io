function removeLast (inputString, separator) {
  const lastIndex = inputString.lastIndexOf(separator)
  if (lastIndex > 0) return inputString.substring(0, lastIndex)
  else return ''
}
function isQueryParamSet (paramName) {
  const searchParams = new URLSearchParams(window.location.search)
  return searchParams.has(paramName)
}
function isRelativeUrl (url) {
  return url.startsWith('./')
}
function getAbsoluteUrl (url, baseUrl) {
  if (isRelativeUrl(url)) {
    return url.replace('./', baseUrl)
  }
  return url
}
function getSourceFeeds (data, key) {
  const urls = []
  data.forEach((item) => {
    if (!item.hasOwnProperty('_feeds')) return
    if (item._feeds.hasOwnProperty(key)) { urls.push(encodeURI(item._feeds[key])) }
    // else console.warn(`Source ${item.name} has no ${key}`);
  })
  console.log('URLs:', urls) // Log encoded URLs
  const urlCount = urls.length
  const baseUrl = 'https://rssmerge.onrender.com' // Use the current page's origin as the base URL
  console.log('Base URL:', baseUrl) // Log base URL
  const params = new URLSearchParams({
    title: `${urlCount} ${key}`,
    urls: urls.join(',')
  }).toString()
  const finalUrl = `${baseUrl}/?${params}`
  console.log('Final URL:', finalUrl) // Log final URL
  return finalUrl
}
function fixData (data) {
  data.baseUrl = removeLast(data.sourceUrl, '/') + '/'
  if (!data.hasOwnProperty('_feeds')) data._feeds = {}
  if (!data.hasOwnProperty('_tags')) data._tags = {}
  for (const [key, value] of Object.entries(data)) {
    if (key.toLowerCase().includes('url')) {
      if (Array.isArray(value)) continue
      if (isRelativeUrl(value)) {
        data[key + '_'] = value
        data[key] = getAbsoluteUrl(value, data.baseUrl)
      }
    }
  }
  console.log(data)
  return data
}
function generateQrCode (url) {
  const qr = new QRious({ value: url })
  return `<img class="source-qrcode" alt="QR Code" src="${qr.toDataURL()}" style="display:none"></img>`
}
function getFavicon (url, size = 128) {
  console.log(url)
  if (!url.startsWith('http')) {
    url = `http://${url}`
  }
  url = new URL(url)
  return `https://www.google.com/s2/favicons?domain=${url.hostname}&sz=${size}` // `https://icons.adguard.org/icon?domain=${url.hostname}`
}
function generateCard (data) {
  const sourceUrlEncoded = encodeURIComponent(data.sourceUrl)
  console.log(sourceUrlEncoded)
  const installUrl = `grayjay://plugin/${data.sourceUrl}`
  const repoUrl = data.repositoryUrl ?? data.configUrl
  if (!data.iconUrl) {
    if (data.platformUrl) {
      data.iconUrl = getFavicon(data.platformUrl)
    } else {
      data.iconUrl = getFavicon(data.allowUrls[0])
    }
  }
  let author = data.author
  if (author === 'FUTO') author = `<b>${data.author}</b>`
  /*  */
  let html = `
        <div class="col">
            <div class="card shadow-sm">
            <div class="card-header"><b>${data.name}</b></div>`
  if (data.iconUrl) {
    html += `<img class="source-icon" alt="${data.name}" src="${data.iconUrl}" width="auto" height="auto" style="display:block"></img>`
  } else {
    html += `<svg class="bd-placeholder-img card-img-top" width="auto" height="auto" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Source Icon" preserveAspectRatio="xMidYMid slice" focusable="false">
        <title>${data.name} Source Icon</title>
        <rect width="auto" height="auto" fill="#55595c"></rect>
        <text x="50%" y="50%" fill="#eceeef" dy=".3em"><b>${data.name}</b></text>
        </svg>`
  }
  html += generateQrCode(installUrl)
  html += `<div class="card-body">
                    <p class="card-text">${data.description}</p>
                    <div class="d-flex justify-content-between align-items-center">
                        <div class="btn-group">
                        <a href="${installUrl}" target="_blank" rel="noopener noreferrer"><button type="button" class="btn btn-sm btn-primary">Install</button></a>&nbsp;
                        <a href="${repoUrl}" target="_blank" rel="noopener noreferrer"><button type="button" class="btn btn-sm btn-outline-secondary">Source</button></a>
    `
  if (data._customButtons) {
    html += '<br>'
    data._customButtons.forEach((btn) => {
      html += `&nbsp;<a href="${btn.url}" target="_blank" rel="noopener noreferrer"><button type="button" class="btn btn-sm ${btn.classes}">${btn.text}</button></a>`
    })
  }
  html += `</div>
                        <small class="text-body-secondary">${data.author}</small>
                    </div>
                </div>
            </div>
        </div>
    `
  return html
}
async function addNavbarItem (text, url, spacer = false) {
  const navbarMenu = document.querySelector(
    'body > header > div.navbar.navbar-dark.bg-dark.shadow-sm > div > li > ul'
  )

  if (spacer) {
    const hrElement = document.createElement('hr')
    hrElement.className = 'dropdown-divider'
    const listItemElement = document.createElement('li')
    listItemElement.appendChild(hrElement)
    navbarMenu.appendChild(listItemElement)
  }

  const anchorElement = document.createElement('a')
  anchorElement.className = 'dropdown-item'
  anchorElement.target = '_blank'
  anchorElement.rel = 'noopener noreferrer'
  anchorElement.href = url
  anchorElement.textContent = text
  const listItemElement = document.createElement('li')
  listItemElement.appendChild(anchorElement)
  navbarMenu.appendChild(listItemElement)
}
async function populateCardsContainer (url) {
  try {
    const response = await fetch(url)
    const data = await response.json()
    const cardsContainer = document.getElementById('cards-container')
    cardsContainer.innerHTML = ''
    data.forEach((item) => {
      const fixedItem = fixData(item)
      const tags = fixedItem._tags ?? []
      console.log(tags)
      // const shouldHideNsfw =!isQueryParamSet("nsfw") && tags.includes("nsfw");
      // const shouldHideNonWorking = isQueryParamSet("working") &&!tags.includes("working");
      // const shouldHideNonOfficial = isQueryParamSet("official") &&!tags.includes("official");
      // if (!shouldHideNsfw ||!shouldHideNonWorking ||!shouldHideNonOfficial) {
      //     const cardHtml = generateCard(fixedItem);
      //     cardsContainer.innerHTML += cardHtml;
      // }

      if (isQueryParamSet('nsfw') || !tags.includes('nsfw')) {
        const cardHtml = generateCard(fixedItem)
        cardsContainer.innerHTML += cardHtml
      }
    })

    const commitFeedsUrl = getSourceFeeds(data, 'commits')
    addNavbarItem('Source Commits RSS Feed', commitFeedsUrl, true)
    const releaseFeedsUrl = getSourceFeeds(data, 'releases')
    addNavbarItem('Sources Releases RSS Feed', releaseFeedsUrl)
  } catch (error) {
    console.error('Error fetching data:', error)
  }
}
function toggleQRCodes () {
  const firstSourceIcon = document.getElementsByClassName('source-icon')[0]
  const sourceIconStyle = firstSourceIcon.getAttribute('style')
  if (sourceIconStyle == 'display:block') {
    document.querySelectorAll('.source-icon').forEach((element) => {
      element.setAttribute('style', 'display:none')
    })
    document.querySelectorAll('.source-qrcode').forEach((element) => {
      element.setAttribute('style', 'display:block')
    })
  } else {
    document.querySelectorAll('.source-icon').forEach((element) => {
      element.setAttribute('style', 'display:block')
    })
    document.querySelectorAll('.source-qrcode').forEach((element) => {
      element.setAttribute('style', 'display:none')
    })
  }
}
document.addEventListener('DOMContentLoaded', () => {
  const url =
    'https://raw.githubusercontent.com/grayjay-sources/repo/main/sources.json'
  populateCardsContainer(url)
  document.querySelectorAll('#bd-qrcodes').forEach((toggle) => {
    toggle.addEventListener('click', toggleQRCodes)
  })
})
