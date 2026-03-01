import asyncio
from langchain_groq import ChatGroq
from langchain_core.messages import SystemMessage, HumanMessage
from decouple import config

GROQ_API_KEY = config("GROQ_API_KEY")

llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0,
    api_key=GROQ_API_KEY,
)
print("LOADED KEY:", GROQ_API_KEY)

async def chat(prompt: str):
    messages = [
        SystemMessage(content="You are a personal assistant. Always provide short answers."),
        HumanMessage(content=prompt)
    ]

    async for chunk in llm.astream(messages):
        if chunk.content:
            print(chunk.content, end="", flush=True)
            await asyncio.sleep(0.02)

while True:
    print()
    prompt = input("User -> ")

    if prompt.lower() == "bye":
        break

    print()
    asyncio.run(chat(prompt))