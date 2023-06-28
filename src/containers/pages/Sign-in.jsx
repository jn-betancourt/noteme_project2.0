import LogInForm from "../../components/forms/logInForm";
import NavBar from "../../components/navegation/navBar";
import Layout from "../../hocs/Layout";

function SignIn(){
    return (
        <Layout>
            <NavBar/>
            <LogInForm/>
        </Layout>
    )
}

export default SignIn;