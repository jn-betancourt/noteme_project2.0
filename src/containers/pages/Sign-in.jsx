import SignInForm from "components/login/sign-in";
import NavBar from "components/navegation/nav-bar";
import Layout from "hocs/Layout";

function SignIn(){
    return (
        <Layout>
            <NavBar/>
            <SignInForm/>
        </Layout>
    )
}

export default SignIn;