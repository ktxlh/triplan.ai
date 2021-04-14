import React from "react";
import { DragDropContext, Droppable, Draggable } from "react-beautiful-dnd";

const grid = 8;

const getItemStyle = (isDragging, draggableStyle) => ({
  // some basic styles to make the items look a bit nicer
  userSelect: "none",
  padding: grid * 2,
  margin: `0 0 ${grid}px 0`,

  // change background colour if dragging
  background: isDragging ? "lightgreen" : "grey",

  // styles we need to apply on draggables
  ...draggableStyle
});

const getListStyle = isDraggingOver => ({
  background: isDraggingOver ? "lightblue" : "lightgrey",
  padding: grid,
  width: 250
});

const reorder = (list, startIndex, endIndex) => {
    const result = Array.from(list);
    const [removed] = result.splice(startIndex, 1);
    result.splice(endIndex, 0, removed);
  
    return result;
  };

export const onDragEnd = (schedule, setSchedule, result) => {
    if (!result.destination) return;
    const items = reorder(schedule, result.source.index, result.destination.index);
    setSchedule(items);
}

export const handlePlacesChange = (schedule, setSchedule, event) => {
    const id = event.target.key;
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

export function Schedule(props) {
    return (
        <DragDropContext onDragEnd={props.onDragEnd}>
        <Droppable droppableId="droppable">
            {(provided, snapshot) => (
            <div
                {...provided.droppableProps}
                ref={provided.innerRef}
                style={getListStyle(snapshot.isDraggingOver)}
            >
                {props.schedule.map((item, index) => (
                <Draggable key={item} draggableId={item} index={index}>
                    {(provided, snapshot) => (
                    <div
                        ref={provided.innerRef}
                        {...provided.draggableProps}
                        {...provided.dragHandleProps}
                        style={getItemStyle(
                        snapshot.isDragging,
                        provided.draggableProps.style
                        )}
                    >
                        {props.allPlaces.find(x => x.id === item) ?
                        props.allPlaces.find(x => x.id === item).name.substr(0, 10) : "loading"}
                    </div>
                    )}
                </Draggable>
                ))}
                {provided.placeholder}
            </div>
            )}
        </Droppable>
        </DragDropContext>
    );
}