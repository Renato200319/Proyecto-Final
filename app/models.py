from app import db


class Usuario(db.Model):
    #info basica
    dni = db.Column(db.String(8), unique=True, nullable=False, primary_key = True) #dni 
    name = db.Column(db.String(25), nullable=False) #nombre 
    last_name = db.Column(db.String(25), nullable=False) #apellido
    phone = db.Column(db.String(9), nullable=True) #9 digitos
    adress = db.Column(db.String(120), nullable=False) #direccion tienda fisica
    #info para register
    email = db.Column(db.String(30), unique=True, nullable=False) #correo personal
    password = db.Column(db.String(15), nullable=False) # Contraseña cifrada

    def __repr__(self):
        return '<User %r>' % self.username

class Producto(db.Model):
    p_id = db.Column(db.String(6), unique=True, nullable=False, primary_key=True) 
    p_name = db.Column(db.String(40), nullable=False) #nombre real
    p_price = db.Column(db.Float, nullable=True) #precio
    p_stock = db.Column(db.Integer, nullable=True) #stock
    p_description = db.Column(db.String(120), nullable=False) #descripcion del producto
    p_brand = db.Column(db.String(120), nullable=False) #marca del producto
    p_due_date = db.Column(db.DateTime, nullable=False) #fecha de caducidad
    def __repr__(self):
        return '<Product %r>' % self.name

class Compra(db.Model):
    c_registro = db.Column(db.DateTime, nullable=False) #fecha de registro
    c_descripcion =   db.Column(db.String(120), nullable=False) #descripcion de la compra
    p_codigo = db.Column(db.String(6), db.ForeignKey('producto.p_id'), nullable=False) #codigo del producto
    u_dni = db.Column(db.String(8), db.ForeignKey('usuario.dni'), nullable=False) #dni del usuario

    def __repr__(self):
        return '<Ventas %r>' % self.name

class Venta(db.Model):
    v_descripcion =   db.Column(db.String(120), nullable=False) #descripcion de la venta
    p_codigo = db.Column(db.String(6), db.ForeignKey('producto.p_id'), nullable=False) #codigo del producto
    u_dni = db.Column(db.String(8), db.ForeignKey('usuario.dni'), nullable=False) #dni del usuario

    def __repr__(self):
        return '<Ventas %r>' % self.name
