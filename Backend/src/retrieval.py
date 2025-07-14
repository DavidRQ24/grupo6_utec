from langchain_ollama import OllamaEmbeddings
from langchain_core.vectorstores import InMemoryVectorStore

#Definimos la funcion que devuelve la información relevante
def get_documents(question,pages):

    #Modelo de representación vectorial
    embeddings = OllamaEmbeddings(
        model="llama3",
    )
    
    #Lista de paginas obtenidas
    pages_new = [page.page_content for page in pages]#[0]
    vectorstore = InMemoryVectorStore.from_texts(
        pages_new,
        embedding=embeddings,
    )

    retriever = vectorstore.as_retriever()

    retrieved_documents = retriever.invoke(question)

    return retrieved_documents