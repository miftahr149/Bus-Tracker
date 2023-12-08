function submitFunctionGenerator(param) {
  const { currentPlace, destination, map } = param;
  const { addressList } = param;

  const getRoute = async (param) => {
    const data = await getMapboxRoute(param);
    console.log('apiData:')
    console.log(data);
    return data.routes[0].geometry;
  }

  const idControllerGenerator = () => {
    let counterId = 0;
    let previousRoute = [];
    let logList = [];
    
    const addRoute = (idRouteList) => {
      idRouteList.forEach(idRoute => previousRoute.push(idRoute));
    }

    const deleteRoute = () => {
      if (!previousRoute) return;

      previousRoute.forEach(idRoute => map.removeLayer(idRoute));
      while (previousRoute.length > 0) previousRoute.shift();

      console.log('successfully delete all layer');
      console.log(`previousRoute:`);
      console.log(previousRoute);
    };

    const setupRoute = async (param) => {
      const {location, id} = param;
      const {name: locationName, coordinates: locationCoordinates} = location;
      console.log(locationName, locationCoordinates);
      const nearestBusStop = getNearestBusStop({
        currentPosition: locationCoordinates,
        addressList: addressList
      })

      console.log(addressList);
      console.log(nearestBusStop);
      
      const route =  await getRoute({
        type: 'walking',
        currentPosition: locationCoordinates,
        destination: nearestBusStop.coordinates,
      })

      console.log('route');
      console.log(route);

      previousRoute.push(id);
      console.log('previous route');
      console.log(previousRoute);
      addLayertoMap({id: id, route: route, map: map})
    }

    const getId = () => {
      counterId++;
      const id = `userRoute-${counterId}`;
      return id;
    }

    const getLog = () => logList;

    return {
      deleteRoute: deleteRoute,
      addRoute: addRoute,
      setupRoute: setupRoute,
      getLog: getLog,
      getId: getId
    };
  };

  const idController = idControllerGenerator()

  return async () => {
    let currentPlaceCoords = await getAddressCoordinates(currentPlace.value);
    let destinationCoords = await getAddressCoordinates(destination.value);

    console.log(`currentPlace: ${currentPlaceCoords}`);
    console.log(`destnation: ${destinationCoords}`);

    map.flyTo({ center: currentPlaceCoords, zoom: 15 });
    idController.deleteRoute();
    
    idController.setupRoute({
      id: idController.getId(),
      location: {
        name: currentPlace.value,
        coordinates: currentPlaceCoords
      }
    })
    idController.setupRoute({
      id: idController.getId(),
      location: {
        name: destination.value,
        coordinates: destinationCoords
      }
    })
  };
}
