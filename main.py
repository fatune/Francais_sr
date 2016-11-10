# -*- coding: utf-8 -*-
from flask import Flask, render_template, request
app = Flask(__name__)

from sr import sr
import decks

decks = {"etre":   sr(decks.to_learn_stack_etre),
         "Ver" :   sr (decks.to_learn_stack_Ver),
       "avoir" : sr (decks.to_learn_stack_avoir)}

@app.route("/")
def index():
    return "Index!"
 
@app.route("/decks")
def members():
    return "Decks"

@app.route("/decks/<string:name>/")
def getMember(name):
    item = decks[name].get_next_item()
    question = item[0]
    answer = ""
    return render_template('deck.html',**locals())


@app.route("/decks/<string:name>/", methods=['POST'])
def getMember_post(name):
    if request.method == 'POST':
        if request.form['submit'] == "Show answer":
            item = decks[name].get_last_item_again()
            question = item[0]
            answer = item[1]
            return render_template('deck.html',**locals())
        elif request.form['submit'] == "Bad":
            rate = -1
        elif request.form['submit'] == "Norm":
            rate = 0
        elif request.form['submit'] == "Good":
            rate = 1
	decks[name].rate_current_item(rate) 
        return getMember(name)
        #return render_template('deck.html',**locals())
    return "?"
 
if __name__ == "__main__":
    app.run(debug=True)
