from fastapi import FastAPI, HTTPException, status, Response, Depends
from models import Curso
from time import sleep



app = FastAPI()

cursos = {
    1: {
        'titulo': 'Programação para Leigos',
        'aulas': 112,
        'horas': 58

    }
}

def fake_db():
    try:
        print("Abrindo conexão com o banco de dados")
        sleep(1)
    finally:
        print("Fechando conexão com o banco de dados")
        sleep(1)


@app.get('/cursos')

# db: any = Depends(fake_db)   é uma injeção de depedência
# Uma função que exerce alguma coisa, que é necessária para o funcionamento de determinado bloco de código
# Exemplo: Uma consulta num banco de dados, depende de uma função que abra uma conexão com o banco 
#           pra só depois, realizar a consulta.

async def getCursos(db: any = Depends(fake_db)):
    return cursos


@app.get('/cursos/{id}')
async def getCursosById(id: int):
    try:
        curso = cursos[id]
        return curso   
    except KeyError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Curso de id {id} não encontrado')



@app.post('/cursos')
async def cadCursos(curso: Curso):
    next_id: int = len(cursos) + 1
    cursos[next_id] = curso
    return curso


@app.delete('/cursos/{id}')
async def deleteCurso(id: int):
    if id in cursos:
        del cursos[id]
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    else:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail='Inexistente')




@app.put('/cursos/{id}')
async def putCurso(id: int, curso: Curso):
    if id in cursos:
        cursos[id] = curso
        curso.id = id
        
        return curso
    else:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail='Inexistente')




if __name__ == "__main__":
    import uvicorn
    uvicorn.run('main:app', host='0.0.0.0', reload=True, port=8000, log_level='info')