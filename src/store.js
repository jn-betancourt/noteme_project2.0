import { configureStore } from '@reduxjs/toolkit';
// import thunk from 'redux-thunk';
// import rootReducer from './redux/reducers'
// import { composeWithDevTools } from 'redux-devtools-extension';

import noteReducer from './redux/features/tasks/taskSlice';

// const middleware = [thunk];

const store = configureStore(
        {
            reducer: {
                notes: noteReducer
            },
        }
);

export default store;