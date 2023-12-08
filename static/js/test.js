const createPointGeoJsonFeature = (addressData) => {
  let lat = addressData.latLng.lat;
  let long = addressData.latLng.long

  return {
    type: 'Feature',
    geometry: {
      type: 'Point',
      coordinates: [long, lat]
    },
    property: {
      title: addressData.name
    }
  }
}

const createBusStopsGeoJson = (addressList) => {
  let featureList = [];
  
  for (let address in addressList) {
    let [lat, long] = Object.values(addressList[address])
    
    featureList.push(createPointGeoJsonFeature({
      name: address,
      latLng: {
        lat: lat,
        long: long,
      } 
    }))
  }

  return {
    type: 'FetureCollection',
    features: featureList 
  }
}

const addMarker = (geoJson, map) => {
  for (const feature of geoJson.features) {
    let marker = new mapboxgl.Marker()
      .setLngLat(feature.geometry.coordinates)
      .addTo(map)
  } 
}

async function mainFunction() {
  const address = await fetchAddress();
  const busRoute = await fetchAddress();

  const [start_lat, start_long] = Object.values(address['Center Point UTM (CP)']);

  let map = new mapboxgl.Map({
    container: 'map',
    style: 'mapbox://styles/mapbox/streets-v12',
    center: [start_long, start_lat], 
    zoom: 18
  })

  const testFunction = testFunctionGenerator({
    addressList: address, 
    map: map
  });

  //center maps to userLocation
  if ("geolocation" in navigator) {
    const successLocation = async (position) => {
      const {longitude, latitude} = position.coords;
      const userPosition = [longitude, latitude];
      map.flyTo({ center: userPosition })

      map.on('load', async () => {
        console.log(address)
        const {lat, long} = address['Arked Meranti'];
        await testFunction({
          currentPosition: userPosition,
          destination: [long, lat]
        });
      });
    }

    const errorLocation = (position) => {
      console.error('Unable to retrieve data');
    }

    navigator.geolocation.getCurrentPosition(successLocation, errorLocation, {enableHighAccuracy: true});
  }

  // Creating Marker
  const geoJson = createBusStopsGeoJson(address);
  addMarker(geoJson, map)

  // Add Layer
}

mainFunction()