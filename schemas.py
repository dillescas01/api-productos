from pydantic import BaseModel

class Producto(BaseModel):
    nombre: str
    descripcion: str
    precio: float
    inventario: int
    id_categoria: int

class Categoria(BaseModel):
    nombre_categoria: str