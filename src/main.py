from fastapi import FastAPI
from adapters.inbound.user_controller import router as user_router

app = FastAPI(
    title="Hexagonal Architecture API",
    description="API RESTful implementando Arquitectura Hexagonal",
    version="1.0.0"
)

app.include_router(user_router)

@app.get("/")
def root():
    return {"message": "API con Arquitectura Hexagonal funcionando"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)