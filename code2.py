# -*- coding: utf-8 -*-
import web
from web import form

from sr import sr

to_learn_stack = [["je","suis",0],["tu","es",0],["nous","sommes",0],["vous",u"êtes",0],["il","est",0],["elle","est",0],["ils","sont",0],["elles","sont",0]]
spaced_rep = sr(to_learn_stack)

urls = ('/', 'index')
app = web.application(urls, globals())

render = web.template.render('templates/')

class index: 
	def GET(self): 
		item = spaced_rep.get_next_item()
		return render.a(item[0],"")

	def POST(self): 
		i = web.input() 
		if "show" in i.keys():
			if i.show == 'show': 
				item = spaced_rep.get_last_item_again()
				return render.a(item[0],item[1])
			
		if "form_action" in i.keys():
			if i.form_action == 'good': 
				spaced_rep.rate_current_item(+1) 
			elif i.form_action == 'norm': 
				spaced_rep.rate_current_item(0) 
			elif i.form_action == 'bad': 
				spaced_rep.rate_current_item(-1) 

			item = spaced_rep.get_next_item()
			return render.a(item[0],"")

if __name__=="__main__":
    web.internalerror = web.debugerror
    app.run()
