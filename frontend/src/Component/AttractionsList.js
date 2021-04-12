import React from 'react';
import { makeStyles } from '@material-ui/core/styles';
import List from '@material-ui/core/List';
import ListItem from '@material-ui/core/ListItem';
import ListItemIcon from '@material-ui/core/ListItemIcon';
import ListItemSecondaryAction from '@material-ui/core/ListItemSecondaryAction';
import ListItemText from '@material-ui/core/ListItemText';
import Checkbox from '@material-ui/core/Checkbox';
import IconButton from '@material-ui/core/IconButton';
import CommentIcon from '@material-ui/icons/Comment';

const useStyles = makeStyles({
  root: {
    width: 300,
  },
});

function valuetext(value) {
  return `${value}°C`;
}

export default function AttractionList() {
  const classes = useStyles();

  const [outdoor, setOutdoor] = React.useState(0.5);
  const [compactness, setCompactness] = React.useState(0.5);

  const handleOutdoorChange = (event, newValue) => {
    setOutdoor(newValue);
  };
  
  const handleCompactnessChange = (event, newValue) => {
    setCompactness(newValue);
  };
  
  return (
    <div className={classes.root}>
      <Typography id="budget-typo" gutterBottom>
        Budget
      </Typography>
      <Slider
        defaultValue={2}
        getAriaValueText={valuetext}
        aria-labelledby="budget-slider"
        valueLabelDisplay="auto"
        step={1}
        marks
        min={1}
        max={3}
      />
      <Typography id="outdoor-typo" gutterBottom>
        Prefer Indoor Outdoor
      </Typography>
      <Slider 
        value={outdoor} 
        onChange={handleOutdoorChange} 
        aria-labelledby="continuous-slider" 
        step= {0.01}
        min = {0}
        max = {1}
      />
      <Typography id="compact-typo" gutterBottom>
        Compactness
      </Typography>
      <Slider 
        value={compactness} 
        onChange={handleCompactnessChange} 
        aria-labelledby="continuous-slider" 
        step= {0.01}
        min = {0}
        max = {1}
      />
      <Typography id="compact-typo" gutterBottom>
        Compactness
      </Typography>
      <Slider 
        value={compactness} 
        onChange={handleCompactnessChange} 
        aria-labelledby="continuous-slider" 
        step= {0.01}
        min = {0}
        max = {1}
      />
      <form className={classes.container} noValidate>
        <TextField
          id="departHrMin"
          label="Depart Time"
          type="time"
          defaultValue="07:30"
          className={classes.textField}
          InputLabelProps={{
            shrink: true,
          }}
          inputProps={{
            step: 300, // 5 min
          }}
        />
        <br></br>
        <TextField
          id="backHrMin"
          label="Back Time"
          type="time"
          defaultValue="18:30"
          className={classes.textField}
          InputLabelProps={{
            shrink: true,
          }}
          inputProps={{
            step: 300, // 5 min
          }}
        />
      </form>
    </div>
  );
}





