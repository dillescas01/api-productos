from fastapi import FastAPI
import mysql.connector
import schemas

app = FastAPI()

host_name = "98.82.74.138" # MV BD
port_number = "8005"
user_name = "root"
password_db = "utec"
database_name = "bd_api_productos"  

# Get echo test for load balancer's health check
@app.get("/")
def get_echo_test():
    return {"message": "Echo Test OK"}

# Get all productos
@app.get("/productos")
def listar_productos():
    mydb = mysql.connector.connect(host=host_name, port=port_number, user=user_name, password=password_db, database=database_name)  
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM productos")
    result = cursor.fetchall()
    cursor.close()
    mydb.close()
    return {"productos": result}

# Add a new producto
@app.post("/productos")
def crear_producto(item:schemas.Producto):
    mydb = mysql.connector.connect(host=host_name, port=port_number, user=user_name, password=password_db, database=database_name)  
    nombre = item.nombre
    descripcion = item.descripcion
    precio = item.precio
    inventario = item.inventario
    id_categoria = item.id_categoria
    cursor = mydb.cursor()
    sql = "INSERT INTO productos (nombre, descripcion, precio, inventario, id_categoria) VALUES (%s, %s, %s, %s, %s)"
    val = (nombre, descripcion, precio, inventario, id_categoria)
    cursor.execute(sql, val)
    mydb.commit()
    cursor.close()
    mydb.close()
    return {"message": "Producto creado exitosamente"}


# Modify a producto
@app.put("/productos/{id_producto}")
def actualizar_producto(id_producto:int, item:schemas.Producto):
    mydb = mysql.connector.connect(host=host_name, port=port_number, user=user_name, password=password_db, database=database_name)  
    nombre = item.nombre
    descripcion = item.descripcion
    precio = item.precio
    inventario = item.inventario
    id_categoria = item.id_categoria
    cursor = mydb.cursor()
    sql = "UPDATE productos SET nombre = %s, descripcion = %s, precio = %s, inventario = %s, id_categoria = %s WHERE id_producto = %s"
    val = (nombre, descripcion, precio, inventario, id_categoria, id_producto)
    cursor.execute(sql, val)
    mydb.commit()
    cursor.close()
    mydb.close()
    return {"message": "Producto modified successfully"}

# Delete an employee by ID
@app.delete("/productos/{id_producto}")
def eliminar_producto(id_producto: int):
    mydb = mysql.connector.connect(host=host_name, port=port_number, user=user_name, password=password_db, database=database_name)  
    cursor = mydb.cursor()
    cursor.execute(f"DELETE FROM productos WHERE id_producto = {id_producto}")
    mydb.commit()
    cursor.close()
    mydb.close()
    return {"message": "Producto deleted successfully"}