import axios from 'axios';
function convertDateToAPIDate(date) {
    const yyyy = date.getYear();
    const mm = date.getMonth() + 1; // getMonth() is zero-based
    const dd = date.getDate();
    return [ yyyy,
            (mm>9 ? '' : '0') + mm,
            (dd>9 ? '' : '0') + dd
            ].join('-');
}

export default function callAPIs(embeddedSearchFields, setAllPlaces, setSchedule){
    const departureDate = convertDateToAPIDate(embeddedSearchFields.departureDate);
    const returnDate = convertDateToAPIDate(embeddedSearchFields.returnDate);
    const city = embeddedSearchFields.city;
    const priceLevel = embeddedSearchFields.priceLevel;
    const outDoor = embeddedSearchFields.outDoor;
    const compactness = embeddedSearchFields.compactness;
    const startTime = embeddedSearchFields.startTime;
    const endTime = embeddedSearchFields.endTime;
    const placesSearchParams = new URLSearchParams();
    embeddedSearchFields.schedule.forEach((id)=>{
        placesSearchParams.append("place_ids", id);
    })
    const scheduleSearchParams = new URLSearchParams();
    embeddedSearchFields.schedule.forEach((id)=>{
        scheduleSearchParams.append("schedule", id);
    })

    const requestObject = {
        departure_date: departureDate,
        return_date: returnDate,
        city: city,
        price_level: priceLevel,
        outdoor: outDoor,
        compactness: compactness,
        start_time: startTime,
        back_time: endTime,
        placesSearchParams: placesSearchParams,
        scheduleSearchParams: scheduleSearchParams,
    }
    axios.post('http://localhost:5000/plan', requestObject).then( (response) => {
        const newAllPlaces = [];
        response.data.places.forEach(element => {
            newAllPlaces.push(element);
        })
        setAllPlaces(newAllPlaces);
        const newSchedule = []
        response.data.schedule.forEach(element => {
            newSchedule.push(element);
        })
        setSchedule(newSchedule);
    }).catch( (error) =>  {
        console.log(error);
    }).then(()=>{});
}