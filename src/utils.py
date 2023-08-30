from langchain.embeddings.openai import OpenAIEmbeddings
from sentence_transformers import SentenceTransformer
from langchain.text_splitter import SentenceTransformersTokenTextSplitter as ss
from langchain.vectorstores.chroma import Chroma

import openai
from dotenv.main import load_dotenv
import os
load_dotenv()


openai.api_key=os.getenv('OPENAI_API_KEY')
class Utils:

    def __init__(self):
        self.model=OpenAIEmbeddings(
        openai_api_key=openai.api_key,
        model='text-embedding-ada-002')
        # self.
        self.vectorStore=Chroma('langchain_store',self.model)
        
        
    def add_text(self,input):
        splitter = ss(chunk_size=50,chunk_overlap=0)
        input_splt=splitter.split_text(text=input)
        self.vectorStore.add_texts([input])

    def findmatch(self,input):
        result=self.vectorStore.similarity_search(query=input)
        if result==[]:
            return result
        else:
            response=""
            for i in range (len(result)):
                response+=result[i].page_content+" "
            return response

    def query_refiner(self,conversation,query):
        response=openai.Completion.create(
            model='ada',
            prompt=f"""###SYSTEM: Your an AI chatbot at a Ecommerce Website If anyThing asked other than ecommerce just say I dont know. Please give the answer based upon following text and your duty is to respond to user query. 
            ###TEXT: {conversation} 
            ###USER:{query}?
            ###RESPONSE: """,
            temperature=0.2,
            max_tokens=1024,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0,
            stop=['?']
        )
        return response['choices'][0]['text']

    def get_conversation_string(self,requests, responses):
        conversation_string=""
        for i in range(len(responses)-1):
            conversation_string+=f"User: {requests[i]}\n"
            conversation_string+=f"Bot: {responses[i+1]}\n"
        print(conversation_string)
        return conversation_string    




