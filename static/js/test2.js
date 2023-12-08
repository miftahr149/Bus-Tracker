const testFunctionGenerator = (param) => {
    const {addressList, map} = param;
    
    const setupRoute = async (param) => {
        const {location, id} = param;
        const nearestBusStop = getNearestBusStop({
            currentPosition: location,
            addressList: addressList,
        });
        const data = await getMapboxRoute({
            type: "walking",
            currentPosition: location,
            destination: nearestBusStop.coordinates
        })
        const route = data.routes[0].geometry;
        addLayertoMap({id: 'route-1', route: route, map: map});
    }

    return async (param) => {
        const {currentPosition, destination} = param;
        setupRoute({location: currentPosition, id: "route-1"});
        setupRoute({location: destination, id: "route-2"});
    }
}