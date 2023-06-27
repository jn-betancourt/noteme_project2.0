import axios from "axios"

const createUser = async (data)=>{
    return axios.post(
        "http://127.0.0.1:8000/api/users/signUp",
        data,
    );
}

const logIn = async (data)=>{
    return axios.post(
        "http://127.0.0.1:8000/api/users/logIn",
        data,
    );
}

const logOut = async (token)=>{
    return axios.get(
        "http://127.0.0.1:8000/api/users/logOut",
        {
            headers:{
                Authorization: "Token "+token
            },
        }
    );
}

export { createUser, logIn, logOut  };