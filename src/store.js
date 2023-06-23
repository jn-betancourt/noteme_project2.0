import { configureStore, combineReducers } from '@reduxjs/toolkit';
import thunk from 'redux-thunk';
import storage from 'redux-persist/lib/storage';
import { persistReducer, persistStore } from 'redux-persist';

import noteReducer from './redux/features/tasks/taskSlice';
import userReducer from './redux/features/user/userSlice';


const persistConfig = {
    key: "root",
    storage
};

const reducers = combineReducers({
    notes: noteReducer, 
    user: userReducer
})

const persistedReducer = persistReducer(persistConfig, reducers);

export const store = configureStore(
        {
            reducer: persistedReducer,
            middleware: [thunk]
        }
);

export const persistor = persistStore(store)