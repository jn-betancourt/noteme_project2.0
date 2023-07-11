import { useSelector } from "react-redux"

export default function ProfileData(){
    const user = useSelector( (store)=>store.user );

    return (
        <div class="mt-20 text-center border-b pb-12">
                <h1 class="text-4xl font-medium text-gray-700">{user.username}</h1>
                <p class="font-light text-gray-600 mt-3">Bucharest, Romania</p>

                <p class="mt-8 text-gray-500">Solution Manager - Creative Tim Officer</p>
                <p class="mt-2 text-gray-500">University of Computer Science</p>
        </div>
    )  
}