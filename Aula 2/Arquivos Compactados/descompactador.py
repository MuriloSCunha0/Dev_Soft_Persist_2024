import os
from zipfile import ZipFile as zip

def compact_zip_folder(folder_path, output_file):
     # Create a ZipFile object
     with zip(output_file, 'w') as zip_file:
          # Iterate over all files in the folder
          for root, dirs, files in os.walk(folder_path):
               for file in files:
                    # Get the relative path of the file
                    relative_path = os.path.relpath(root, folder_path)
                    # Create the full path of the file
                    file_path = os.path.join(root, file)
                    # Add the file to the zip
                    zip_file.write(file_path, os.path.join(relative_path, file))


folder_to_compress = input('Enter the folder path: ')

output_gzip_file = 'compressed.zip'

zip_folder(folder_to_compress, output_gzip_file)

print('Done')
 
def descompactar_arquivos_zip(arquivo_gz, arquivo_saida):
        with zip.open(arquivo_gz, 'rb') as entrada:
            with open(arquivo_saida, 'wb') as saida:
                saida.write(entrada.read())
               
arquivo_comprimido = 'Aula 2\Arquivo de configuração'
nome_saida = 'descomprimido'
 
descompactar_arquivos_zip(arquivo_comprimido, nome_saida)
