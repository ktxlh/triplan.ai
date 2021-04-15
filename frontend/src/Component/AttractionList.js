import React from 'react';
import { makeStyles } from '@material-ui/core/styles';
import FormLabel from '@material-ui/core/FormLabel';
import FormControl from '@material-ui/core/FormControl';
import FormGroup from '@material-ui/core/FormGroup';
import FormControlLabel from '@material-ui/core/FormControlLabel';
import Checkbox from '@material-ui/core/Checkbox';
//  This Page need to modify Form Control label
const useStyles = makeStyles((theme) => ({
  root: {
    display: 'flex',
  },
  formControl: {
    minWidth: 200,
    // margin: theme.spacing(3),
  },
}));

export const handlePlacesChange = (schedule, setSchedule, event) => {
  const id = event.target.name;
  const isAdd = event.target.checked;

  if (isAdd) {
    const newSchedule = Array.from(schedule);
    newSchedule.push(id);
    setSchedule(newSchedule);
  } else {
    const newSchedule = Array.from(schedule);
    var index = newSchedule.indexOf(id);
    if (index !== -1) {
      newSchedule.splice(index, 1);
    }
    setSchedule(newSchedule);
  }
};

export function AttractionList(props) {
  const classes = useStyles();

  return (
    <div className={classes.root}>
      <FormControl component="fieldset" className={classes.formControl}>
        <FormLabel component="legend">Attraction</FormLabel>
        <FormGroup>

          {props.allPlaces.map((item, index) => (
            <FormControlLabel
              control={<Checkbox checked={props.schedule.includes(item.id)} onChange={props.onChange} name={item.id} />}
              label={item.name.substr(0, 10)}
            />
            ))}
        </FormGroup>
      </FormControl>
    </div>
  );
}
