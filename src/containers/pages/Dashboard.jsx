import NavBar from "../../components/navegation/navBar";
import NotesLayout from "../../components/notes/notesLayout";
import Layout from "../../hocs/Layout";

function Dashboard(){
    return (
        <Layout>
            <NavBar/>
            <NotesLayout/>
        </Layout>
    )
}

export default Dashboard;