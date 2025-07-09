from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain_groq import ChatGroq
from prompt import prompt,parser

llm = ChatGroq(
    temperature=0,
    model_name="llama-3.3-70b-versatile",
    groq_api_key="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"
)

def get_response(retrieved_documents,question):
    
    chain = LLMChain(llm=llm, prompt=prompt, output_parser=parser) #Objeto que concatena todo y permite ejecutar

    texto = str(retrieved_documents)

    pregunta = question

    result = chain.invoke({"texto": texto, "pregunta":pregunta})

    return result['text']