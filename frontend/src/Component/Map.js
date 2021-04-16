/*global google*/
import React, { useEffect, useState } from "react";
import {
  withGoogleMap,
  GoogleMap,
  DirectionsRenderer
} from "react-google-maps";

export function Map(props) {
  const [state, setState] = useState({
    directions: null
  });
  
  useEffect(()=>{
    const directionsService = new google.maps.DirectionsService();
    const backupOrigin = null; // { lat: 40.756795, lng: -73.954298 };
    const backupDestination = null; // { lat: 41.756795, lng: -78.954298 };

    if(props.allPlaces[0]) console.log(props.allPlaces[0].geometry.location);

    const beginId = props.schedule[0] ? props.schedule[0] : null;
    const endId = (props.schedule.length > 0 && props.schedule[props.schedule.length-1]) ?
                            props.schedule[props.schedule.length-1] : null;
    const beginLocation = beginId ? props.allPlaces.find(element => element.id === beginId).geometry.location : backupOrigin;
    const endLocation = endId ? props.allPlaces.find(element => element.id === endId).geometry.location : backupDestination;
    const wayPoints = [];
    if(props.schedule && props.allPlaces) {
      for (let i = 1; i < props.schedule.length-1; ++i) {
        const loc = props.allPlaces.find(element => element.id === props.schedule[i]).geometry;
        const locObject = {
          location: new google.maps.LatLng(loc.location.lat,  loc.location.lng)// location: new google.maps.LatLng(loc., loc.lng)
        }
        wayPoints.push(locObject);
      }  
    }
    directionsService.route(
      {
        origin: beginLocation,
        destination: endLocation,
        waypoints: wayPoints,
        travelMode: google.maps.TravelMode.DRIVING
      },
      (result, status) => {
        if (status === google.maps.DirectionsStatus.OK) {
        setState({
            directions: result
          });
        } else {
          console.error(`error fetching directions ${result}`);
        }
      }
    );
  })

    const GoogleMapExample = withGoogleMap((props) => (
      <GoogleMap
        defaultCenter={{ lat: 25.033964, lng: 121.564468 }}
        defaultZoom={12}
      >
        <DirectionsRenderer
          directions={state.directions}
          {...props}
        />
      </GoogleMap>
    ));

    return (
      <div>
        <GoogleMapExample
          containerElement={<div style={{ height: `500px`, width: "500px" }} />}
          mapElement={<div style={{ height: `100%` }} />}
          {...props}
        />
      </div>
    );

}

