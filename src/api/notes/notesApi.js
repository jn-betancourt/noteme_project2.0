import axios from "axios";


const getNotes = async (TOKEN, id)=>{
    return axios.get(
        "http://127.0.0.1:8000/api/notes/getNotes",
        {
            headers: {
                Authorization: `Token ${TOKEN}`,
                id: `${id}`,
            }
        },
        
    )
}

const saveNoteApi = (TOKEN, data)=>{
    return axios.post(
        "http://127.0.0.1:8000/api/notes/modNote",
        data,
        {
            headers: {
                Authorization: `Token ${TOKEN}`,
                action: "POST",
            }
        },
        
    )
}

const changeNoteApi = (TOKEN, data)=>{
    return axios.post(
        "http://127.0.0.1:8000/api/notes/modNote",
        data,
        {
            headers: {
                Authorization: `Token ${TOKEN}`,
                action: "PUT",
            }
        },
        
    )
}

const delNoteApi = (TOKEN, data)=>{
    return axios.post(
        "http://127.0.0.1:8000/api/notes/modNote",
        {note_id: data},
        {
            headers: {
                Authorization: `Token ${TOKEN}`,
                action: "DELETE",
            }
        },
        
    )
}

export {getNotes, saveNoteApi, changeNoteApi, delNoteApi};