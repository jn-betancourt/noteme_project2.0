import './styles/App.css';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import store from './store';

import Error from 'containers/errors/error';

import Dashboard from 'containers/pages/Dashboard'
import Profile from 'containers/pages/Profile'

import { Provider } from 'react-redux'

function App() {
  return (
    <>
      <Provider store={store}>
        <Router>
          <Routes>
            {/* Ruta errror */}
            <Route path="*" element={<Error/>} />
            {/* Ruta home */}
            <Route path="/" element={<Dashboard/>} />
            <Route path="/profile" element={<Profile/>} />
          </Routes>
        </Router>
      </Provider>
    </>
  );
}

export default App;