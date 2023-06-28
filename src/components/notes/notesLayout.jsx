import { Link, Outlet } from 'react-router-dom';
import Notes  from './notes';

function NotesLayout(){

    const JSX = (
        <div className="flex flex-col w-5/6 bg-dark text-light">
            <div className="h-10 ml-2 mt-2">
                <button className="hover:bg-nav-color hover:rounded-md">abrir/cerar</button>
            </div>
            <div className="flex flex-wrap overflow-auto h-full">
                <Outlet id="noteForm"/>
                <Notes/>
            </div>
            <div className="flex justify-end h-10 mr-2 mb-2">    
                <Link id="add" to="addNote" className="hover:bg-nav-color hover:rounded-md">agregar nota</Link>
            </div>
        </div>
    );
    return JSX
}

export default NotesLayout