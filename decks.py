# -*- coding: utf-8 -*-

deck_avoir = {"name":"avoir",
             "template":"deck.html", 
             "title":u"avoir",
             "questions":[["Je %s une pomme","'ai"], 
                          ["Tu %s une pomme","as"], 
                          ["Il %s une pomme","a"], 
                          ["Elle %s une pomme","a"], 
                          ["Nous %s une pomme","avons"], 
                          ["Vous %s une pomme","avez"], 
                          ["Ils %s une pomme","ont"], 
                          ["Elles %s une pomme","ont"]], 
             "qparser": lambda ptrn, dctn : ptrn % u"<question2>⟨ ? ⟩</question2>", 
             "aparser": lambda ptrn, dctn : ptrn % ("<answer>%s</answer>" % dctn)}

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
             "qparser": lambda ptrn, dctn : ptrn % u"<question2>⟨ ? ⟩</question2>", 
             "aparser": lambda ptrn, dctn : ptrn % ("<answer>%s</answer>" % dctn)}

deck_Ver = {"name":"Ver", 
             "template":"deck.html", 
             "title":u"V-er",
             "questions":[["Je %s une pomme","mang<frm>e</frm>"], 
                          ["Tu %s une pomme","mang<frm>es</frm>"], 
                          ["Il %s une pomme","mang<frm>e</frm>"], 
                          ["Elle %s une pomme","mang<frm>e</frm>"], 
                          ["Nous %s une pomme","mang<frm>ons</frm>"], 
                          ["Vous %s une pomme","mang<frm>ez</frm>"], 
                          ["Ils %s une pomme","mang<frm>ent</frm>"], 
                          ["Elles %s une pomme","mang<frm>ent</frm>"]], 
             "qparser": lambda ptrn, dctn : ptrn % u"<question2>⟨ mang<frm>er</frm> ⟩</question2>", 
             "aparser": lambda ptrn, dctn : ptrn % ("<answer>%s</answer>" % dctn)}

