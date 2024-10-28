import os
import chainlit as cl
from ddtrace.llmobs.decorators import llm, workflow


from dotenv import load_dotenv

load_dotenv()

from ddtrace.llmobs import LLMObs

LLMObs.enable(
    api_key=os.getenv("DD_API_KEY"),
    site=os.getenv("DD_SITE"),
    ml_app=os.getenv("DD_LLMOBS_ML_APP"),
    agentless_enabled=os.getenv("DD_LLMOBS_AGENTLESS_ENABLED"),
    env="dev",
    service="llmmode",
)

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")


@workflow
@cl.step(type="tool")
async def tool():
    # Fake tool
    # await cl.sleep(2)
    return "Response from the tool!"


@llm(model_name="claude", name="invoke_llm", model_provider="anthropic")
@cl.on_message  # this function will be called every time a user inputs a message in the UI
async def main(message: cl.Message):
    """
    This function is called every time a user inputs a message in the UI.
    It sends back an intermediate response from the tool, followed by the final answer.

    Args:
        message: The user's message.

    Returns:
        None.
    """

    # Call the tool
    tool_res = await tool()

    await cl.Message(content=tool_res).send()
