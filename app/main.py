from fastapi import FastAPI, Response

from app.api.router import router as v1

app = FastAPI()
app.include_router(v1, prefix='/api')


@app.get('/health')
def health():
    return Response(status_code=200)
