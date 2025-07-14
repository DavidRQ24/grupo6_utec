from langchain_community.document_loaders import PyPDFLoader  #Desde la libreria langchain_community voy a importar,  la clase PyPDFLoader
import asyncio

def load_documents(file_path):
    
    loader = PyPDFLoader(file_path)  #Se pasa la ruta del archivo el pdf
    pages = []     #Se crea una lista vacia llamada pages

    #Función async para agregar las paginas con async
    async def process():
        async for page in loader.alazy_load():
            pages.append(page)   #Se agrega cada pagina , a la lista pages

    #Corre el proceso
    asyncio.run(process())

    return pages