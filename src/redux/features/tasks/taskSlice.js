import {createSlice} from "@reduxjs/toolkit"


export const notesSlice = createSlice(
    {
        name: 'notes',
        initialState: [], 
        reducers: {
            addNote: (state, action) =>{
                state.push(action.payload);
            },
            delNote: (state, action) =>{
                const foundTask = state.find((task) => task.id === action.payload);
                if (foundTask) {
                  state.splice(state.indexOf(foundTask), 1);
                }
              },
            changeNote: (state, action)=>{
                const foundTask = state.find((task) => task.id === action.payload.id);
                if (foundTask) {
                    const index = state.indexOf(foundTask);
                    const newNote = {
                        id: foundTask.id, 
                        title: action.payload.title, 
                        description: action.payload.description
                        }
                    state.splice(index, 1, newNote);
                  }
            }
        }
    }
)


export const {addNote, delNote, changeNote} = notesSlice.actions
export default notesSlice.reducer