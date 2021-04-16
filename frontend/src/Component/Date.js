import 'date-fns';
import React from 'react';
import Grid from '@material-ui/core/Grid';
import DateFnsUtils from '@date-io/date-fns';
import {
  MuiPickersUtilsProvider,
  KeyboardDatePicker,
} from '@material-ui/pickers';

export default function DatePicker(props) {
  
  const handleDepartureDateChange = (date) => {
    props.departureDateOnChange(date);
  };

  const handleReturnDateChange = (date) => {
    props.returnDateOnChange(date);
  };

  return (
    <MuiPickersUtilsProvider utils={DateFnsUtils}>
      <Grid container justify="space-evenly">
        <KeyboardDatePicker
          disableToolbar
          variant="inline"
          format="MM/dd/yyyy"
          margin="normal"
          id="Departure Date"
          label="Departure Date"
          value={props.departureDate}
          onChange={handleDepartureDateChange}
          KeyboardButtonProps={{
            'aria-label': 'change date',
          }}
        />
        <KeyboardDatePicker
          disableToolbar
          variant="inline"
          margin="normal"
          id="Return Date"
          label="Return Date"
          format="MM/dd/yyyy"
          value={props.returnDate}
          onChange={handleReturnDateChange}
          KeyboardButtonProps={{
            'aria-label': 'change date',
          }}
        />
      </Grid>
    </MuiPickersUtilsProvider>
  );
}
