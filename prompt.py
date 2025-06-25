from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from pydantic import BaseModel, Field

TEMPLATE="""
Responde la pregunta {pregunta} en base a la información del
{texto}

El formato de salida debe ser el siguiente:{format_instructions}
"""
def get_prompt(template):

    class ContentGenScript(BaseModel):
        respuesta: str = Field(description="Respuesta")

    parser= JsonOutputParser(pydantic_object=ContentGenScript)

    prompt = PromptTemplate(
        input_variables=["texto","pregunta"],
        template=TEMPLATE,
        partial_variables={"format_instructions": parser.get_format_instructions()},
    )
    return prompt,parser

prompt,parser = get_prompt(TEMPLATE)