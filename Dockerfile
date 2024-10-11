FROM python:3.9
WORKDIR /programas/api-productos

# Actualizar pip
RUN pip3 install --upgrade pip

# Instalar dependencias
RUN pip3 install "fastapi[standard]"
RUN pip3 install pydantic
RUN pip3 install mysql-connector-python

# Copiar el código al contenedor
COPY . .

# Comando para iniciar la aplicación
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
