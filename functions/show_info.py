import json

def showInfo(path: str):
    with open(path, 'r') as file:
        content = file.read()

    ctt = json.loads(content)

    text = f"""
    LINK: {ctt["link"]}
    TITLE: {ctt["title"]}
    AUTHOR: {ctt["author"]}
    TIMELIMIT: {ctt["timelimit"]}
    DESCRIPTION: {ctt["description"]}
    INPUT: {ctt["input"]}
    OUTPUT: {ctt["output"]}

    | INPUT EXAMPLE                       
    {ctt["input-example"]}
    
    
    
    | OUTPUT EXAMPLE
    {ctt["output-example"]}
    
    """
    print(text)

showInfo("repo/info/1000.json")