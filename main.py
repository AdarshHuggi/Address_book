from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from endpoints.api import router 
from database.db_connection import Base,engine
import uvicorn


Base.metadata.create_all(bind=engine)
app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
