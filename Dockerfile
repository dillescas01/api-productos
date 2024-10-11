FROM python:3-slim
WORKDIR /programas/api-productos

# Actualizar pip
RUN pip3 install --upgrade pip

# Copiar el archivo de requisitos e instalar dependencias
COPY requirements.txt .
RUN pip3 install -r requirements.txt

# Copiar el código al contenedor
COPY . .

# Comando para iniciar la aplicación
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
