import './styles/App.css';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';

import Error from './containers/errors/error';

import Dashboard from './containers/pages/Dashboard';
import NotesForm from './components/notes/NotesForm';

import Profile from './containers/pages/Profile';
import SignIn from './containers/pages/Sign-in';
import SignUp from './containers/pages/Sign-up';


function App() {

  return (
      <Router>
          <Routes>
            {/* Ruta errror */}
            <Route path="*" element={<Error/>} />
            {/* Ruta home */}
            <Route path="/" element={<Dashboard/>}>
              <Route path="addNote" element={<NotesForm/>} />
              <Route path="edit/:id" element={<NotesForm/>} />
            </Route>
            <Route path="/profile" element={<Profile/>} />
            <Route path="/signin" element={<SignIn/>} />
            <Route path="/signup" element={<SignUp/>} />
          </Routes>
      </Router>
  );
}

export default App;