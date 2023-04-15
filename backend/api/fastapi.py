from pydantic import BaseModel
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from lang_chain.lang_chain import Langchain

app = FastAPI()


origins = [
    "http://localhost",
    "http://localhost:8000",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Query(BaseModel):
    userInput: str
    prompt: str
    test: str 

    


@app.post("/message/{message_id}")
def create_query(message_id: int, message: Query):
    llm_response = Langchain(message.userInput).get_answer()
    return {"message-id": message_id, "response": llm_response, **message.dict()}