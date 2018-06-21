import requests,sys


#VERIFICANDO SE EH UM LINK VALIDO
def isSite(link):
    protocolo = link[0:5]

    if protocolo != 'https':
        protocolo = link[0:4]
        if protocolo != 'http':
            return False
    if protocolo == 'https':    
        if link[5] != ':' or link[6] != '/' or link[7] != '/':
            return False
    else:
        if link[4] != ':' or link[5] != '/' or link[6] != '/':
            return False
    return True


#VERIFICANDO SE É UM CPF
def isCPF(string):
    #Se o tamanho da string for 11 QUER DIZER QUE NAO TEM SIMBOLOS, APENAS NUMEROS
    if len(string) == 11:

        #PARA CADA VALOR NO INTERVALO DE 0 A 11
        for i in range(len(string)):

            #SE O RETORNO DO METODO FOR FALSO
            if not string[i].isdecimal():
                #RETORNE FALSO
                return False
    else:
        for i in range(0,3):
            if not string[i].isdecimal():
                return False

        for i in range(4,7):
            if not string[i].isdecimal():
                return False
        
        for i in range(8,11):
            if not string[i].isdecimal():
                return False
        for i in range(12,14):
            if not string[i].isdecimal():
                return False

        if string[3] != '.' or string[7] != '.' or string[11] != '-':
            return False
    return True           
          

if len(sys.argv) < 2:
    print('Uso: \t \t site')
else:
    site = sys.argv[1]
    if isSite(site):
        print(site + ' eh um Site!')
        conteudo = requests.get(site)
        conteudo = str(conteudo.content[:9999])
        for i in range(len(conteudo)):
            cp = conteudo[i:i+11]
            cp2 = conteudo[i:i+14]
            if isCPF(cp):
                print(cp)
            if isCPF(cp2):
                print(cp2)
    else:
        print('Isira um site valido')
print('Feito!')
