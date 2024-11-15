import guardrails as gd
import streamlit as st

from src.models import LLMResponse
from src.prompt import PROMPT
from phoenix.otel import register
from openinference.instrumentation.openai import OpenAIInstrumentor


@st.cache_resource
def get_guard() -> gd.Guard:
    """
    Create an output guard using GuardRails.
    """
    return gd.Guard.from_pydantic(output_class=LLMResponse, prompt=PROMPT)

@st.cache_resource
def instrument() -> None:
    """
    Instrument the OpenAI API using Phoenix.
    """
    tracer_provider = register(
        project_name="my-llm-app",
        endpoint="http://phoenix:6006/v1/traces",
    )
    OpenAIInstrumentor().instrument(tracer_provider=tracer_provider)