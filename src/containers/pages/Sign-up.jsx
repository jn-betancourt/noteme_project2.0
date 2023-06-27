import SignUpForm from "components/forms/signUpForm";
import NavBar from "components/navegation/navBar";
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