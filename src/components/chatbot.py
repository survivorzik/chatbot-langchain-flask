import os 
import sys
from langchain.chat_models import ChatOpenAI
from langchain.chains import ConversationChain
from langchain.text_splitter import CharacterTextSplitter
from langchain.chains.conversation.memory import ConversationBufferWindowMemory
from langchain.prompts import (
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
    ChatPromptTemplate,
    MessagesPlaceholder)
from src.utils import Utils
from langchain.docstore.document import Document
from langchain.chains.summarize import load_summarize_chain
from src.exception import CustomException
from src.logger import logging
from dotenv.main import load_dotenv
load_dotenv()

openai_api_key=os.getenv('OPENAI_API_KEY')



class Chatbot:
    def __init__(self):
        self.buffer_memory=ConversationBufferWindowMemory(k=16,return_messages=True)
        self.llm=ChatOpenAI(model="gpt-3.5-turbo",openai_api_key=openai_api_key)
        self.system_msg_template=SystemMessagePromptTemplate.from_template(template="""You Are a chatbot and interact with the user.""")
        self.human_msg_template=HumanMessagePromptTemplate.from_template(template="{input}")
        self.prompt_template=ChatPromptTemplate.from_messages([self.system_msg_template,MessagesPlaceholder(variable_name='history'),self.human_msg_template])
        self.conversation=ConversationChain(memory=self.buffer_memory,prompt=self.prompt_template,llm=self.llm,verbose=False)
        self.chain=load_summarize_chain(llm=self.llm, chain_type="stuff")
        self.requests=["Hey How can i help you"]
        self.responses=[]
        self.utils=Utils()
        
    def generateresponse(self,input):
        # print("input",input)
        if len(self.requests) > 0:
            # print("input1",input)
            conversation_string=self.utils.get_conversation_string(requests=self.requests,responses=self.responses)
            refined_query=self.utils.query_refiner(conversation_string,input)
            context=self.utils.findmatch(refined_query)
            # print(refined_query,'refined_query')
        else:
            # print('in else')
            refined_query=input
        # print('context')
        self.utils.add_text(input)
        response=self.conversation.predict(input=f"""Context:\n {context} \n\n Query:\n{input} """)
        self.requests.append(input)
        self.responses.append(response)
        # print(response)
        return response            
    
    def generatesummary(self):
        docs=self.utils.get_all_docs()
        # splitter=CharacterTextSplitter()
        # texts=splitter.split_documents(docs)
        doc=[Document(page_content=t) for t in docs]
        
        global_summary =  self.chain.run(doc)
        return global_summary
        
        
        
    
    