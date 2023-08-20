import os 
import sys
from langchain.chat_models import ChatOpenAI
from langchain.chains import ConversationChain
from langchain.chains.conversation.memory import ConversationBufferWindowMemory
from langchain.prompts import (
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
    ChatPromptTemplate,
    MessagesPlaceholder)
from src.utils import *
from src.exception import CustomException
from src.logger import logging
from dotenv.main import load_dotenv
load_dotenv()
openai_api_key=os.getenv('OPENAI_API_KEY')



class Chatbot:
    def __init__(self):
        self.buffer_memory=ConversationBufferWindowMemory(k=3,return_messages=True)
        self.llm=ChatOpenAI(model="gpt-3.5-turbo",openai_api_key=openai_api_key)
        self.system_msg_template=SystemMessagePromptTemplate.from_template(template="""You Are a chatbot and interact with the user.""")
        self.human_msg_template=HumanMessagePromptTemplate.from_template(template="{input}")
        self.prompt_template=ChatPromptTemplate.from_messages([system_msg_template,MessagesPlaceholder(variable_name='history'),self.human_msg_template])
        self.conversation=ConversationChain(memory=self.buffer_memory,prompt=self.prompt_template,llm=self.llm,verbose=True)
        self.requests=[]
        self.responses=["Hey User How are you"]
    def generateresponse(self,input):
        if len(self.requests) > 0:
            conversation_string=get_conversation_string(requests=self.requests,responses=self.responses)
            refined_query=query_refiner(input)
        else:
            refined_query=input
        context=findmatch(refined_query)
        response=self.conversation.predict(input=f"""Context:\n {context} \n\n Query:\n{input} """)
        self.requests.append(query)
        self.responses.append(query)
        return response            
        
    
    