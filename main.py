import random
from fastapi import FastAPI # Importação do FastAPI para criar a aplicação web
from pydantic import BaseModel # Importação do BaseModel para criar modelos de dados
from fastapi.staticfiles import StaticFiles # Importação do StaticFiles para servir arquivos estáticos, como HTML, CSS e JavaScript

app = FastAPI() # Criação da instância do FastAPI para a aplicação web

# Montagem do diretório "assets" para servir arquivos estáticos, como HTML, CSS e JavaScript
app.mount("/", StaticFiles(directory="assets", html=True), name="assets")

# Modelo de dados para um estudante
class Estudante(BaseModel):
    nome: str
    curso: str
    ativo: bool


@app.get("/hello")
def read_root():
    return {"Hello": "World"}


@app.get("/random")
async def number_random():
    return {"random": True, "num_aleatorio": random.randint(1, 100)}

# Rota para criar um estudante
@app.post("/estudantes/cadastro")
async def create_estudante(estudante: Estudante):
    return estudante

# Rota para atualizar um estudante
@app.put("/estudantes/update/{id_estudante}")
async def update_item(id_estudante: int):
    return id_estudante > 0

# Rota para deletar um estudante
@app.delete("/estudantes/delete/{id_estudante}")
async def delete_estudante(id_estudante: int):
    return id_estudante > 0
