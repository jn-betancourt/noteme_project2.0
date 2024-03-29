import ProfileData from "./profileData";
import ProfileDescription from "./profileDescription";


export function Profile(){

    return (
        <div class="flex justify-center flex-wrap p-16 w-5/6 h-full overflow-auto bg-dark">
            <div class="p-8 bg-white shadow mt-24">
            <div class="grid grid-cols-1 md:grid-cols-3">
                <div class="grid grid-cols-3 text-center order-last md:order-first mt-20 md:mt-0">
                <div>
                    <p class="font-bold text-gray-700 text-xl">22</p>
                    <p class="text-gray-400">Friends</p>
                </div>
                <div>
                    <p class="font-bold text-gray-700 text-xl">89</p>
                    <p class="text-gray-400">Comments</p>
                </div>
                </div>
                <div class="relative">
                <div class="w-48 h-48 bg-indigo-100 mx-auto rounded-full shadow-2xl absolute inset-x-0 top-0 -mt-24 flex items-center justify-center text-indigo-500">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-24 w-24" viewBox="0 0 20 20" fill="currentColor">
            <path fill-rule="evenodd" d="M10 9a3 3 0 100-6 3 3 0 000 6zm-7 9a7 7 0 1114 0H3z" clip-rule="evenodd" />
            </svg>
                </div>
                </div>

            <div class="space-x-8 flex justify-between mt-32 md:mt-0 md:justify-center">
            <button
            class="text-white py-2 px-4 uppercase rounded bg-blue-400 hover:bg-blue-500 shadow hover:shadow-lg font-medium transition transform hover:-translate-y-0.5"
            >
            Connect
            </button>
            <button
            class="text-white py-2 px-4 uppercase rounded bg-gray-700 hover:bg-gray-800 shadow hover:shadow-lg font-medium transition transform hover:-translate-y-0.5"
            >
            Message
            </button>
            </div>
            </div>
                <ProfileData/>
                <ProfileDescription/>
            </div>
        </div>
    )
}