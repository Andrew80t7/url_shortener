from fastapi import FastAPI

# Явно создаём экземпляр FastAPI
app = FastAPI(title="URL Shortener")

@app.get("/")
async def root():
    return {"message": "Hello World"}