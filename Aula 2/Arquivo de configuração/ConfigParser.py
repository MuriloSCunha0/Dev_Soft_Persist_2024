import configparser as cp

config = cp.ConfigParser()
filename = r'Aula 2\Arquivo de configuração\config.ini'
config.read(filename)

sections = config.sections()
print(sections)

for section in sections:
    print(f'\n[{section}]')
    for key in config[section]:
        print(f'{key} = {config[section][key]}')


