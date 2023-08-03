import axios from "axios";

const registerGoogle = async (data) => {
  const res = await axios.post(
    "http://localhost:8000/api/google/register", 
    data
    );
  return res;
};
const loginGoogle = async (data) => {
  const res = await axios.post(
    "http://localhost:8000/api/google/login", 
    data
    );
  return res;
};

export { loginGoogle, registerGoogle };
