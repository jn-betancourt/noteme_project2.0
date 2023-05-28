import NavBar from "components/navegation/nav-bar";
import Layout from "hocs/Layout";

function Profile(){
    return (
        <Layout>
            <NavBar/>
            <div>profile</div>
        </Layout>
    )
}

export default Profile;