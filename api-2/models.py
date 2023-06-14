from typing import Optional, Any, Dict, List

from pydantic import BaseModel, validator

cursos = {
    1: {
        'titulo': 'Programação para Leigos',
        'aulas': 112,
        'horas': 58

    }
}

class Curso(BaseModel):
    id: Optional[int] = None
    titulo: str
    aulas: int
    horas: int


    @validator('titulo')
    def caracter_não_permitido(cls, value):
        if "'" in value:
            raise ValueError('Título não permitido')
        return value

cursos = [
    Curso(id=1, titulo='Programação para Leigos', aulas=50, horas=120),
    Curso(id=1, titulo='Algoritmos', aulas=40, horas=80),
    Curso(id=1, titulo='Lógica', aulas=25, horas=60)
]


