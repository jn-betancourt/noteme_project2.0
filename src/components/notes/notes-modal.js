export default function ModalNotes(){
    return (
        <dialog id="dialog" class="rounded-lg">
            <div className="space-y-2">    
                <div>
                    <form className="flex flex-col">
                        <label className="flex justify-center" for="titulo">Titulo</label>
                        <input className="focus:border-b-2 focus:border-red-400 focus:outline-0 hover:border-2 hover:rounded  hover:border-red-200" id="titulo"/>
                        <label className="flex justify-center" for="descripcion">Descripcion</label>
                        <input className="focus:border-b-2 focus:border-green-400 focus:outline-0 hover:border-2 hover:rounded  hover:border-green-200" id="descripcion"/>
                    </form>
                </div>
                <div className="flex justify-between">
                    <button className="hover:border-purple-500 hover:border-b-2" onClick={()=>{document.querySelector('#dialog').close()}} id="cerrar">Cancelar</button>
                    <button className="hover:border-purple-500 hover:border-b-2" id="cerrar">Guardar</button>
                </div>
            </div>
        </dialog>
    )
}