import { useDispatch, useSelector } from "react-redux";
import { Link } from 'react-router-dom';

import { delNote } from "../../redux/features/tasks/taskSlice";
import { delNoteApi } from "../../api/notes/notesApi";

function Notes() {

    const notes = useSelector( ( store ) => store.notes );
    const user = useSelector( ( store ) => store.user )
    const dispatch = useDispatch();

    const onDelete = (note_id)=>{
        dispatch(delNote(note_id));
        if (user.is_auth){
            delNoteApi(user.token, note_id)
        }
    }

    return (
        <>
        {
            notes.map( (element) => {
                const ElementNotes = (
                <div id={element.note_id} key={element.note_id} className="flex flex-col h-48 w-40 p-1 m-2 bg-red-400 rounded-md">
                    <div className="overflow-auto h-4/5">
                        <div className="flex flex-col">
                            <h3 className='text-2xl font-bold border-b-2'>{element.title}</h3>
                            <p>{element.description}</p>
                        </div>
                    </div>  
                    <div id="actions" className="flex justify-end h-5/4">
                        <button className="p-2" onClick={()=>onDelete(element.note_id)}>Delete</button>
                        <Link className="p-2" to={"edit/"+element.note_id}>Edit</Link>
                    </div>
                </div>
                )
                return ElementNotes
                }
            )
        }
        </>
    )

}

export default Notes;