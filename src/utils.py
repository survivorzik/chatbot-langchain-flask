from sentence_transformers import SentenceTransformer
import pinecone
import openai
from dotenv.main import load_dotenv
import os
load_dotenv()

openai.api_key=os.getenv('OPENAI_API_KEY')
pineconeapikey=os.getenv('PINECONE_API_KEY')
model=SentenceTransformer('all-MiniLM-L6-v2')
pinecone.init(api_key=pineconeapikey,environment='asia-southeast1-gcp-free')
index=pinecone.Index('chatbot')

def findmatch(input):
    input_em=model.encode(input).tolist()
    
    result=index.query(input_em,top_k=2,includeMetadata=True)
    if result['matches']==[]:
        # index.upsert(input_em,ids=input,metadata=input)
        return result['matches']
    else:
        index.upsert(input_em,ids=input,metadata=input)
        
    return result['matches'][0]['metadata']['text']+'\n'+result['matches'][1]['metadata']['text']

def query_refiner(conversation,query):
    response=openai.Completion.create(
        model='ada',
        prompt=f"""Given the following user query and conversation log, formulate a long detailed question
        that would be the most relevant to provide the user with an 
        answer from a knowledge base and also remember their name and message them your ownself if necessary.\n\n CONVERSATION LOG: \n{conversation} \n\nQuery:{query}\n\n?
        Refined Query: """,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
        stop=['?']
    )
    return response['choices'][0]['text']

def get_conversation_string(requests, responses):
    conversation_string=""
    for i in range(len(responses)-1):
        conversation_string+=f"User: {requests[i]}\n"
        conversation_string+=f"Bot: {responses[i+1]}\n"
    print(conversation_string)
    return conversation_string    




