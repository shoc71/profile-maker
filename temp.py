def dash_end_removal(name : str) -> str:
    apo = "'"
    
    if len(name) < 1:
        return ''
    
    if (apo in name[-1]):
        # name.replace(apo, "")
        print(name)
        return name[:-1]
    
    return name

list_of_str = ["hi", "test'", "cheese",""]

lester = [dash_end_removal(n) for n in list_of_str]
print(lester)