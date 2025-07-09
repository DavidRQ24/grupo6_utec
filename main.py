from parsing import load_documents 
from retrieval import get_documents
from prompt import get_prompt
from llm import llm
from llm import get_response

#Definimos la función main
def pipeline(question):

    #Ruta del archivo
    file_path=r'C:\Users\dgrom\OneDrive\Documentos\TG_Python_UTEC\Manual.pdf'

    #Parsing
    documents = load_documents(file_path)

    #Retrieval
    retrieved_documents = get_documents(question,documents)
    
    #Response
    respuesta = get_response(retrieved_documents,question)

    return respuesta
