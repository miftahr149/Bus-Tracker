const addMarker = (addressList, map) => {
  const createGeoJSONFeature = () => {
    featureList = [];
    for (address in addressList) {
      const [lat, long] = Object.values(addressList[address]);
      featureList.push({
        type: "Feature",
        geometry: {
          type: "Point",
          coordinates: [long, lat],
        },
        property: {
          title: address,
        },
      });
    }
    return featureList;
  };

  createGeoJSONFeature().forEach((addressData) => {
    const divElement = document.createElement('div');
    divElement.className = 'marker marker--bus-stop';
    
    new mapboxgl.Marker(divElement)
      .setLngLat(addressData.geometry.coordinates)
      .addTo(map);
  });
};

async function mainFunction() {
  const address = await fetchAddress();
  const route = await fetchRoute();
  const currentPlace = document.getElementById("current_place");
  const destination = document.getElementById("destination");

  const [start_lat, start_long] = Object.values(
    address["Center Point UTM (CP)"]
  );

  let map = new mapboxgl.Map({
    container: "map",
    center: [start_long, start_lat],
    style: "mapbox://styles/mapbox/streets-v12",
    zoom: 18,
  });

  // get user current place
  if ("geolocation" in navigator) {
    const successLocation = async (position) => {
      const userPosition = [
        position.coords.longitude,
        position.coords.latitude,
      ];

      map.flyTo({ center: userPosition });

      const url = `https://api.mapbox.com/geocoding/v5/mapbox.places/${userPosition[0]},${userPosition[1]}.json?access_token=${accessToken}`;

      const apiData = await fetch(url).then((response) => response.json());
      const currentPositionAddress = apiData.features[0].place_name;
      currentPlace.value = currentPositionAddress;
    };

    const errorLocation = (error) => {
      console.error("Unable to retrieve data");
    };

    navigator.geolocation.getCurrentPosition(successLocation, errorLocation, {
      enableHighAccuracy: true,
    });
  }

  addMarker(address, map);

  //find route event listener

  const routeButton = document.querySelector(".route__button");
  routeButton.addEventListener(
    "click",
    submitFunctionGenerator({
      currentPlace: currentPlace,
      destination: destination,
      map: map,
      addressList: address
    })
  );
}

mainFunction();
