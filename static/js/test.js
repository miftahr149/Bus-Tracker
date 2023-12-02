let userPosition;

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

const getNearestBusStop = (userPosition, addressList) => {
  const setBusStop = () => {
    result = [];
    for (address in addressList) {
      const [lat, long] = Object.values(addressList[address])
      result.push({
        name: address,
        coordinates: [long, lat]
      })
    }
    return result;
  }

  const busStopList = setBusStop();
  let nearestBusStop = null;
  let nearestDistance = Number.MAX_VALUE;
  let options = {units: 'miles'};
  
  busStopList.forEach(busStop => {
    const distance = turf.distance(userPosition, busStop.coordinates, options)

    if (distance < nearestDistance) {
      nearestDistance = distance;
      nearestBusStop = busStop;
    }
  })

  return nearestBusStop;
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
  const route = await fetchAddress();

  const [start_lat, start_long] = Object.values(address['Center Point UTM (CP)']);

  let map = new mapboxgl.Map({
    container: 'map',
    style: 'mapbox://styles/mapbox/streets-v12',
    center: [start_long, start_lat], 
    zoom: 18
  })

  //center maps to userLocation
  if ("geolocation" in navigator) {
    const successLocation = async (position) => {
      const userPosition = [position.coords.longitude, position.coords.latitude];
      map.flyTo({ center: userPosition })
      const nearestBusStop = getNearestBusStop(userPosition, address);
      
      const [long, lat] = nearestBusStop.coordinates;
      url = `https://api.mapbox.com/directions/v5/mapbox/walking/${userPosition[0]},${userPosition[1]};${long},${lat}?geometries=geojson&access_token=${mapbox_access_token}`;

      const response = await fetch(url);
      const data = await response.json();

      let route = data.routes[0].geometry;
      map.on('load', () => {
        map.addLayer({
          id: 'route',
          type: 'line',
          source: {
            type: 'geojson',
            data: {
              type: 'Feature',
              properties: {},
              geometry: {
                type: 'LineString',
                coordinates: route.coordinates,
              }
            }
          },
          layout: {
            'line-join': 'round',
            'line-cap': 'round'
          },
          paint: {
            'line-color': "#3887be",
            'line-width': 5,
            'line-opacity': 0.8
          }
        })
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