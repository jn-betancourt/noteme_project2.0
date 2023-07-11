export default function GoogleButton(props) {
  const renderButton = () => {
    /*global google*/
    google.accounts.id.initialize({
      client_id:
        "387937601630-4qp9i2826864vtld90buqp34rv6k8bh7.apps.googleusercontent.com",
      callback: props.func,
    });

    setTimeout(() => {
      google.accounts.id.renderButton(
        document.getElementById("google-button"),
        { theme: "outline", size: "large", type: "icon" } // customization attributes
      );
      google.accounts.id.prompt(); // also display the One Tap dialog,
    }, 2000);
  };

  return <div id="google-button">{renderButton()}</div>;
}
