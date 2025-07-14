from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from pydantic import BaseModel, Field

#Definimos el prompt
TEMPLATE="""
Responde la pregunta {pregunta} en base a la información del
{texto}
Tu respuesta debe ser **únicamente** un objeto JSON válido.
Usa exactamente el siguiente formato de salida:

{format_instructions}

Asegúrate de que:
- El JSON sea sintácticamente correcto.
- Solo incluyas claves y valores indicados en el formato.
"""

#Definimos la función que devolverá el prompt y el parser
def get_prompt(template):

    class ContentGenScript(BaseModel):
        #Indicar al llm que debe devolver esta respuesta como JSON
        respuesta: str = Field(description="Respuesta")

    #Indicar al llm que la salida debe ser un JSON válido
    parser= JsonOutputParser(pydantic_object=ContentGenScript)

    #Crea el prompt en base al template
    prompt = PromptTemplate(
        input_variables=["texto","pregunta"],
        template=TEMPLATE,
        partial_variables={"format_instructions": parser.get_format_instructions()},
    )
    return prompt,parser

prompt,parser = get_prompt(TEMPLATE)