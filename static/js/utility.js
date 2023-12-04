const getNearestBusStop = (addressList) => {
    const setBusStopList = () => {
        result = [];
        for (address in addressList) {
            const [lat, long] = Object.values(addressList[address]);
            result.push({
                name: address,
                coordinates: [long, lat]
            })
        }
        return result;
    }
    
    return (userPosition) => {
        let nearestBusStop = null;
        let nearestDistance = Number.MAX_VALUE;
        const options = {units: 'miles'};

        setBusStopList().forEach(busStop => {
            const distance = turf.distance(
                userPosition, 
                busStop.coordinates,
                options
            );

            if (distance < nearestDistance) {
                nearestDistance = distance;
                nearestBusStop = busStop;
            }
        })

        return nearestBusStop
    }
}