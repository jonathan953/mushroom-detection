# Usando uma imagem oficial do Python 3.12-alpine como base
FROM python:3.12-alpine

# Instalar dependências do sistema (se necessário)
RUN apk update && \
    apk add --no-cache build-base libffi-dev openssl-dev python3-dev

# Definindo o diretório de trabalho
WORKDIR /app

# Copiando o arquivo de dependências para o container
COPY requirements.txt . 

# Instalando as dependências do projeto
RUN pip install -r requirements.txt

# Copiando todos os arquivos do projeto para o container
COPY . .

# Expondo a porta para o Jupyter Notebook
EXPOSE 8888

# Comando para rodar o Jupyter Notebook
CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--allow-root", "--no-browser"]
