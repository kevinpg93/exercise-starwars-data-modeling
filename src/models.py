import os
import sys
from sqlalchemy import Integer, String
from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship, Mapped
from typing import List
from sqlalchemy import ForeignKey
Base = declarative_base()
class Usuarios(Base):
    __tablename__ = "usuarios"
    id = mapped_column(Integer, primary_key=True)
    nombre = mapped_column(String(50), nullable=False)
    correo = mapped_column(String(100))  #La mapped_column()directiva se utiliza para todos los atributos basados ​​en columnas que requieren una personalización más específica
    contrasena = mapped_column(String(20))
    suscripcion = mapped_column(String(10))
    favoritos: Mapped[List["Favoritos"]] = relationship()
class Planetas(Base):
    __tablename__ = "planetas"
    id = mapped_column(Integer, primary_key=True)
    nombre_planeta = mapped_column(String(50), nullable=False)
    favoritos: Mapped[List["Favoritos"]] = relationship()
class Personajes(Base):
    __tablename__ = "personajes"
    id = mapped_column(Integer, primary_key=True)
    nombre_personaje = mapped_column(String(50), nullable=False)
    favoritos: Mapped[List["Favoritos"]] = relationship()
class Favoritos(Base):
    __tablename__ = "favoritos"
    id = mapped_column(Integer, primary_key=True)
    usuarios_id: Mapped[int] = mapped_column(ForeignKey("usuarios.id"))
    planetas_id: Mapped[int] = mapped_column(ForeignKey("planetas.id"))
    personajes_id: Mapped[int] = mapped_column(ForeignKey("personajes.id"))
## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')