from fastapi import FastAPI
from app.routers import support_price, support_purpose, support_category,relationships
from .database import init_db

init_db()

app = FastAPI()

app.include_router(support_price.router)
app.include_router(support_purpose.router)
app.include_router(support_category.router)
app.include_router(relationships.router)

@app.get("/")
def root():
    return {"message": "Support System API"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="127.0.0.1", port=8000, reload=True)