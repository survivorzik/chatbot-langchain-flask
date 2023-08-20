from flask import Flask,request,render_template,jsonify
from flask_cors import CORS
import numpy as np
import pandas as pd
import os
from src.components import chatbot
app= Flask(__name__)

@app.route('/',methods=["POST"])
def index():
    data=request.get_json()
    query=data.get('data')
    try:
        chat=chatbot()
        response=chat.generateresponse(query)
    except Exception as e:
        response=str(e)
        return jsonify({"response":False,"message":response})
    return jsonify({"response":True,"message":response})

if __name__ == '__main__':
    app.run(debug=True)        
    