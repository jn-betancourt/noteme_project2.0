import { connect } from 'react-redux';
import note_me from 'assets/img/note_me.png';
import {NavLink, Link} from 'react-router-dom';

function NavBar(){
    const JSX = (
      <div id="side-bar" className="flex flex-col justify-center w-1/5 font-semibold bg-nav-color text-light text-lg">
        <div className="flex flex-col justify-center h-full">
          <div className="flex justify-center h-1/4">
            <div className="bg-light rounded-full px-5 mt-2">
              <Link to="/">
                <img className="py-2" alt="Logo" src={note_me} width={70} height={80}></img>
              </Link>
            </div>
          </div>
          <div className="flex justify-center h-full">
            <ul className="flex flex-col justify-center space-y-10">
              <li className="hover:bg-dark hover:rounded-full">
                <NavLink to='/'>Dashboard</NavLink>
              </li>
              <li className="hover:bg-dark hover:rounded-full">
                <NavLink to='/profile'>Profile</NavLink>
              </li>
              <li className="hover:bg-dark hover:rounded-full">
                <NavLink to='/connect'>Connect!</NavLink>
              </li>
              <li className="hover:bg-dark hover:rounded-full">
                <NavLink to='/settings'>settings</NavLink>
              </li>
            </ul>
          </div>
          <div class="flex flex-col justify-center h-1/4 border-t-2 border-grey">
            <div className="flex justify-evenly p-2">
              <Link to="/signin">Sign In!</Link>
              <Link to="/signup">Sign Up!</Link>
            </div>
          </div>
        </div>
      </div>
    );
    return JSX
}

const mapStateToProps = (state) =>({

})

export default connect(mapStateToProps,{

}) (NavBar);