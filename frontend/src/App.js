import './App.css';

import MaterialUIPickers from './Component/Date';
import SimpleSelect from './Component/City';
import Preferences from './Component/Preferences';

function App() {
  return (
    <div className="App">
      <div className="App-header">Travel Planner</div>
      <div className="input main">
        <SimpleSelect></SimpleSelect>
        <MaterialUIPickers></MaterialUIPickers>
      </div>
      <div className="input pref">
        <p>other preferences</p>
        <Preferences></Preferences>
      </div>
    </div>
  );
}

export default App;
