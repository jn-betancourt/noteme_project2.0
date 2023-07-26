import { Link, useSearchParams } from "react-router-dom";
import { loginGithub } from "../../api/github/githubAuth";
import { useEffect } from "react";

export default function GithubButton() {
  const [searchParams, setSearchParams] = useSearchParams();
  console.log(searchParams);
  useEffect(() => {
    if (searchParams.get("code")) {
      handleSubmit(searchParams.get("code"));
    }
  }, [searchParams]);

  const handleSubmit = async (user_code)=>{
    await loginGithub(user_code).then(
      (res)=>console.log(res)
    )
  }

  return (
    <Link to="https://github.com/login/oauth/authorize?client_id=59a1ea9bfa36b5b2fa70">
      Github
    </Link>
  );
}
