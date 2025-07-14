#### Grupo6_utec

Trabajo grupal grupo 6 2025 Python UTEC

Repositorio de archivos del trabajo final añadidos el 25.06.2025

Overview
Este proyecto consta de un chatbot mediante RAG, se encontra el detalle de los archivos desplegados a continuación:

#### Estructura de la carpeta
#
grupo6_utec/                                                                
│                                                              
├── Backend/                                                        
│   ├── Manual/                  # carpeta del archivo                                                                    
│        ├── Manual.pdf            # archivo pdf                                                                                
│   ├── prompts/                 # carpeta archivos del prompt                                                                            
│        ├── prompt.py            # archivo prompt                                                                              
│   ├── files/                     # Codigo del backend                                                          
│   │   ├── retrieval.py        # archivo del codigo del retrieval                                                                                            
│   │   ├── llm.py                # archivo del codigo del  llm                                                                                                                
│   │   ├── main.py               # archivo del codigo del main                                                                                                          
│   │   └── parsing.py             # archivo del parsing                                                                                                                        
│   └── requirements.txt          # requerimientos para el backend                                                                                                          
│                                                                                                                                                        
├── frontend/                                                                                                                                              
│   ├── files/                     # Frontend source code                                                                                                                        
│   │   ├── groq_chatbot.py     # archivo streamlit                                                                                                                                    
│   └── requirements frontend.txt          # requerimientos para el frontend                                                                                                        
├── README.md                    # Project documentation                                                                                                                                          
├── .env                    # archivo de entorno                                                                                                                                          
│                                                                                                                                                                                              

#### Estructura del proyecto

El proyecto contiene lo siguientes carpetas principales:

1. **Backend**: Contiene la información de la lógica del proyecto con los programas en .py.

2. **Frontend**: Contiene el archivo para la visualización de la interfaz streamlit en .py.

#### Backend Structure

- **Manual**: Contiene el manual del archivo pdf.
- **prompts/**: Contiene el archivo .py con el prompt template.
- **files/retrieval**: Contiene el archivo en .py del retrieval.
- **files/llm**: Contiene el archivo en .py del llm.
- **files/main**: Contiene el archivo en .py del main.
- **files/parsing**: Contiene el archivo en .py del parsing.
- **requirements.txt**: Se muestra los requerimientos para el backend.

#### Frontend Structure

- **files**: Contiene el archivo streeamlit que interactua con el backend.
- **requirements frontend.txt**: Se muestra los requerimientos para el frontend.

#### Ejecución del programa

### Pre - requisitos

`.env` archivo con las variables de entorno.

### Instalación

Descargas los archivos a una carpeta en entorno local

### Ejecución

Abrir la carpeta de archivos en el programa Vscode.
Ejecutar el archivo del streamlit en el terminal, con el comando "streamlit run groq_chatbot.py".


