import {createSlice} from "@reduxjs/toolkit"


export const notesSlice = createSlice(
    {
        name: 'notes',
        initialState: [], 
        reducers: {
            addNote: (state, action) =>{
                state.push(action.payload);
            },
            delNote: (state, action)=>{
                const foundTask = state.find((task) => task.note_id === action.payload);
                if (foundTask) {
                  state.splice(state.indexOf(foundTask), 1);
                }
            },
            changeNote: (state, action)=>{
                const foundTask = state.find((task) => task.note_id === action.payload.note_id);
                if (foundTask) {
                    const index = state.indexOf(foundTask);
                    const newNote = {
                        note_id: foundTask.note_id,
                        title: action.payload.title, 
                        description: action.payload.description
                    }
                    state.splice(index, 1, newNote);
                }
            },
            updateState: (state, action)=>{
                action.payload.forEach(
                    element =>{
                        state.push(element);
                    }
                );
            },
        }
    }
)


export const {addNote, delNote, changeNote, updateState} = notesSlice.actions
export default notesSlice.reducer