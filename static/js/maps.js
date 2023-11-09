const mapElement = document.getElementById('map');
const HeaderElement = document.querySelector('.header');

function initMap() {
    let map = new google.maps.Map(mapElement, {
        center: {
            lat: 1.5590686924757557,
            lng: 103.63803147672287
        },
        zoom: 16
    });
}

const configureMapElement = () => {
    height = screen.height - HeaderElement.clientHeight - 50;
    width = screen.width - 50;

    console.log(`${HeaderElement.clientWidth}`)

    mapElement.style.height = `${85 / 100 * height}px`;
}

configureMapElement();
window.addEventListener('resize', () => {
    configureMapElement()
});