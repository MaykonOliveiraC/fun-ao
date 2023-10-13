config_file = "config.txt"

try:
    with open(config_file, "r") as file:
        config = file.read()
        print("Configurações lidas com sucesso:", config)
except FileNotFoundError:
    print(f"O arquivo '{config_file}' não existe. Criando um novo arquivo de configuração...")
    default_config = "parametro1=valor1\nparametro2=valor2"
    with open(config_file, "w") as file:
        file.write(default_config)
        print("Novo arquivo de configuração criado.")
except IOError as e:
    print(f"Erro ao ler ou escrever o arquivo: {e}")
