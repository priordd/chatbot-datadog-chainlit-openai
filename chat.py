import os
from openai import AsyncOpenAI
import chainlit as cl

client = AsyncOpenAI()
# Instrument the OpenAI client
cl.instrument_openai()

settings = {
    "model": "gpt-4o",
    "temperature": 1,
    # ... more settings
}


from dotenv import load_dotenv

load_dotenv()

from ddtrace.llmobs import LLMObs
from ddtrace.llmobs.decorators import embedding, llm, retrieval, workflow

LLMObs.enable(
    api_key=os.getenv("DD_API_KEY"),
    site=os.getenv("DD_SITE"),
    ml_app=os.getenv("DD_LLMOBS_ML_APP"),
    agentless_enabled=os.getenv("DD_LLMOBS_AGENTLESS_ENABLED"),
    env="dev",
    service="llmmode",
)


@workflow
@cl.step(type="tool")
async def tool():
    # Fake tool
    # await cl.sleep(2)
    return "Response from the tool!"


@llm(model_name=settings["model"], model_provider="openai")
@cl.on_message
async def on_message(message: cl.Message):
    response = await client.chat.completions.create(
        messages=[
            {
                "content": "You are a helpful bot",
                "role": "system",
            },
            {"content": message.content, "role": "user"},
        ],
        **settings
    )
    await cl.Message(content=response.choices[0].message.content).send()
