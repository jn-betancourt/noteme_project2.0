import axios from "axios";

const registerGoogleUser = async (data) => {
  const res = await axios.post(
    "http://localhost:3000/api/google/googleRegister",
    data
  );
  return res;
};

export { registerGoogleUser };
