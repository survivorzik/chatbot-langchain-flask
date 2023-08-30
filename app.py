from flask import Flask,request,render_template,jsonify
from flask_cors import CORS
import os
import sys
from src.components.chatbot import Chatbot
from src.logger import logging
from src.exception import CustomException


app= Flask(__name__)
CORS(app)

@app.route('/',methods=["GET"])
def proper():
    input="User has not replied or is away kindly message them."
    try:
        logging.info("User has not replied or is away kindly message them.")
        chat=Chatbot()
        result=chat.generateresponse(input)
        logging.info(f"Response from User {result}")
    except Exception as e:
        raise CustomException(e,sys)
        return jsonify({"response":False,"message":str(e)})
    return jsonify({"response":True,"message":result})
        
def generate():
    while True:
        user=input("Hey Interact with me I am A Chatbot")
        os.system('cls' if os.name == 'nt' else 'clear')
        if user=='q':
            break
        else:
            try:
                chat=Chatbot()
                logging.info(f"Chatbot initialized with user query={user}")
                # print(query,'query')
                response=chat.generateresponse(user)
                # print('Response')
                logging.info(response)
            except Exception as e:
                raise CustomException(e,sys)
                logging.info(f"{str(e)}")
        
        
            


@app.route('/data',methods=["POST"])
def index():
    data=request.get_json()
    query=data.get('data')
    logging.info(query)
    try:
        chat=Chatbot()
        logging.info('Chatbot initialized')
        # print(query,'query')
        
        response=chat.generateresponse(query)
        logging.info(response)
    except Exception as e:
        raise CustomException(e,sys)
        logging.info(f"{str(e)}")
        return jsonify({"response":False,"message":str(e)})
    return jsonify({"response":True,"message":response})

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True,port=5000)        
    