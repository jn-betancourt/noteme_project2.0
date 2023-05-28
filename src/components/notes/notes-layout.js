import { connect } from 'react-redux';
import ModalNotes from 'components/notes/notes-modal';

function NotesLayout(){
    const JSX = (
        <div className="flex flex-col w-4/5 bg-dark text-light">
            <div className="h-10 ml-2 mt-2">
                <button className="hover:bg-nav-color hover:rounded-md">abrir/cerar</button>
            </div>
            <div className="flex h-full"><ModalNotes/></div>
            <div className="flex justify-end h-10 mr-2 mb-2">    
                <button id="agregar" onClick={()=>{document.querySelector("#dialog").show()}} className="hover:bg-nav-color hover:rounded-md">agregar nota</button>
            </div>
        </div>
    );
    return JSX
}

const mapStateToProps = (state) =>({

})

export default connect(mapStateToProps,{

}) (NotesLayout);