from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def root():
    return {"message": "Hello"}

#query param
@app.get('/dobro')
async def quad(num: int):
    text = f'o dobro de {num} é {num**2}'
    return {"msg": text}

