from app.models import Categoria
import app.database as db
from sqlalchemy.exc import SQLAlchemyError

import app.models as models
import app.schemas as schemas

# from uuid import uuid4 as uuid

def create_chat_sql(chat: schemas.Chat):
    try:
        ch = models.Chat(
            mensaje=chat.mensaje,
            avatar=chat.avatar,
            estado=chat.estado,
            cuenta_id= chat.cuenta_id,
            cuenta_grupo_id = chat.cuenta_grupo_id
        )
        db.session.add(ch)
        db.session.commit()
        chat.id = ch.id
        return chat
    except SQLAlchemyError as e:
        db.session.rollback()
        print(e)

def get_chat_sql():
    try:
        chat = db.session.query(models.Chat).all()
        return chat
    except SQLAlchemyError as e:
        print(e)

def update_chat_sql(uid: str, chat: schemas.Chat):
    try:
        cha_db = db.session.query(models.Chat).get(uid)
        if cha_db:
            print(chat)
            print(cha_db.__dict__)
            cha_db.mensaje = chat.mensaje or cha_db.mensaje
            cha_db.avatar = chat.avatar or cha_db.avatar
            cha_db.estado = chat.estado or cha_db.estado
            cha_db.cuenta_id = chat.cuenta_id #or cue_db.rol_id
            cha_db.cuenta_grupo_id = chat.cuenta_grupo_id

            db.session.commit()
            return schemas.Chat(id=cha_db.id, mensaje=cha_db.mensaje, avatar=cha_db.avatar, estado=cha_db.estado, cuenta_id=cha_db.cuenta_id, cuenta_grupo_id=cha_db.cuenta_grupo_id)
        return None
    except SQLAlchemyError as e:
        db.session.rollback()
        print(e)
        return None

def buscar_chat_sql(uid: str):
    try: 
        chat = db.session.query(models.Chat).get(uid)
        return chat
    except SQLAlchemyError as e:
        print(e)

def delete_chat_sql(chat_id: str):
    try:
        db.session.query(models.Chat).filter(models.Chat.id == chat_id).delete()
        db.session.commit()
        return True
    except SQLAlchemyError as e:
        print(e)
        db.session.rollback()
        return False


def create_cuenta_sql(cuenta: schemas.Cuenta):
    try:
        usu = models.Cuenta(
            nombre=cuenta.nombre,
            apellido=cuenta.apellido,
            edad=cuenta.edad,
            sexo=cuenta.sexo,
            direccion=cuenta.direccion,
            avatar=cuenta.avatar,
            email=cuenta.email,
            password=cuenta.password,
            estado=cuenta.estado,
            rol_id=cuenta.rol_id,
            #chat_id=cuenta.chat_id
        )
        db.session.add(usu)
        db.session.commit()
        return cuenta
    except SQLAlchemyError as e:
        db.session.rollback()
        print(e)

def get_cuentas_sql():
    try:
        cuentas = db.session.query(models.Cuenta).all()
        return cuentas
    except SQLAlchemyError as e:
        print(e)

def update_cuenta_sql(uid: str, cuenta: schemas.Cuenta):
    try:
        cue_db = db.session.query(models.Cuenta).get(uid)
        if cue_db:
            print(cuenta)
            print(cue_db.__dict__)
            cue_db.nombre = cuenta.nombre or cue_db.nombre
            cue_db.apellido = cuenta.apellido or cue_db.apellido
            cue_db.edad = cuenta.edad or cue_db.edad
            cue_db.sexo = cuenta.sexo or cue_db.sexo
            cue_db.direccion = cuenta.direccion or cue_db.direccion
            cue_db.avatar = cuenta.avatar or cue_db.avatar
            cue_db.email = cuenta.email or cue_db.email
            cue_db.password = cuenta.password or cue_db.password
            cue_db.estado = cuenta.estado or cue_db.estado
            cue_db.rol_id = cuenta.rol_id #or cue_db.rol_id

            db.session.commit()
            return schemas.Cuenta(id=cue_db.id, nombre=cue_db.nombre, apellido=cue_db.apellido, edad=cue_db.edad, sexo=cue_db.sexo, direccion=cue_db.direccion, avatar=cue_db.avatar, email=cue_db.email, password=cue_db.password, estado=cue_db.estado, rol_id=cue_db.rol_id)
        return None
    except SQLAlchemyError as e:
        db.session.rollback()
        print(e)
        return None

def buscar_cuenta_sql(uid: str):
    try: 
        cuentas = db.session.query(models.Cuenta).get(uid)
        return cuentas
    except SQLAlchemyError as e:
        print(e)

def delete_cuenta_sql(cuenta_id: str):
    try:
        db.session.query(models.Cuenta).filter(models.Cuenta.id == cuenta_id).delete()
        db.session.commit()
        return True
    except SQLAlchemyError as e:
        print(e)
        db.session.rollback()
        return False

def create_evento_sql(evento: schemas.Evento):
    try:
        ev = models.Evento(
            nombre=evento.nombre,
            tipo_privacidad=evento.tipo_privacidad,
            fecha_hora=evento.fecha_hora,
            categoria_id=evento.categoria_id,
        )
        db.session.add(ev)
        db.session.commit()
        evento.id = ev.id
        return evento
    except SQLAlchemyError as e:
        db.session.rollback()
        print(e)

def get_evento_sql():
    try:
        evento = db.session.query(models.Evento).all()
        return evento
    except SQLAlchemyError as e:
        print(e)

def update_evento_sql(uid: str, evento: schemas.Evento):
    try:
        eve_db = db.session.query(models.Evento).get(uid)
        if eve_db:
            print(evento)
            print(eve_db.__dict__)
            eve_db.nombre = evento.nombre or eve_db.nombre
            eve_db.tipo_privacidad = evento.tipo_privacidad or eve_db.tipo_privacidad
            eve_db.fecha_hora = evento.fecha_hora or eve_db.fecha_hora
            eve_db.categoria_id = evento.categoria_id #or cue_db.rol_id

            db.session.commit()
            return schemas.Evento(id=eve_db.id, nombre=eve_db.nombre, tipo_privacidad=eve_db.tipo_privacidad, fecha_hora=eve_db.fecha_hora, categoria_id=eve_db.categoria_id)
        return None
    except SQLAlchemyError as e:
        db.session.rollback()
        print(e)
        return None

def buscar_evento_sql(uid: str):
    try: 
        evento = db.session.query(models.Evento).get(uid)
        return evento
    except SQLAlchemyError as e:
        print(e)

def delete_evento_sql(evento_id: str):
    try:
        db.session.query(models.Evento).filter(models.Evento.id == evento_id).delete()
        db.session.commit()
        return True
    except SQLAlchemyError as e:
        print(e)
        db.session.rollback()
        return False

def create_post_sql(post: schemas.Post):
    try:
        po = models.Post(
            cuenta_id=post.cuenta_id,
            evento_id=post.evento_id,
            fecha_hora_create=post.fecha_hora_create,
            mensaje=post.mensaje,
        )
        db.session.add(po)
        db.session.commit()
        post.id = po.id
        return post
    except SQLAlchemyError as e:
        db.session.rollback()
        print(e)

def get_post_sql():
    try:
        post = db.session.query(models.Post).all()
        return post
    except SQLAlchemyError as e:
        print(e)

def update_post_sql(uid: str, post: schemas.Post):
    try:
        pot_db = db.session.query(models.Post).get(uid)
        if pot_db:
            print(post)
            print(pot_db.__dict__)
            pot_db.fecha_hora_create = post.fecha_hora_create or pot_db.fecha_hora_create
            pot_db.mensaje = post.mensaje or pot_db.mensaje
            pot_db.cuenta_id = post.cuenta_id
            pot_db.evento_id = post.evento_id #or cue_db.rol_id

            db.session.commit()
            return schemas.Post(id=pot_db.id, fecha_hora_create=pot_db.fecha_hora_create, mensaje=pot_db.mensaje, cuenta_id=pot_db.cuenta_id, evento_id=pot_db.evento_id)
        return None
    except SQLAlchemyError as e:
        db.session.rollback()
        print(e)
        return None

def buscar_post_sql(uid: str):
    try: 
        post = db.session.query(models.Post).get(uid)
        return post
    except SQLAlchemyError as e:
        print(e)

def delete_post_sql(post_id: str):
    try:
        db.session.query(models.Post).filter(models.Post.id == post_id).delete()
        db.session.commit()
        return True
    except SQLAlchemyError as e:
        print(e)
        db.session.rollback()
        return False

def create_reaccion_Post_sql(reaccion_Post: schemas.reaccion_Post):
    try:
        rea = models.reaccion_Post(
            tipo=reaccion_Post.tipo,
            reaccion=reaccion_Post.reaccion,
            fecha_hora=reaccion_Post.fecha_hora,
            post_id=reaccion_Post.post_id,
            cuenta_id=reaccion_Post.cuenta_id,
        )
        db.session.add(rea)
        db.session.commit()
        reaccion_Post.id = rea.id
        return reaccion_Post
    except SQLAlchemyError as e:
        db.session.rollback()
        print(e)

def get_reaccion_Post_sql():
    try:
        reaccion_Post = db.session.query(models.reaccion_Post).all()
        return reaccion_Post
    except SQLAlchemyError as e:
        print(e)

def update_reaccion_Post_sql(uid: str, reaccion_Post: schemas.reaccion_Post):
    try:
        rep_db = db.session.query(models.reaccion_Post).get(uid)
        if rep_db:
            print(reaccion_Post)
            print(rep_db.__dict__)
            rep_db.tipo = reaccion_Post.tipo or rep_db.tipo
            rep_db.reaccion = reaccion_Post.reaccion or rep_db.reaccion
            rep_db.fecha_hora = reaccion_Post.fecha_hora or rep_db.fecha_hora
            rep_db.post_id = reaccion_Post.post_id #or cue_db.rol_id
            rep_db.cuenta_id = reaccion_Post.cuenta_id

            db.session.commit()
            return schemas.reaccion_Post(id=rep_db.id, tipo=rep_db.tipo, reaccion=rep_db.reaccion, fecha_hora=rep_db.fecha_hora, post_id=rep_db.post_id, cuenta_id=rep_db.cuenta_id)
        return None
    except SQLAlchemyError as e:
        db.session.rollback()
        print(e)
        return None

def buscar_reaccion_Post_sql(uid: str):
    try: 
        reaccion_Post = db.session.query(models.reaccion_Post).get(uid)
        return reaccion_Post
    except SQLAlchemyError as e:
        print(e)

def delete_reaccion_Post_sql(reaccion_Post_id: str):
    try:
        db.session.query(models.reaccion_Post).filter(models.reaccion_Post.id == reaccion_Post_id).delete()
        db.session.commit()
        return True
    except SQLAlchemyError as e:
        print(e)
        db.session.rollback()
        return False

def create_notificacion_sql(notificacion: schemas.Notificacion):
    try:
        no = models.Notificacion(
            
            mensaje=notificacion.mensaje,
            fecha_hora=notificacion.fecha_hora,
            post_id=notificacion.post_id,
        )
        db.session.add(no)
        db.session.commit()
        notificacion.id = no.id
        return notificacion
    except SQLAlchemyError as e:
        db.session.rollback()
        print(e)

def get_notificacion_sql():
    try:
        notificacion = db.session.query(models.Notificacion).all()
        return notificacion
    except SQLAlchemyError as e:
        print(e)

def update_notificacion_sql(uid: str, notificacion: schemas.Notificacion):
    try:
        nof_db = db.session.query(models.Notificacion).get(uid)
        if nof_db:
            print(notificacion)
            print(nof_db.__dict__)
            nof_db.mensaje = notificacion.mensaje or nof_db.mensaje
            nof_db.fecha_hora = notificacion.fecha_hora or nof_db.fecha_hora
            nof_db.post_id = notificacion.post_id #or cue_db.rol_id

            db.session.commit()
            return schemas.Notificacion(id=nof_db.id, mensaje=nof_db.mensaje, fecha_hora=nof_db.fecha_hora, post_id=nof_db.post_id)
        return None
    except SQLAlchemyError as e:
        db.session.rollback()
        print(e)
        return None

def buscar_notificacion_sql(uid: str):
    try: 
        notificacion = db.session.query(models.Notificacion).get(uid)
        return notificacion
    except SQLAlchemyError as e:
        print(e)

def delete_notificacion_sql(notificacion_id: str):
    try:
        db.session.query(models.Notificacion).filter(models.Notificacion.id == notificacion_id).delete()
        db.session.commit()
        return True
    except SQLAlchemyError as e:
        print(e)
        db.session.rollback()
        return False

def create_categoria_sql(categoria: schemas.Categoria):
    try:
        ca = models.Categoria(
            nombre=categoria.nombre,
        )
        db.session.add(ca)
        db.session.commit()
        categoria.id = ca.id
        return categoria
    except SQLAlchemyError as e:
        db.session.rollback()
        print(e)

def get_categoria_sql():
    try:
        categoria = db.session.query(models.Categoria).all()
        return categoria
    except SQLAlchemyError as e:
        print(e)

def update_categoria_sql(uid: str, categoria: schemas.Categoria):
    try:
        cat_db = db.session.query(models.Categoria).get(uid)
        if cat_db:
            print(categoria)
            print(cat_db.__dict__)
            cat_db.nombre = categoria.nombre or cat_db.nombre

            db.session.commit()
            return schemas.Categoria(id=cat_db.id, nombre=cat_db.nombre)
        return None
    except SQLAlchemyError as e:
        db.session.rollback()
        print(e)
        return None

def buscar_categoria_sql(uid: str):
    try: 
        Categoria = db.session.query(models.Categoria).get(uid)
        return Categoria
    except SQLAlchemyError as e:
        print(e)

def delete_categoria_sql(categoria_id: str):
    try:
        db.session.query(models.Categoria).filter(models.Categoria.id == categoria_id).delete()
        db.session.commit()
        return True
    except SQLAlchemyError as e:
        print(e)
        db.session.rollback()
        return False

def create_rol_sql(rol: schemas.Rol):
    try:
        ro = models.Rol(
            tipo=rol.tipo,
        )
        db.session.add(ro)
        db.session.commit()
        rol.id = ro.id
        return rol
    except SQLAlchemyError as e:
        db.session.rollback()
        print(e)

def get_rol_sql():
    try:
        rol = db.session.query(models.Rol).all()
        return rol
    except SQLAlchemyError as e:
        print(e)

def update_rol_sql(uid: str, rol: schemas.Rol):
    try:
        roo_db = db.session.query(models.Rol).get(uid)
        if roo_db:
            print(rol)
            print(roo_db.__dict__)
            roo_db.tipo = rol.tipo or roo_db.tipo

            db.session.commit()
            return schemas.Rol(id=roo_db.id, tipo=roo_db.tipo)
        return None
    except SQLAlchemyError as e:
        db.session.rollback()
        print(e)
        return None

def buscar_rol_sql(uid: str):
    try: 
        Rol = db.session.query(models.Rol).get(uid)
        return Rol
    except SQLAlchemyError as e:
        print(e)

def delete_rol_sql(rol_id: str):
    try:
        db.session.query(models.Rol).filter(models.Rol.id == rol_id).delete()
        db.session.commit()
        return True
    except SQLAlchemyError as e:
        print(e)
        db.session.rollback()
        return False

def create_contacto_sql(contacto: schemas.Contacto):
    try:
        co = models.Contacto(
            fecha_hora=contacto.fecha_hora,
            descripcion=contacto.descripcion,
            cuenta_id=contacto.cuenta_id,
        )
        db.session.add(co)
        db.session.commit()
        contacto.id = co.id
        return contacto
    except SQLAlchemyError as e:
        db.session.rollback()
        print(e)

def get_contacto_sql():
    try:
        contacto = db.session.query(models.Contacto).all()
        return contacto
    except SQLAlchemyError as e:
        print(e)

def update_contacto_sql(uid: str, contacto: schemas.Contacto):
    try:
        con_db = db.session.query(models.Contacto).get(uid)
        if con_db:
            print(contacto)
            print(con_db.__dict__)
            con_db.fecha_hora = contacto.fecha_hora or con_db.fecha_hora
            con_db.descripcion = contacto.descripcion or con_db.descripcion
            con_db.cuenta_id = contacto.cuenta_id

            db.session.commit()
            return schemas.Contacto(id=con_db.id, fecha_hora=con_db.fecha_hora, descripcion=con_db.descripcion, cuenta_id=con_db.cuenta_id)
        return None
    except SQLAlchemyError as e:
        db.session.rollback()
        print(e)
        return None

def buscar_contacto_sql(uid: str):
    try: 
        Contacto = db.session.query(models.Contacto).get(uid)
        return Contacto
    except SQLAlchemyError as e:
        print(e)

def delete_contacto_sql(contacto_id: str):
    try:
        db.session.query(models.Contacto).filter(models.Contacto.id == contacto_id).delete()
        db.session.commit()
        return True
    except SQLAlchemyError as e:
        print(e)
        db.session.rollback()
        return False

def create_archivo_sql(archivo: schemas.Archivo):
    try:
        ar = models.Archivo(
            tipo=archivo.tipo,
            contenido=archivo.contenido,
            url=archivo.url,
            post_id=archivo.post_id,
        )
        db.session.add(ar)
        db.session.commit()
        archivo.id = ar.id
        return archivo
    except SQLAlchemyError as e:
        db.session.rollback()
        print(e)

def get_archivo_sql():
    try:
        archivo = db.session.query(models.Archivo).all()
        return archivo
    except SQLAlchemyError as e:
        print(e)

def update_archivo_sql(uid: str, archivo: schemas.Archivo):
    try:
        arc_db = db.session.query(models.Archivo).get(uid)
        if arc_db:
            print(archivo)
            print(arc_db.__dict__)
            arc_db.tipo = archivo.tipo or arc_db.tipo
            arc_db.contenido = archivo.contenido or arc_db.contenido
            arc_db.url = archivo.url or arc_db.url
            arc_db.post_id = archivo.post_id

            db.session.commit()
            return schemas.Contacto(id=arc_db.id, tipo=arc_db.tipo, contenido=arc_db.contenido, url=arc_db.url, post_id=arc_db.post_id)
        return None
    except SQLAlchemyError as e:
        db.session.rollback()
        print(e)
        return None

def buscar_archivo_sql(uid: str):
    try: 
        Archivo = db.session.query(models.Archivo).get(uid)
        return Archivo
    except SQLAlchemyError as e:
        print(e)

def delete_archivo_sql(archivo_id: str):
    try:
        db.session.query(models.Archivo).filter(models.Archivo.id == archivo_id).delete()
        db.session.commit()
        return True
    except SQLAlchemyError as e:
        print(e)
        db.session.rollback()
        return False

def create_grupo_sql(grupo: schemas.Grupo):
    try:
        usu = models.Grupo(
            nombre=grupo.nombre,
            tipo=grupo.tipo,
        )
        usu.cuentas.extend([models.Cuenta(**ev.dict()) for ev in grupo.cuentas])
        db.session.add(usu)
        db.session.commit()
        #print(usu.dict)
        return grupo
    except SQLAlchemyError as e:
        db.session.rollback()
        print(e)


def get_grupos_sql():
    try:
        grupo = db.session.query(models.Grupo).all()
        return grupo
    except SQLAlchemyError as e:
        print(e)



def update_grupo_sql(uid: str, grupo: schemas.Grupo):
    try:
        gru_db = db.session.query(models.Grupo).get(uid)
        if gru_db:
            print(grupo)
            print(gru_db._dict_)
            gru_db.nombre = grupo.nombre or gru_db.nombre
            gru_db.tipo = grupo.tipo or gru_db.tipo
           

            db.session.commit()
            return schemas.Grupo(id=gru_db.id, nombre=gru_db.nombre, tipo=gru_db.tipo)
        return None
    except SQLAlchemyError as e:
        db.session.rollback()
        print(e)
        return None


def buscar_grupo_sql(uid: str):
    try:
        
        grupo = db.session.query(models.Grupo).get(uid)
        return grupo
    except SQLAlchemyError as e:
        print(e)

def delete_grupo_sql(grupo_id: str):
    try:
        db.session.query(models.Grupo).filter(models.Grupo.id == grupo_id).delete()
        db.session.commit()
        return True
    except SQLAlchemyError as e:
        print(e)
        db.session.rollback()
        return False

def login_sql(usuario: schemas.Cuenta):
    try:
        usu = models.Empleado(email=usuario.email, password=usuario.password)
        db.session.add(usu)
        db.session.commit()
        return schemas.Empleado(email=usu.email, password=usu.password)
    except SQLAlchemyError as e:
        db.session.rollback()
        print(e)
