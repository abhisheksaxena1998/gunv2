import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
import pickle
import re
import flask
import praw
from flask import Flask, render_template, request

app=Flask(__name__)

REPLACE_BY_SPACE_RE = re.compile('[/(){}\[\]\|@,_;]')
BAD_SYMBOLS_RE = re.compile('[^0-9a-z #+_]')

'''flairs={1:"AskIndia",
2:"Non-Political",
3:"[R]eddiquette",
4:"Scheduled",
5:"Photography",
6:"Science/Technology",
7:"Politics",
8:"Business/Finance",
9:"Policy/Economy",
10:"Sports",
11:"Food",
12:"AMA"
}'''

@app.route('/')

@app.route('/index')
def index():
    return flask.render_template('index.html')

@app.route('/statistics')
def statistics():
    return flask.render_template('statistics.html')

@app.route("/register", methods=["POST"])
def register():
    if request.method=='POST':
        nm = request.form.get("url")
        mm=nm

        def warn(*args, **kwargs):
            pass
        import warnings
        warnings.warn = warn
        import warnings 
        from sklearn.externals import joblib
        warnings.filterwarnings(action = 'ignore')
        phrase=nm       #input("Enter : ")
        #filename2 = 'C:\\Users\\DELL\\Downloads\\wp3_Log_model_optimized.sav'
        filename2='log_gun_model_trained3.sav'
        loaded_model2 = joblib.load(filename2)
        arg=loaded_model2.predict(([phrase]))
        arg[0]
        from json.encoder import JSONEncoder
        final_entity = { "predicted_argument": [arg[0]]}
        # directly called encode method of JSON
        print (JSONEncoder().encode(final_entity))


        if arg[0]=='for':
            t='Pro-Gun'
        else:
            t='Anti-Gun'    
    #return flask.render_template('result.html',prediction=flairs[int(load_lr_model.predict(vect.transform([processed_tweet])))],url=mm)
    return flask.render_template('result.html',prediction=t,url=mm)
        
