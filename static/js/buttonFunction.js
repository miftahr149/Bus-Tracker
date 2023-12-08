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
    
    const addRoute = (idRouteList) => {
      idRouteList.forEach(idRoute => previousRoute.push(idRoute));
    }

    const deleteRoute = () => {
      if (!previousRoute) return;
      previousRoute.forEach((routeId) => map.removeLayer(routeId));
      previousRoute = [];
      console.log(`previousRoute: ${previousRoute}`);
    };

    const setupRoute = async (param) => {
      const {location, id} = param;
      const nearestBusStop = getNearestBusStop({
        currentPosition: location,
        addressList: addressList
      })

      console.log(addressList);
      console.log(nearestBusStop);
      
      const route =  await getRoute({
        type: 'walking',
        currentPosition: location,
        destination: nearestBusStop.coordinates,
      })

      console.log('route');
      console.log(route);

      addLayertoMap({id: id, route: route, map: map})
    }

    return {
      deleteRoute: deleteRoute,
      addRoute: addRoute,
      setupRoute: setupRoute
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
      id: 'userRoute-1',
      location: currentPlaceCoords
    })
    idController.setupRoute({
      id: 'userRoute-2',
      location: destinationCoords
    })
  };
}
