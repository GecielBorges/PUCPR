# Usar a imagem oficial do Python como base
FROM python:3.10-slim

# Definir o diretório de trabalho dentro do contêiner
WORKDIR /app

# Copiar o arquivo de dependências (requirements.txt) para o diretório de trabalho
COPY requirements.txt .

# Instalar as dependências listadas no requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copiar o restante do código da API para o diretório de trabalho
COPY . .

# Expor a porta que o FastAPI usa (8000 por padrão)
EXPOSE 8000

# Comando para iniciar o servidor FastAPI com Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
