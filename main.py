# -*- coding: utf-8 -*-
from flask import Flask, render_template, request, Markup, redirect
app = Flask(__name__)

from sr import sr2
import decks

decks = {"etre": sr2(decks.deck_etre),
         "Ver" : sr2(decks.deck_Ver),
         "Vir" : sr2(decks.deck_Vir),
         "faire" : sr2(decks.deck_faire),
         "aller" : sr2(decks.deck_aller),
         "vouloir" : sr2(decks.deck_vouloir),
         "pouvoir" : sr2(decks.deck_pouvoir),
         "possessives" : sr2(decks.deck_possessives),
         "devoir" : sr2(decks.deck_devoir),
       "avoir" : sr2(decks.deck_avoir)}

@app.route("/")
def index():
    return "Index!"
 
@app.route("/decks")
def members():
    return render_template('decks.html', decks = decks)

@app.route("/back/<string:name>/")
def go_back(name):
    decks[name].rate_current_item(0)
    return redirect("/decks")
    

@app.route("/deck/<string:name>/")
def getMember(name):
    item = decks[name].get_next_item()
    title = decks[name].title
    question = item[0]
    return render_template('deck.html', text = Markup(question), title = title,quest="1",name=name)


@app.route("/deck/<string:name>/", methods=['POST'])
def getMember_post(name):
    if request.method == 'POST':
        if request.form['submit'] == "Show answer":
            item = decks[name].get_last_item_again()
            title = decks[name].title
            answer = item[1]
            return render_template('deck.html',text = Markup(answer), title = title,name=name )
        elif request.form['submit'] == "Bad":
            rate = -1
        elif request.form['submit'] == "Norm":
            rate = 0
        elif request.form['submit'] == "Good":
            rate = 1
	decks[name].rate_current_item(rate) 
        item = decks[name].get_next_item()
        title = decks[name].title
        question = item[0]
        return getMember(name)
    return "?"
 
if __name__ == "__main__":
    app.run(debug=True)
