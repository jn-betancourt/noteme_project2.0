import {createSlice} from "@reduxjs/toolkit"

const initialState = {
    username: null,
    id: null,
    token: null,
    is_auth: false
}

export const userSlice = createSlice(
    {
        name: 'user',
        initialState, 
        reducers: {
            logIn: (state, action)=>{
                state = {...state, ...action.payload, is_auth: true};
                return state
            },
            logOut: (state, action)=>{
                state = {...state, ...action.payload};
                return state
            }
        }
    }
)


export const {logIn, logOut} = userSlice.actions
export default userSlice.reducer