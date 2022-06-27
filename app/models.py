from sqlalchemy import (
    Column,
    ForeignKey,
    Integer,
    String,
    Table,
    DateTime,
)
from sqlalchemy.orm import relationship
from app.database import Base


class Chat(Base):
     __tablename__ = "chat"
     __table_args__ = {'extend_existing': True}

     id = Column(Integer, primary_key=True, index=True)
     mensaje = Column(String, nullable=False)
     avatar = Column(String, nullable=False)
     estado = Column(String, nullable=False)
     cuenta_id = Column(Integer, ForeignKey("cuenta.id"), nullable=True)
     cuenta_grupo_id = Column(Integer, ForeignKey("cuenta_grupo.id"))

class Rol(Base):
    __tablename__ = "rol"
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True, index=True)
    tipo = Column(String, nullable=False)

    cuentas = relationship("Cuenta")

class Post(Base):
     __tablename__ = "post"
     __table_args__ = {'extend_existing': True}

     id = Column(Integer, primary_key=True, autoincrement=True)
     cuenta_id = Column(Integer, ForeignKey("cuenta.id"), nullable=True)
     evento_id = Column(Integer, ForeignKey("evento.id"), nullable=True)
     fecha_hora_create = Column(DateTime, nullable=False)
     mensaje = Column(String, nullable=False)


class Notificacion(Base):
     __tablename__ = "notificacion"
     __table_args__ = {'extend_existing': True}

     id = Column(Integer, primary_key=True, index=True)
     mensaje = Column(String, nullable=False)
     fecha_hora = Column(DateTime, nullable=False)
     post_id=Column(Integer, ForeignKey("post.id"), nullable=True)

class reaccion_Post(Base):
     __tablename__ = "reaccion_Post"
     __table_args__ = {'extend_existing': True}

     id = Column(Integer, primary_key=True, index=True)
     tipo = Column(String, nullable=False)
     reaccion = Column(String, nullable=False)
     fecha_hora = Column(DateTime, nullable=False)
     post_id = Column(Integer, ForeignKey("post.id"), nullable=True)
     cuenta_id = Column(Integer, ForeignKey("cuenta.id"), nullable=True)

class Archivo(Base):
     __tablename__ = "archivo"
     __table_args__ = {'extend_existing': True}

     id = Column(Integer, primary_key=True, index=True)
     tipo = Column(String, nullable=False)
     contenido = Column(String, nullable=False)
     url = Column(String, nullable=False)
     post_id = Column(Integer, ForeignKey("post.id"), nullable=True)


class Evento(Base):
     __tablename__ = "evento"
     __table_args__ = {'extend_existing': True}

     id = Column(Integer, primary_key=True, index=True)
     nombre = Column(String, nullable=False)
     tipo_privacidad = Column(String, nullable=False)
     fecha_hora = Column(DateTime, nullable=False)
     categoria_id = Column(Integer, ForeignKey("categoria.id"), nullable=True)
     #cuentas = relationship("Cuenta", secondary=Post, back_populates="eventos")

     # categoria = relationship("Lugar",foreign_keys=[categoria_id])


class Categoria(Base):
     __tablename__ = "categoria"
     __table_args__ = {'extend_existing': True}

     id = Column(Integer, primary_key=True, index=True)
     nombre = Column(String, nullable=False)
     # eventos = relationship()


CuentaGrupo = Table(
     "cuenta_grupo",
     Base.metadata,

     Column("id", Integer, primary_key=True, autoincrement=True),
     Column("cuenta_id", Integer, ForeignKey("cuenta.id", ondelete="CASCADE")),
     Column("grupo_id", Integer, ForeignKey("grupo.id", ondelete="CASCADE"))
     #extend_existing=True
     #Column("descripcion", String, nullable=False),
 )


class Cuenta(Base):
    __tablename__ = "cuenta"
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    nombre = Column(String, nullable=False)
    apellido = Column(String, nullable=False)
    edad = Column(Integer, nullable=False)
    sexo = Column(String, nullable=False)
    direccion = Column(String, nullable=False)
    avatar = Column(String, nullable=False)
    email = Column(String, nullable=False)
    password = Column(String, nullable=False)
    estado = Column(String, nullable=False)
    grupos = relationship("Grupo", secondary=CuentaGrupo, back_populates="cuentas")
    #eventos = relationship("Evento", secondary=Post, back_populates="cuentas")
    #chat_id = Column(Integer, ForeignKey("chat.id"), nullable=True)

    #chat_id=Column(Integer, ForeignKey("chat.id"), nullable=True)

    rol_id = Column(Integer, ForeignKey("rol.id"))


class Contacto(Base):
     __tablename__ = "contacto"
     __table_args__ = {'extend_existing': True}

     id = Column(Integer, primary_key=True, index=True)
     fecha_hora = Column(DateTime, nullable=False)
     descripcion = Column(String, nullable=False)
     cuenta_id = Column(Integer, ForeignKey("cuenta.id"), nullable=True)
    


class Grupo(Base):
     __tablename__ = "grupo"
     __table_args__ = {'extend_existing': True}

     id = Column(Integer, primary_key=True, index=True)
     nombre = Column(String, nullable=False)
     tipo = Column(String, nullable=False)
     cuentas = relationship("Cuenta", secondary=CuentaGrupo, back_populates="grupos")
