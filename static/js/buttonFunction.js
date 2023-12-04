function createSubmitFunction(currentPlace, destination, map) {
    const getGeocoding = async (address) => {
      const response = await fetchGeocoding(address);
      const [lat, long] = response.coordinate;
      return [long, lat];
    };
  
    const createIdFunction = () => {
      let counterId = 0;
      let previousRoute = [];
  
      const functionId = (n) => `route-${n}`;
  
      const createRouteId = () => {
        counterId++;
        const value = functionId(counterId);
        previousRoute.push(value);
        return value;
      }
  
      const deleteRoute = () => {
        if (!previousRoute) return;
        previousRoute.forEach(routeId => map.removeLayer(routeId));
      }
  
      return [createRouteId, deleteRoute];
    }
  
    const [createRouteId, deletePreviousRoute] = createIdFunction();
  
    const fetchApi = async (currentPlaceCoords, destinationCoords) => {
      let url = `https://api.mapbox.com/directions/v5/mapbox/walking/${currentPlaceCoords[0]},${currentPlaceCoords[1]};${destinationCoords[0]},${destinationCoords[1]}?geometries=geojson&access_token=${accessToken}`;
  
      let response = await fetch(url);
      let data = await response.json();
      return data;
    };
  
    const addRouteToMap = (dataFetchApi) => {
      const route = dataFetchApi.routes[0].geometry;
      map.addLayer({
        id: createRouteId(),
        type: "line",
        source: {
          type: "geojson",
          data: {
            type: "Feature",
            properties: {},
            geometry: {
              type: "LineString",
              coordinates: route.coordinates,
            },
          },
        },
        layout: {
          "line-join": "round",
          "line-cap": "round",
        },
        paint: {
          "line-color": "#3887be",
          "line-width": 5,
          "line-opacity": 0.8,
        },
      });
    }

    const configureRoute = (currentPlaceCoords, destinationCoords) => {
      if (!("geolocation" in navigator)) return;
      navigator.geolocation.getCurrentPosition(async (position) => {
        const coordinates = position.coords;
        const userPosition = [coordinates.longitude, coordinates.latitude];
      })
    }
  
  
    return async () => {
      let currentPlaceCoords = await getGeocoding(currentPlace.value);
      let destinationCoords = await getGeocoding(destination.value);
      map.flyTo({ center: currentPlaceCoords, zoom: 15 });
      deletePreviousRoute();
      let data = await fetchApi(currentPlaceCoords, destinationCoords);
      addRouteToMap(data);
      configureRoute();
    };
  }