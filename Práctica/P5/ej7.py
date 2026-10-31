palabras = ["sol", "luna", "sol", "estrella", "luna", "sol","sol"]
dic_pal = {}
i = 0

for pal in palabras:
    if pal not in dic_pal:
        dic_pal.update ({pal : i})
    elif pal in dic_pal:
        dic_pal.update ({pal : i + 1})
        i += 1
print(dic_pal)
            