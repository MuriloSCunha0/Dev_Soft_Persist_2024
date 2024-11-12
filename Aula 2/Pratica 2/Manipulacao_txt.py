import zipfile
import os
#Criar um diretorio de arquivos txt
os.mkdir('arquivos_txt')
#Mudar o diretorio de trabalho
os.chdir('arquivos_txt')
#Criar um arquivo txt
quantidade_de_arquivos = 10
for i in range(quantidade_de_arquivos):
    with open(f'arquivo_{i}.txt', 'w') as arquivo:
        arquivo.write(f'Este e o arquivo {i}')

#Listar os arquivos do diretorio
print(os.listdir())

#Ler conteudo dos arquivos
for arquivo in os.listdir():
    with open(arquivo, 'r') as arquivo:
        print(arquivo.read())

#COntar quantidade de letras em cada arquivo
for arquivo in os.listdir():
    with open(arquivo, 'r') as arquivo:
        conteudo = arquivo.read()
        print(f'O arquivo {arquivo.name} tem {len(conteudo)} letras')


#Criar um arquivo consolidado
with open('arquivo_consolidado.txt', 'w') as arquivo_consolidado:
    for arquivo in os.listdir():
        with open(arquivo, 'r') as arquivo:
            conteudo = arquivo.read()
            palavras = conteudo.split()
            arquivo_consolidado.write(f'O arquivo {arquivo.name} tem {len(palavras)} palavras e {len(conteudo)} letras\n')

#Criar arquivo zipado com os arquivos txt e o arquivo consolidado
with zipfile.ZipFile('arquivos.zip', 'w') as zipado:
    for arquivo in os.listdir():
        zipado.write(arquivo)
    zipado.write('arquivo_consolidado.txt')





