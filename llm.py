from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain_groq import ChatGroq
from prompt import prompt,parser

#Modelo de lenguaje llm
llm = ChatGroq(
    temperature=0,
    model_name="llama-3.3-70b-versatile",
    groq_api_key="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"
)

#Definimos la función que devuelve al respuesta
def get_response(retrieved_documents,question):
    
    #Objeto que concatena todo el texto y permite ejecutar en base al prompt el llm
    chain = LLMChain(llm=llm, prompt=prompt, output_parser=parser) 

    texto = str(retrieved_documents)

    pregunta = question

    result = chain.invoke({"texto": texto, "pregunta":pregunta})

    return result['text']