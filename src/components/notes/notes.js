import { useSelector, useDispatch } from "react-redux";
import { delNote } from "redux/features/tasks/taskSlice";
import { Link } from 'react-router-dom';

function Notes() {

    const notes = useSelector((store) => store.notes);
    const dispatch = useDispatch();

    const onDelete = (id)=>{
        dispatch( 
            delNote(id)
        )
    }   

    return (
        <>
        {
            notes.map( (element) => {
                const ElementNotes = (
                <div id={element.id} className="flex flex-col h-48 w-40 p-1 m-2 bg-red-400 rounded-md">
                    <div className="overflow-auto h-4/5">
                        <div className="flex flex-col">
                            <h3 className='text-2xl font-bold border-b-2'>{element.title}</h3>
                            <p>{element.description}</p>
                        </div>
                    </div>  
                    <div id="actions" className="flex justify-end h-5/4">
                        <button className="p-2" onClick={()=>{onDelete(element.id)}}>Delete</button>
                        <Link className="p-2" to={"edit/"+element.id}>Edit</Link>
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