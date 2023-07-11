import NavBar from "../../components/navegation/navBar";
import Layout from "../../hocs/Layout";
import {Profile as ProfileComponent} from "../../components/profile/profile";

function Profile(){
    return (
        <Layout>
            <NavBar/>
            <ProfileComponent/>
        </Layout>
    )
}

export default Profile;