import os
from pathlib import Path
from dotenv import load_dotenv
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

dotenv_path = Path('.') / '.env'
load_dotenv(dotenv_path = dotenv_path)

OPENAI_API_KEY = os.getenv("REACT_APP_OPENAI_KEY")
print(OPENAI_API_KEY)

# initialize the models
llm = OpenAI(
    model_name="text-davinci-003",
    openai_api_key= OPENAI_API_KEY,
    temperature= 0.1
)


class Langchain: 
    def __init__(self, query):
        self.query = query
        self.llm = OpenAI(model_name="text-davinci-003", openai_api_key= OPENAI_API_KEY, temperature= 0.1)
        self.template = """Assistant is a large language model trained by OpenAI.

Assistant is designed to be able to assist with a wide range of tasks, from answering simple questions to providing in-depth explanations and discussions on a wide range of topics. As a language model, Assistant is able to generate human-like text based on the input it receives, allowing it to engage in natural-sounding conversations and provide responses that are coherent and relevant to the topic at hand.

Assistant is constantly learning and improving, and its capabilities are constantly evolving. It is able to process and understand large amounts of text, and can use this knowledge to provide accurate and informative responses to a wide range of questions. Additionally, Assistant is able to generate its own text based on the input it receives, allowing it to engage in discussions and provide explanations and descriptions on a wide range of topics.

Overall, Assistant is a powerful tool that can help with a wide range of tasks and provide valuable insights and information on a wide range of topics. Whether you need help with a specific question or just want to have a conversation about a particular topic, Assistant is here to assist.

Human: {query}
Assistant:"""
        self.prompt_template = PromptTemplate(input_variables=["query"], template=self.template)
        self.answer_chain = LLMChain(llm=self.llm, prompt=self.prompt_template)
        self.answer = self.answer_chain.run(query=self.query)

    def get_answer(self):
        print(self.answer)
        return self.answer




