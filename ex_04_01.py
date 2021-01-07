
x=5
print("Hello")

def print_lyrics():
    print("Amar sonar bangla ami tomai valobashi")
    print("Chiro din tmr akash tmr batash amar prane")

print("Yo")
x=x+2
print(x)
print_lyrics()

def greet(lang):
    if lang == 'es':
        return "Holla"
    elif lang == 'fr':
        return "Bonjour"
    else:
        return "Hello"
print(greet('en'), "Gleen")
print(greet('es'), "Sally")
print(greet('fr'), "Micheal")

def addtwo(a,b):
    added = a+b
    return a
x =addtwo(10,5)
print(x)
