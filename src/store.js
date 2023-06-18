import { configureStore } from '@reduxjs/toolkit';
// import thunk from 'redux-thunk';
// import rootReducer from './redux/reducers'
// import { composeWithDevTools } from 'redux-devtools-extension';

import noteReducer from './redux/features/tasks/taskSlice';
import userReducer from './redux/features/user/userSlice';

// const middleware = [thunk];

const store = configureStore(
        {
            reducer: {
                notes: noteReducer,
                user: userReducer
            },
        }
);

export default store;