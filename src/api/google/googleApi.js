import axios from "axios";

const loginGoogleUser = async (data) => {
  const res = await axios.post(
    "http://localhost:8000/api/google/login", 
    data
    );
  return res;
};

export { loginGoogleUser };
