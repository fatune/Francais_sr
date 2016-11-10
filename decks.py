# -*- coding: utf-8 -*-
to_learn_stack_etre = [["je","suis",0],
                       ["tu","es",0],
                       ["il","est",0],
                       ["elle","est",0],
                       ["nous","sommes",0],
                       ["vous",u"êtes",0],
                       ["ils","sont",0],
                       ["elles","sont",0]]

to_learn_stack_Ver = [["je","V-e",0],
                      ["tu","V-es",0],
                      ["il","V-e",0],
                      ["elle","V-e",0],
                      ["nous","V-ons",0],
                      ["vous",u"V-ez",0],
                      ["ils","V-ent",0],
                      ["elles","V-ent",0]]

to_learn_stack_avoir = [["je","'ai",0],
                        ["tu","as",0],
                        ["il","a",0],
                        ["elle","a",0],
                        ["nous","avons",0],
                        ["vous","avez",0],
                        ["ils","ont",0],
                        ["elles","ont",0]]

deck_etre = {"name":"etre", 
             "template":"deck.html", 
             "title":u"être",
             "questions":[["Je %s grande","suis"], 
                          ["Tu %s grande","es"], 
                          ["Il %s grande","est"], 
                          ["Elle %s grande","est"], 
                          ["Nous %s grandes","sommes"], 
                          ["Vous %s grandes",u"êtes"], 
                          ["Ils %s grandes","sont"], 
                          ["Elles %s grandes","sont"]], 
             "qparser": lambda ptrn, dctn : ptrn % u"<être>", 
             "aparser": lambda ptrn, dctn : ptrn % dctn}


