import './App.css';

import MaterialUIPickers from './Component/Date';
import SimpleSelect from './Component/City';
import Preferences from './Component/Preferences';

function App() {
  return (
    <div className="App">
      <SimpleSelect></SimpleSelect>
      <MaterialUIPickers></MaterialUIPickers>
      <Preferences></Preferences>
    </div>
  );
}

export default App;
