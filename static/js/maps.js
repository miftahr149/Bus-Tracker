const mapElement = document.getElementById('map');
const routeElement = document.getElementById('maps-routes');

const configureMap = () => {
    let height = window.innerHeight - routeElement.offsetHeight;
    mapElement.style.height = `${0.95 * height}px`;
}

configureMap();
window.addEventListener('resize', () => {
    configureMap();
})