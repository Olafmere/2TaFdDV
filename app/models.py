class Cliente:
    def __init__(self, id, nombre, email, rfc, telefono):
        self.id = id
        self.nombre = nombre
        self.email = email
        self.rfc = rfc
        self.telefono = telefono

    def to_dict(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "email": self.email,
            "rfc": self.rfc,
            "telefono": self.telefono
        }