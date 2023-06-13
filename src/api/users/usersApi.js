import axios from "axios"

const createUser = async (data)=>{
    return axios.post(
        "http://127.0.0.1:8000/api/users/signUp",
        data
    ).then(
        ( response ) =>{
            return response.data;
        }
    );
}

const getUser = async (data)=>{
    return axios.post(
        "http://127.0.0.1:8000/api/users/logIn",
        data
    ).then(
        ( response ) =>{
            return response.data;
        }
    );
}

export { createUser, getUser };