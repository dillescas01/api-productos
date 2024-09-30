from pydantic import BaseModel

# Esquema para crear o actualizar un producto
class ProductoBase(BaseModel):
    nombre: str
    descripcion: str
    precio: float
    inventario: int
    id_categoria: int

# Esquema para respuesta que incluye el id del producto
class ProductoResponse(ProductoBase):
    id_producto: int

    class Config:
        orm_mode = True

# Esquema para crear o actualizar una categoría
class CategoriaBase(BaseModel):
    nombre_categoria: str

# Esquema para respuesta que incluye el id de la categoría
class CategoriaResponse(CategoriaBase):
    id_categoria: int

    class Config:
        orm_mode = True
