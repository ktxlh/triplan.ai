import './App.css';
import React, { useState } from 'react';
import DatePicker from './Component/Date';
import City from './Component/City';
import Preferences from './Component/Preferences';
import { AttractionList, handlePlacesChange} from './Component/AttractionList';
import { Map } from './Component/Map';
import { Schedule, onDragEnd } from './Component/Schedule';
import callAPIs from './utils';
import { Button } from '@material-ui/core';
import withScriptjs from 'react-google-maps/lib/withScriptjs';

function App() {

  const [show, toggleShow] = useState(false);

  const [city, setCity] = useState("");
  const [departureDate, setDepartureDate] = useState(new Date());
  const [returnDate, setReturnDate] = useState(new Date());
  const [priceLevel, setPriceLevel] = useState(2);
  const [outDoor, setOutdoor] = useState(0.5);
  const [compactness, setCompactness] = useState(0.5);
  const [startTime, setStartTime] = useState("09:30");
  const [backTime, setBackTime] = useState("21:00");
  
  const [schedule, setSchedule] = useState([]);
  const [allPlaces, setAllPlaces] = useState([]);

  const onSearchClicked = () => {
    const embeddedSearchFields = {
      city: city,
      departureDate: departureDate,
      returnDate: returnDate,
      priceLevel: priceLevel,
      outDoor: outDoor,
      compactness: compactness,
      startTime: startTime,
      backTime: backTime,
      schedule: schedule,
    }
    callAPIs(embeddedSearchFields, setAllPlaces, setSchedule);
  }
  
  const handleDrag = (result) => {
      onDragEnd(schedule, setSchedule, result);
    }

  const handleTick = (event) => {
      handlePlacesChange(schedule, setSchedule, event);
  }

  const MapLoader = withScriptjs(Map);

  return (
    <div className="App">
      <div className="App-header">Travel Planner</div>
      <div className="input row">
        <City city={city} onChange={setCity}></City>
        <DatePicker 
          departureDate={departureDate}
          departureDateOnChange={setDepartureDate}
          returnDate={returnDate}
          returnDateOnChange={setReturnDate}
          ></DatePicker>
      </div>
      <div className = "input column">
        <Button variant="contained" onClick={onSearchClicked}>Search</Button>
      </div>
      <div className="input column">
        <button className="button" onClick={() => toggleShow(!show)}>
          {show? "collapse": "other preferences"}
        </button>
        {show && <Preferences
                    priceLevel={priceLevel} priceLevelOnChange={setPriceLevel}
                    outDoor={outDoor} outDoorOnChange={setOutdoor}
                    compactness={compactness} compactnessOnChange={setCompactness}
                    startTime={startTime} startTimeOnChange={setStartTime}
                    backTime={backTime} backTimeOnChange={setBackTime}
                    />}
      </div>
      <div className="output row">
        <AttractionList
          allPlaces={allPlaces}
          schedule={schedule}
          onChange={handleTick}
          />
          <Schedule
            schedule={schedule}
            allPlaces={allPlaces}
            onDragEnd={handleDrag}
          />
          <p>to use map, uncomment the lines below and put your api key inside</p>
          {/* <MapLoader
            googleMapURL="https://maps.googleapis.com/maps/api/js?key=YOUR-API-KEY-HERE"
            loadingElement={<div style={{ height: `100%` }} />}
            schedule={schedule}
            allPlaces={allPlaces}
          /> */}
      </div>
    </div>
  );
}

export default App;