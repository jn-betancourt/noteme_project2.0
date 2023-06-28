import { useDispatch,useSelector } from 'react-redux';
import { useNavigate, useParams } from 'react-router-dom';

import {useState, useEffect} from 'react';
import { v4 as uuid } from "uuid";

import { addNote, changeNote } from '../../redux/features/tasks/taskSlice';
import { saveNoteApi, changeNoteApi } from '../../api/notes/notesApi';

export default function NotesForm(){

    const notes = useSelector( (store) => store.notes);
    const user = useSelector( (store) => store.user);
    const dispatch = useDispatch();
    const params = useParams();
    const navigate = useNavigate();

    const [note, setNote] = useState(
        {
            note_id: uuid(),
            title: "",
            description: ""
        }
    );

    const handleChange = (e) => {
        setNote({
            ...note,
            [e.target.id]: e.target.value
        })
    }

    const onSubmit = () => {
        if (params.id){
            const newNote = {...note, note_id: params.id };
            console.log(newNote);
            dispatch(changeNote(newNote));
        }
        else{
            const note_info = {
                ...note,
              }
            dispatch(
                addNote(note_info)
            )
        }
        navigate("/")
    }

    const onCancel = (e)=>{
        e.preventDefault();
        navigate("/");
    }

    const onSubmitAuth = ()=>{
        onSubmit();
        if (params.id){
            console.log(params.id)
            modified(params.id);
        }
        else{
            save();
        }
    }
    
    const save = async ()=>{
        await saveNoteApi(
            user.token, 
            {
               ...note,
                id: user.id
            }
        )
    }
    const modified = async (note_id)=>{
        await changeNoteApi(
            user.token,
            {
                ...note,
                note_id: note_id
            }
        )
    }

    useEffect(()=>{
            if (params.id){
                setNote(notes.find((note) => note.note_id === params.id));
            }
        }, [params, notes]);

    return (
        <div className="absolute left-1/2 right-1/2 bg-white w-64 rounded-lg">
            <div className="space-y-2 text-black">
                <div className="flex flex-col p-2 space-y-2">
                    <label className="flex justify-center" htmlFor="title">Title</label>
                    <input value={note.title} onChange={handleChange} className=" focus:border-b-2 focus:border-red-400 focus:outline-0 hover:border-2 hover:rounded  hover:border-red-200" id="title"/>
                    <label className="flex justify-center" htmlFor="description">Description</label>
                    <textarea rows="2" value={note.description} onChange={handleChange} className="focus:border-b-2 focus:border-green-400 focus:outline-0 hover:border-2 hover:rounded  hover:border-green-200" id="description"/>
                </div>
                <div className="flex justify-between p-2">
                    <button className="hover:border-purple-500 hover:border-b-2" onClick={onCancel} id="close">Cancel</button>
                    <button 
                    className="hover:border-purple-500 hover:border-b-2" 
                    id="save" 
                    onClick={user.is_auth
                            ? onSubmitAuth
                            : onSubmit }>Save</button>
                </div>
            </div>
        </div>
    )
}