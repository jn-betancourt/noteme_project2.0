import axios from "axios"

const createUser = async (data)=>{
    return axios.post(
        "http://localhost:3000/api/users/signUp",
        data,
    );
}

const logIn = async (data)=>{
    return axios.post(
        "http://localhost:3000/api/users/logIn",
        data,
    );
}

export { createUser, logIn };