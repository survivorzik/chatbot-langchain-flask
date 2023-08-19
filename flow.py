# from langchain.llms import OpenAI
# from langchain.embedding import OpenAIEmbeddings
# from langchain.text_splitter import CharacterTextSplitter
# from langchain.text_generator import TextGenerator


import openai

context={
    'role':'system',
    "content":"""act as a waiter in a fast foot restaurant
    Ask the customer what they want and offer them the items on the menu: 
    in the menu there is 
    fuet sandwitch 2 
    Ham Sandwitch 6 
    water 2"""
}