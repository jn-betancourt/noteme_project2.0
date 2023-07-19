import axios from "axios";

const registerGoogleUser = async (data) => {
  const res = await axios.post(
    "http://localhost:8000/api/google/register",
    data
  );
  return res;
};

const loginGoogleUser = async (data) => {
  const res = await axios.post(
    "http://localhost:8000/api/google/login", 
    data
    );
  return res;
};

export { registerGoogleUser, loginGoogleUser };
