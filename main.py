from parsing import load_documents 
from retrieval import get_documents
from prompt import get_prompt
from llm import llm
from llm import get_response

#Archivo cargado
file_path=r'C:\Users\dgrom\OneDrive\Documentos\TG Python UTEC\Manual.pdf'

documents = load_documents(file_path)

#Pregunta
question = "what happends if water gets inside the connector?"

#Retrieval
retrieved_documents = get_documents(question,documents)

#Response
respuesta = get_response(retrieved_documents,question)

print(respuesta)
