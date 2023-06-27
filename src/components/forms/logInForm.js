import { logIn } from "api/users/usersApi";
import { getNotes } from "api/notes/notesApi";
import { useState } from "react";
import { useDispatch } from "react-redux";
import { useNavigate, Link  } from "react-router-dom";
import { logIn as saveUser } from "redux/features/user/userSlice";
import { updateState } from "redux/features/tasks/taskSlice";

export default function LogInForm(){
    
    const dispatch = useDispatch();
    const navigate = useNavigate();
    const [form, setForm] = useState(
        {
            email: "",
            password: ""
        }
    );

    const onChange = (e)=>{
        setForm(
            {
                ...form,
                [e.target.id]: e.target.value
            }
        )
    }

    const handleSubmit = async (e)=>{
        e.preventDefault();
        await logIn(form)
        .then(
            async (response)=>{
                const data = response.data
                dispatch(
                    saveUser({...data})
                );
                fetchNotes(data.token, data.id);
                navigate("/");
                window.location.reload(true);
            }
        )
        .catch(
            (response)=>console.warn(response)
        );
    }

    const fetchNotes = async (token, id)=>{
        await getNotes(token, id)
        .then(
            res=>{
                dispatch(
                    updateState(
                        res.data.response
                    )
                )
            }
        )
    }

    return (
        <section class="w-5/6 bg-gray-50 dark:bg-gray-900">
            <div class="flex flex-col items-center justify-center px-6 py-8 mx-auto md:h-screen lg:py-0">
                <div class="w-full bg-white rounded-lg shadow dark:border md:mt-0 sm:max-w-md xl:p-0 dark:bg-gray-800 dark:border-gray-700">
                    <div class="p-6 space-y-4 md:space-y-6 sm:p-8">
                        <h1 class="text-xl font-bold leading-tight tracking-tight text-gray-900 md:text-2xl dark:text-white">
                            Sign in to your account
                        </h1>
                        <form class="space-y-4 md:space-y-6" action="#">
                            <div>
                                <label for="email" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Your email</label>
                                <input onChange={onChange} type="email" name="email" id="email" class="bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="name@company.com" required=""/>
                            </div>
                            <div>
                                <label for="password" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Password</label>
                                <input onChange={onChange} type="password" name="password" id="password" placeholder="••••••••" class="bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" required=""/>
                            </div>
                            <button onClick={handleSubmit} type="submit" class="w-full text-white bg-primary-600 hover:bg-primary-700 focus:ring-4 focus:outline-none focus:ring-primary-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800">Sign in</button>
                            <p class="text-sm font-light text-gray-500 dark:text-gray-400">
                                Don't have an account yet? <Link to="/signup" class="font-medium text-primary-600 hover:underline dark:text-primary-500">Sign up</Link>
                            </p>
                        </form>
                    </div>
                </div>
            </div>
        </section>
    )    
}
