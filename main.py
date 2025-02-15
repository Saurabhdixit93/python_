from fastapi import FastAPI
from app.routes import router

app = FastAPI()

# Include API routes
app.include_router(router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Backend API"}
