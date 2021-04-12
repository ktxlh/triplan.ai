import React, { Component } from 'react';
import { render } from 'react-dom';
import Map from './Map';

const googleMapsApiKey = "AIzaSyAg3YGGUH4iI4sAWhkcg1jyErmvyMgucSs";

const destinations = [
    {latitude: 25.8103146,longitude: -80.1751609},
    {latitude: 27.9947147,longitude: -82.5943645},
    {latitude: 28.4813018,longitude: -81.4387899}
  ]

const MapWithRoute = props => {
//   const {places} = props;
  const {places} = destinations;

  const {
    loadingElement,
    containerElement,
    mapElement,
    defaultCenter,
    defaultZoom
  } = props;

  return (
    <Map
      googleMapURL={
        'https://maps.googleapis.com/maps/api/js?key=' +
        googleMapsApiKey +
        '&libraries=geometry,drawing,places'
      }
      markers={places}
      loadingElement={loadingElement || <div style={{height: `100%`}}/>}
      containerElement={containerElement || <div style={{height: "80vh"}}/>}
      mapElement={mapElement || <div style={{height: `100%`}}/>}
      defaultCenter={defaultCenter || {lat: 25.798939, lng: -80.291409}}
      defaultZoom={defaultZoom || 11}
    />
  );
};

export default MapWithRoute;
