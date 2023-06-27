import { configureStore, combineReducers } from '@reduxjs/toolkit';
import thunk from 'redux-thunk';
import storage from 'redux-persist/lib/storage';
import { persistReducer, persistStore, createTransform } from 'redux-persist';
import { encryptTransform } from 'redux-persist-transform-encrypt';

import noteReducer from './redux/features/tasks/taskSlice';
import userReducer from './redux/features/user/userSlice';

let secretKey = "123456789"
const transformFunctions = createTransform(
  (inboundState, key) => {
    return inboundState;
  },
  // transform state being rehydrated
  (outboundState, key) => {
    const isAuth = outboundState.is_auth;
    if (isAuth){
      secretKey = outboundState.token;
    }
    return outboundState;
  },
)
const persistConfig = {
    key: "root",
    storage,
    transforms: [
      transformFunctions,
      encryptTransform({
          secretKey: secretKey,
          onError: function (error) {
            console.error(error);
          },
        }),
      ],
};

const reducers = combineReducers({
    notes: noteReducer, 
    user: userReducer
});

const persistedReducer = persistReducer(persistConfig, reducers);

export const store = configureStore(
  {
    reducer: persistedReducer,
    middleware: [thunk]
  }
);

export const persistor = persistStore(store)