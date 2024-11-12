#Escrevendo em um arquivo txt
with open('Aula 1\Manipulação de Arquivos\arquivo.txt', 'w', encoding= 'utf-8') as f:
    while True:
        try:
            line = input('Digite algo: ')

            print(line, file=f) 

        except EOFError:
            break