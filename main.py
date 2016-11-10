# -*- coding: utf-8 -*-
from flask import Flask, render_template, request, Markup
app = Flask(__name__)

from sr import sr, sr2
import decks

decks = {"etre":   sr2(decks.deck_etre),
         "Ver" :   sr (decks.to_learn_stack_Ver),
       "avoir" : sr (decks.to_learn_stack_avoir)}

@app.route("/")
def index():
    return "Index!"
 
@app.route("/decks")
def members():
    return render_template('decks.html', decks = decks)

@app.route("/deck/<string:name>/")
def getMember(name):
    item = decks[name].get_next_item()
    title = decks[name].title
    question = item[0]
    return render_template('deck.html', text = Markup(question), title = title,quest="1")


@app.route("/deck/<string:name>/", methods=['POST'])
def getMember_post(name):
    if request.method == 'POST':
        if request.form['submit'] == "Show answer":
            item = decks[name].get_last_item_again()
            title = decks[name].title
            answer = item[1]
            return render_template('deck.html',text = Markup(answer), title = title )
        elif request.form['submit'] == "Bad":
            rate = -1
        elif request.form['submit'] == "Norm":
            rate = 0
        elif request.form['submit'] == "Good":
            rate = 1
	decks[name].rate_current_item(rate) 
        return getMember(name)
    return "?"
 
if __name__ == "__main__":
    app.run(debug=True)
