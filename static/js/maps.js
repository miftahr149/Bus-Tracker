const mapElement = document.getElementById('map');
const HeaderElement = document.querySelector('.header');

function initMap() {
    var map = new google.maps.Map(mapElement, {
        center: { lat: 1.5590686924757557, lng: 103.63803147672287 },
        zoom: 15
    });
}

window.addEventListener('resize', () => {
    height = screen.height - HeaderElement.clientHeight;
    mapElement.style.height = `${height}px`;
    console.log(mapElement.style.height);
})