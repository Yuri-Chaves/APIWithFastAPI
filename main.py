from fastapi import FastAPI
from typing import Union
from pydantic import BaseModel

livros = [
    {
        'id': 1,
        'título': 'O pequeno príncipe',
        'autor': 'Antoine de Saint-Exupéry'
    },
    {
        'id': 2,
        'título': 'Arsène Lupin contra Herlock Sholmes',
        'autor': 'Maurice Leblanc'
    },
    {
        'id': 3,
        'título': 'Arsène Lupin o ladrão de casaca',
        'autor': 'Maurice Leblanc'
    },
]

app = FastAPI()

class Item(BaseModel):
    id: int
    título: str
    autor: str

# Consultar (todos)
@app.get('/')
def mostrar():
    return livros
# Consultar(por id)
@app.get('/{id}')
def mostrar_por_id(id: int):
    for livro in livros:
        if livro.get('id') == id:
            return livro
# Editar
@app.put('/{id}')
async def editar_por_id(id: int, item: Item):
    for indice, livro in enumerate(livros):
        if livro.get('id') == id:
            livros[indice].update(item)
    return livros
# Criar
@app.post('/')
async def criar(item: Item):
    livros.append(item)
    return livros
@app.delete('/{id}')
async def remover(id: int):
    for indice, livro in enumerate(livros):
        if livro.get('id') == id:
            del livros[indice]
    return livros