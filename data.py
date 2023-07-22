def userData(search):

    data =  [
        "Aziz", "Sardor", "Fazliddin", "XojiAkbar", "Abdulloh", "Akbar",
        "Sarvar", "Aziza", "Xurshid", "Abduvali", "Vali", "Sadriddin"
    ]

    return [ 
        item for item in data 
        if search.lower() in item.lower() and len(search) ]
