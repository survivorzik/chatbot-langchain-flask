import os 
import sys
from langchain.chat_models import ChatOpenAI
from langchain.chains import ConversationChain
from langchain.chains.conversation.memory import ConversationBufferWindowMemory
from langchain.prompts import (
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
    ChatPromptTemplate,
    MessagesPlaceholder
)
from dotenv.main import load_dotenv
load_dotenv()
openai_api_key=os.getenv('OPENAI_API_KEY')

from src.exception import CustomException
from src.logger import logging

class Chatbot:
    def __init__(self):
        self.buffer_memory=ConversationBufferWindowMemory(k=3,return_messages=True)
        self.llm=ChatOpenAI(model="gpt-3.5-turbo",openai_api_key=openai_api_key)
        self.system_msg_template=SystemMessagePromptTemplate.from_template(template="""You Are a chatbot and ineract with the user.""")
        self.human_msg_template=HumanMessagePromptTemplate.from_template(template="{input}")
        self.prompt_template=ChatPromptTemplate.from_messages([system_msg_template,MessagesPlaceholder(variable_name='history'),self.human_msg_template])
        self.conversation=ConversationChain(memory=self.buffer_memory,prompt=self.prompt_template,llm=self.llm,verbose=True)
        self.requests=[]
        self.responses=["Hey User How are you"]
    
    