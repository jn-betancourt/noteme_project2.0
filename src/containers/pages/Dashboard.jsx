import NavBar from "components/navegation/nav-bar";
import NotesLayout from "components/notes/notes-layout";
import Layout from "hocs/Layout";

function Dashboard(){
    return (
        <Layout>
            <NavBar/>
            <NotesLayout/>
        </Layout>
    )
}

export default Dashboard;