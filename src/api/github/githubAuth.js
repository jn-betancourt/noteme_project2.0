import axios from "axios";

const loginGithub = async (user_code) => {
  return await axios.post("http://localhost:8000/api/github/register",
  {data: {
      client_id: "59a1ea9bfa36b5b2fa70",
      client_secrets: "ff780e844f22ef184fdf65312e56b77ed05fe7c0",
      code: user_code,
    }}
  );
};

export { loginGithub };
