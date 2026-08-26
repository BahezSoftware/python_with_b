dic = {
        "info":[ [
        "this is simple dictionary"
             ],4,3,
        "bahez",
    
               ],
        "whatsapp":("bahez","this is tuple"),
       "person": {"number":1,
         "name":"bahez"},
         "karo":"laro"
      }

print(dic.update({"whatsapp":"this is updated value"}))
print(dic.get("whatsapp"))
print(dic.get("whatsapp"))
print(dic.get("info"))
print(dic.pop("karo"))
print(dic.keys())
print(dic.values()  )
# print(dic["info"][0][0])
# print(dic["whatsapp"][1])
# print(dic["person"]["name"])
# print(dic["karo"])
