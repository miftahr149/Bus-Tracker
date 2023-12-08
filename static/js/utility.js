const getNearestBusStop = (param) => {
  const { currentPosition, addressList } = param;

  const setBusStopList = () => {
    result = [];
    for (address in addressList) {
      const { lat, long } = addressList[address];
      result.push({
        name: address,
        coordinates: [long, lat],
      });
    }
    return result;
  };

  const busStopList = setBusStopList();
  let nearestBusStop = null;
  let nearestDistance = Number.MAX_VALUE;
  let options = { units: "miles" };

  busStopList.forEach((busStop) => {
    const { coordinates } = busStop;
    const distance = turf.distance(currentPosition, coordinates, options);

    if (distance < nearestDistance) {
      nearestDistance = distance;
      nearestBusStop = busStop;
    }
  });

  return nearestBusStop;
};

const addLayertoMap = (param) => {
  let currentLayout = {
    "line-join": "round",
    "line-cap": "round",
  };

  let currentPaint = {
    "line-color": "#3887be",
    "line-width": 5,
    "line-opacity": 0.8,
  };

  const { id, route, map, source } = param;

  if ("layout" in param) {
    let { layout } = param;
    currentLayout = layout;
  }

  if ("paint" in param) {
    let { paint } = param;
    currentPaint = paint;
  }

  let objectLayer = {
    id: id,
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
    layout: currentLayout,
    paint: currentPaint,
  };

  if (source) objectLayer.source = source;
  map.addLayer(objectLayer);
};

const getMapboxRoute = async (param) => {
  console.log(param);
  const { type, currentPosition, destination } = param;
  const url = `https://api.mapbox.com/directions/v5/mapbox/${type}/${currentPosition[0]},${currentPosition[1]};${destination[0]},${destination[1]}?geometries=geojson&access_token=${accessToken}`;

  const data = await fetch(url).then((response) => response.json());
  return data;
};

const getAddressCoordinates = async (location) => {
  const data = await fetchGeocoding(location);
  console.log(data);
  const [lat, long] = data.coordinate;
  return [long, lat];
};