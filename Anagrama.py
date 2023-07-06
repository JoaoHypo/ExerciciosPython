string1 = input()
string2 = input()

string1.lower()
string2.lower()

especiais = ["á","é","í","ó","ú","â","ê","î","ô","û","ã","õ"]
tradução =  ["a","e","i","o","u","a","e","i","o","u","a","o"]

string1fix =''
for letra in string1:
    if letra in especiais:
        for indice,letraespecial in enumerate(especiais):
            if letra == letraespecial:
                string1fix = string1fix + tradução[indice]
    else:
        string1fix = string1fix + letra

#Esse bloco inteiro é pra conseidera japão igual a japao, 
# sem ele o programa identificaria como diferentes essas strings
string2fix =''
for letra in string2:
    if letra in especiais:
        for indice,letraespecial in enumerate(especiais):
            if letra == letraespecial:
                string2fix = string2fix + tradução[indice]
    else:
        string2fix = string2fix + letra

while string1fix == string2fix:
    string2 = input().lower()
    string2fix =''
    for letra in string2:
        if letra in especiais:
            for indice,letraespecial in enumerate(especiais):
                if letra == letraespecial:
                    string2fix = string2fix + tradução[indice]
        else:
            string2fix = string2fix + letra

if len(string1fix) != len(string2fix):
    print (f"{string1} não é um anagrama de {string2}")

listastring1 = sorted([x for x in string1fix])
listastring2 = sorted([x for x in string2fix])

if listastring1 == listastring2:  
    print (f"{string1} é um anagrama de {string2}")
