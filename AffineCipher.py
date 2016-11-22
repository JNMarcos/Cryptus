#Cifra Afim

'''
Funcao para encriptar uma letra apenas, nessa funcao utiliza-se a tabela ASCII
onde cada letra tem seu codigo. Definir a e b e foi usada a equacao da cifra Afim.
Foram usadas funcoes do proprio python para transformar/destranformar uma 
letra em seu codigo correspondente da tabela ASCII. Importante saber que essas
funcoes funcionam para um caractere por vez. Letra tem que ser minuscula.
'''
def encryptLetter(letra):
    a = 5
    b = 8
    x = ord(letra) - 97 
    resultado = ((a*x) + b) % 26
    return chr(resultado + 97) 

'''
Nessa funcao usa-se a funcao anterior para encriptar uma mensagem agora.
Eh considerado que uma mensagem eh uma string. Sem espacos e tudo minusculo
(escolha da autora ser assim).
'''
def encryptString(palavra):
    palavraCriptografada = ""
    for i in palavra.lower():
      palavraCriptografada = palavraCriptografada + encryptLetter(i)
    return palavraCriptografada

'''
Essa funcao decripta a mensagem. Eh definido a e b e a funcao da cifra Afim para decriptar.
Como na funcao de encriptar aqui tambem usa-se a tabela ASCII e as funcoes do proprio
python que tranforma/destranforma uma letra. Essa letra tem que ser minuscula.
'''
def decryptLetter(letra):
    a = 21
    b = 8
    y = ord(letra) - 97
    resultado = (a*(y - 8)) % 26
    return chr(resultado + 97)

'''
Aqui usa-se a funcao anterior para decriptar uma mensagem inteira. A mensagem eh dita como uma string.
As letras sao todas minusculas.
'''
def decryptString(palavra):
    palavraDescriptada = ""
    for i in palavra.lower():
      palavraDescriptada = palavraDescriptada + decryptLetter(i)
    return palavraDescriptada

'''
Nessa parte apenas um mini programa com um menu para rodar o codigo acima
'''
while True:
    escolha = raw_input("Digite 1 para encriptar ou 2 para decriptar: ")
    if escolha == "1":
      palavra = raw_input("Digite sua mensagem sem espacos para ser criptografada: ")
      print encryptString(palavra)
      break
    elif escolha == "2":
      palavra = raw_input("Digite sua mensagem sem espacos para ser descriptografada: ")
      print decryptString(palavra)
      break
    else:
      print "Opcao invalida, digite novamente!"

    
