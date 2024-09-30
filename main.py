from fastapi import FastAPI, HTTPException
import mysql.connector
from pydantic import BaseModel

app = FastAPI()

# Parámetros de conexión a la base de datos
host_name = "100.27.62.167" # IP MV Bases de Datos
port_number = "8005"
user_name = "root"
password_db = "utec"
database_name = "bd_api_employees"

# Conexión a MySQL
def get_db_connection():
    return mysql.connector.connect(
        host=host_name,
        port=port_number,
        user=user_name,
        password=password_db,
        database=database_name
    )

# Endpoint de prueba para el balanceador de carga
@app.get("/")
def get_echo_test():
    return {"message": "Echo Test OK"}

# Modelo para los productos
class Producto(BaseModel):
    nombre: str
    descripcion: str
    precio: float
    inventario: int
    id_categoria: int

@app.get("/productos")
def listar_productos():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM productos")
    productos = cursor.fetchall()
    conn.close()
    return productos

@app.post("/productos")
def crear_producto(producto: Producto):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO productos (nombre, descripcion, precio, inventario, id_categoria) VALUES (%s, %s, %s, %s, %s)",
        (producto.nombre, producto.descripcion, producto.precio, producto.inventario, producto.id_categoria)
    )
    conn.commit()
    conn.close()
    return {"mensaje": "Producto creado exitosamente"}

@app.put("/productos/{id_producto}")
def actualizar_producto(id_producto: int, producto: Producto):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE productos SET nombre = %s, descripcion = %s, precio = %s, inventario = %s, id_categoria = %s WHERE id_producto = %s",
        (producto.nombre, producto.descripcion, producto.precio, producto.inventario, producto.id_categoria, id_producto)
    )
    conn.commit()
    conn.close()
    return {"mensaje": "Producto actualizado exitosamente"}

@app.delete("/productos/{id_producto}")
def eliminar_producto(id_producto: int):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM productos WHERE id_producto = %s", (id_producto,))
    conn.commit()
    conn.close()
    return {"mensaje": "Producto eliminado exitosamente"}
