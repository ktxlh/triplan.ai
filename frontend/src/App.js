import './App.css';
import React, { useState } from 'react';
import MaterialUIPickers from './Component/Date';
import SimpleSelect from './Component/City';
import Preferences from './Component/Preferences';
import Attraction from './Component/PlanAttraction';

function App() {
  const [show, toggleShow] = useState(false);

  return (
    <div className="App">
      <div className="App-header">Travel Planner</div>
      <div className="input row">
        <SimpleSelect></SimpleSelect>
        <MaterialUIPickers></MaterialUIPickers>
      </div>
      <div className="input column">
        <button className="button" onClick={() => toggleShow(!show)}>
          {show? "collapse": "other preferences"}
        </button>
        {show && <Preferences></Preferences>}
      </div>
      <div className="output row">
        <Attraction></Attraction>
      </div>
    </div>
  );
}

export default App;
