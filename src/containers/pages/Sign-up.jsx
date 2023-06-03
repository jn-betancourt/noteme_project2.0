import SignUpForm from "components/login/sign-up";
import NavBar from "components/navegation/nav-bar";
import Layout from "hocs/Layout";

function SignUp(){
    return (
        <Layout>
            <NavBar/>
            <SignUpForm/>
        </Layout>
    )
}

export default SignUp;