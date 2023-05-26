from fastapi import FastAPI
from langchain.llms import OpenAI
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory

bot = ConversationChain(
    llm=OpenAI(temperature=0,openai_api_key="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"), 
    memory=ConversationBufferMemory(), 
    verbose=False
    )

app = FastAPI()

@app.get("/new_bot")
def new_bot()->None:
    global bot 
    bot = ConversationChain(
    llm=OpenAI(temperature=0,openai_api_key="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"), 
    memory=ConversationBufferMemory(), 
    verbose=False
    )
    
@app.post("/chat")
def read_root(message: dict):
    
    response = {
        "code: ": 200,
        "chat_ouput": "You don't have chat input!!!"
    }
    
    if "chat_input" in message.keys():
        response["chat_ouput"] = bot.predict(input=message['chat_input'])
    
    return response

@app.get("/")
def read_root():
    return {"Hello": "Khaa"}


#RUN APP
# uvicorn main:app --port 8000 --reload