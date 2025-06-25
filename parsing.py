from langchain_community.document_loaders import PyPDFLoader  # desde la libreria langchain_community voy a importar,  la clase PyPDFLoader   # una clase es un objeto que tiene atributos y metodos
import asyncio

def load_documents(file_path):
    
    loader = PyPDFLoader(file_path)  # se pasa la ruta del archivo el pdf, en este la ruta de arriba
    pages = []     # se crea una lista vacia llamada pages

    async def process():
        async for page in loader.alazy_load():
            pages.append(page)   # se agrega cada pagina , a la lista pages

    asyncio.run(process())

    return pages
