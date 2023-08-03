import jwtDecode from "jwt-decode";
import { useEffect } from "react";
import { useDispatch } from "react-redux";
import { useNavigate } from "react-router-dom";
import { logIn } from "../../redux/features/user/userSlice";

export default function GoogleButton(props) {
  const dispatch = useDispatch();
  const navigate = useNavigate();

  const googleSubmit = async (response) => {
    const info = jwtDecode(response.credential);
    console.log(info);
    await props.func(info).then(async (response) => {
      const data = response.data;
      dispatch(logIn({ ...data }));

      if (props.getNotes) {
        await props.getNotes(data.token);
        navigate("/");
        window.location.reload(true);
      };
      navigate("/");
      window.location.reload(true);
    });
  };

  useEffect(() => {
    /*global google*/
    google.accounts.id.initialize({
      client_id:
        "387937601630-4qp9i2826864vtld90buqp34rv6k8bh7.apps.googleusercontent.com",
      callback: googleSubmit,
    });
    setTimeout(() => {
      google.accounts.id.renderButton(
        document.getElementById("google-button"),
        { theme: "outline", size: "large", type: "button" } // customization attributes
      );
      google.accounts.id.prompt(); // also display the One Tap dialog,
    }, 1000);
  }, []);

  return <div id="google-button"></div>;
}
