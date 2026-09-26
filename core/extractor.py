from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough, RunnableLambda


def get_llm():
    return ChatOllama(
        model="llama3.2:3b",
        temperature=0.0
    )

def build_chain(system_prompt : str):
    llm = get_llm()
    return (
        RunnablePassthrough() | RunnableLambda(lambda x : {"text" : x}) |ChatPromptTemplate.from_messages([
        ("system", system_prompt),
        ("human","{text}"),
    ]) | llm |StrOutputParser()
    )

def extract_action_items(transcript: str) -> str:
    chain = build_chain(
        "You are an expert meeting analyst.\n"
        "Extract ONLY action items that are explicitly stated in the transcript.\n\n"
        "Rules:\n"
        "- Do NOT invent or infer tasks.\n"
        "- Do NOT turn examples, hypothetical scenarios, explanations, or suggestions into action items.\n"
        "- An action item must be an explicitly stated task or to-do item.\n"
        "- Include the owner only if explicitly mentioned.\n"
        "- Include the deadline only if explicitly mentioned.\n"
        "- If no explicit action items exist, return exactly: 'No action items found.'\n\n"
        "Format as a numbered list."
    )

    return chain.invoke(transcript)


def extract_key_decisions(transcript: str) -> str:
    chain = build_chain(
        "You are an expert meeting analyst.\n"
        "Extract ONLY decisions that were explicitly made in the transcript.\n\n"
        "Rules:\n"
        "- A decision must be an explicit choice, agreement, approval, rejection, or final decision.\n"
        "- Do NOT treat explanations, facts, opinions, examples, or discussion points as decisions.\n"
        "- Do NOT invent decisions.\n"
        "- If no explicit decisions were made, return exactly: 'No key decisions found.'\n\n"
        "Format as a numbered list."
    )

    return chain.invoke(transcript)

def extract_questions(transcript: str) -> str:
    chain = build_chain(
        "You are an expert meeting analyst.\n"
        "Extract ONLY questions that are explicitly present in the transcript "
        "and remain unanswered, or topics explicitly identified as requiring follow-up.\n\n"
        "Rules:\n"
        "- Do NOT generate new questions.\n"
        "- Do NOT infer questions from the discussion.\n"
        "- Do NOT turn general topics into questions.\n"
        "- Only use information explicitly present in the transcript.\n"
        "- If there are no explicit unanswered questions or follow-up topics, "
        "return exactly: 'No open questions found.'\n\n"
        "Format as a numbered list."
    )

    return chain.invoke(transcript)