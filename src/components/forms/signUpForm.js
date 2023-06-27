import { useState } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import { createUser } from 'api/users/usersApi';
import { useDispatch } from 'react-redux';
import { logIn } from 'redux/features/user/userSlice';

export default function SignUpForm(){

    const navigate = useNavigate();
    const dispatch = useDispatch();
    const [form, setForm] = useState(
        {
            username: "",
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
        console.log(form);
        await createUser(form)
        .then(
            async (response)=>{
                const data = response.data
                dispatch(
                    logIn({...data})
                );
                navigate("/");
                window.location.reload(true);
            }
        );
    }

    return (
        <section className="w-5/6 h-fit bg-gray-50 dark:bg-gray-900">
            <div className="flex flex-col items-center justify-center px-6 py-8 mx-auto md:h-screen lg:py-0">
                <div className="w-full bg-white rounded-lg shadow dark:border md:mt-0 sm:max-w-md xl:p-0 dark:bg-gray-800 dark:border-gray-700">
                    <div className="px-5 py-2">
                        <h1 className="text-xl font-bold leading-tight tracking-tight text-gray-900 md:text-2xl dark:text-white">
                            Create and account
                        </h1>
                        <form className="md:space-y-6" action="#" method="POST">
                            <div>
                                <label for="username" className="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Your Name</label>
                                <input onChange={onChange} type="text" name="name" id="username" className="bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="Jhon" required=""/>
                            </div>
                            <div>
                                <label for="email" className="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Your email</label>
                                <input onChange={onChange} type="email" name="email" id="email" className="bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" placeholder="name@company.com" required=""/>
                            </div>
                            <div>
                                <label for="password" className="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Password</label>
                                <input onChange={onChange} type="password" name="password" id="password" placeholder="••••••••" className="bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" required=""/>
                            </div>
                            <div>
                                <label for="confirm-password" className="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Confirm password</label>
                                <input type="confirm-password" name="confirm-password" id="confirm-password" placeholder="••••••••" className="bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" required=""/>
                            </div>
                            <button type="submit" onClick={handleSubmit} className="w-full text-white bg-primary-600 hover:bg-primary-700 focus:ring-4 focus:outline-none focus:ring-primary-300 font-medium rounded-lg text-sm px-5 py-2.5 text-center dark:bg-primary-600 dark:hover:bg-primary-700 dark:focus:ring-primary-800">Create an account</button>
                            <p className="text-sm font-light text-gray-500 dark:text-gray-400">
                                Already have an account? <Link to="/signin" className="font-medium text-primary-600 hover:underline dark:text-primary-500">Login here</Link>
                            </p>
                        </form>
                    </div>
                </div>
            </div>
        </section>
    )
}
