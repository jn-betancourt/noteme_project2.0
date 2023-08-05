import axios from "axios";

const getNotes = async (TOKEN) => {
  return axios.get("http://localhost:8000/api/notes/getNotes", {
    headers: {
      Authorization: `Token ${TOKEN}`,
    },
  }); 
};

const saveNoteApi = (TOKEN, data) => {
  return axios.post("http://localhost:8000/api/notes/modNotes", data, {
    headers: {
      Authorization: `Token ${TOKEN}`,
    },
  });
};

const changeNoteApi = (TOKEN, data) => {
  return axios.put("http://localhost:8000/api/notes/modNotes", data, {
    headers: {
      Authorization: `Token ${TOKEN}`,
    },
  });
};

const delNoteApi = (TOKEN, data) => {
  return axios.delete("http://localhost:8000/api/notes/modNotes", {
    data: { note_id: data },
    headers: {
      Authorization: `Token ${TOKEN}`,
    },
  });
};

export { getNotes, saveNoteApi, changeNoteApi, delNoteApi };
