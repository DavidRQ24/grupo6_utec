from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain_groq import ChatGroq
from prompt import prompt,parser

llm = ChatGroq(
    temperature=0,
    model_name="llama3-8b-8192",
    groq_api_key="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"
)

def get_response(retrieved_documents,question):
    
    chain = LLMChain(llm=llm, prompt=prompt, output_parser=parser) #objeto que concatena todo y permite ejecutar

    texto = str(retrieved_documents)

    pregunta = question

    result = chain.invoke({"texto": texto, "pregunta":pregunta})

    return result['text']