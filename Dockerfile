FROM python:3-slim
WORKDIR /programas/api-productos

# Actualizar pip
RUN pip3 install --upgrade pip

# Instalar dependencias manualmente para identificar el problema
RUN pip3 install "fastapi[standard]"
RUN pip3 install pydantic
RUN pip3 install mysql-connector-python

# Copiar el código al contenedor
COPY . .

# Comando para iniciar la aplicación
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
