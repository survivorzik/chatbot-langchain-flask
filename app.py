from flask import Flask,request,render_template,jsonify
from flask_cors import CORS
import os
from src.components.chatbot import Chatbot
app= Flask(__name__)

@app.route('/data',methods=["POST"])
def index():
    data=request.get_json()
    query=data.get('data')
    print(query)
    try:
        chat=chatbot()
        response=chat.generateresponse(query)
    except Exception as e:
        response=str(e)
        print(response)
        return jsonify({"response":False,"message":response})
    return jsonify({"response":True,"message":response})

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True,port=5000)        
    