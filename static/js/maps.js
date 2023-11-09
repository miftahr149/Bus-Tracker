const mapElement = document.getElementById('map');
const routeElement = document.getElementById('maps-routes');

function initMap() {
    let map = new google.maps.Map(mapElement, {
        center: {
            lat: 1.5590686924757557,
            lng: 103.63803147672287
        },
        zoom: 16
    });
}

const configureMap = () => {
    let height = window.innerHeight - routeElement.offsetHeight;
    mapElement.style.height = `${0.95 * height}px`;
}

configureMap();
window.addEventListener('resize', () => {
    configureMap();
})