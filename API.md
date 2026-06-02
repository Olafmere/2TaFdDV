# **Diseño de API REST**

## **1. Introducción**

La plataforma Sky utilizará una arquitectura basada en microservicios comunicados mediante APIs REST. Cada servicio expondrá endpoints específicos para gestionar clientes, notificaciones y auditoría.

**Formato de intercambio de datos:**

{
  "message": "Ejemplo"
}

**Tipo de contenido:**

application/json

## **2. Client Service**

Base URL:

/api/v1/clientes

### **2.1 Crear Cliente**

**Endpoint**

POST /api/v1/clientes

**Request**

{
  "nombre": "Juan Perez",
  "rfc": "PEPJ800101ABC",
  "direccion": "Ciudad de México",
  "telefono": "5512345678",
  "correo": "juan@email.com"
}

**Response 201**

{
  "idCliente": "c12345",
  "mensaje": "Cliente creado correctamente"
}

**Códigos HTTP**

| Código | Descripción |
| ------- | ------- |
| 201 | Cliente creado |
| 400 | Datos inválidos |
| 409 |	Cliente duplicado |
| 500 | Error interno |

### **2.2 Obtener Cliente por ID**

**Endpoint**

GET /api/v1/clientes/{idCliente}

**Response 200**

{
  "idCliente": "c12345",
  "nombre": "Juan Perez",
  "rfc": "PEPJ800101ABC",
  "direccion": "Ciudad de México",
  "telefono": "5512345678",
  "correo": "juan@email.com",
  "estado": "ACTIVO"
}

**Códigos HTTP**

|Código | Descripción |
| ------- | -------- |
|200 | Consulta exitosa |
|404 | Cliente no encontrado |
|500 | Error interno |

### **2.3 Listar Clientes**

**Endpoint**

GET /api/v1/clientes

**Response 200**

[
  {
    "idCliente": "c12345",
    "nombre": "Juan Perez"
  },
  {
    "idCliente": "c67890",
    "nombre": "Maria Lopez"
  }
]
**Códigos HTTP**

| Código | Descripción |
| ------- | -------- |
| 200 | Consulta exitosa |
| 500 | Error interno |

### **2.4 Actualizar Cliente**

**Endpoint**

PUT /api/v1/clientes/{idCliente}

**Request**

{
  "direccion": "Monterrey",
  "telefono": "5588889999",
  "correo": "nuevo@email.com"
}
Response 200
{
  "mensaje": "Cliente actualizado correctamente"
}

**Códigos HTTP**

| Código | Descripción |
| -------- | --------- |
| 200 | Actualización exitosa |
| 400 | Datos inválidos |
| 404 | Cliente no encontrado |
| 500 | Error interno |

### **2.5 Eliminar Cliente**

**Endpoint**

DELETE /api/v1/clientes/{idCliente}

**Response 200**

{
  "mensaje": "Cliente eliminado correctamente"
}

**Códigos HTTP**

| Código | Descripción |
| -------- | -------- |
| 200 |	Eliminación exitosa |
| 404 |	Cliente no encontrado |
| 500 |	Error interno |

## **3. Notification Service**

**Base URL:**

/api/v1/notificaciones

### 3.1 Crear Notificación

**Endpoint**

POST /api/v1/notificaciones

**Request**

{
  "idCliente": "c12345",
  "tipo": "EMAIL",
  "mensaje": "Bienvenido a Sky"
}

**Response 201**

{
  "idNotificacion": "n12345",
  "mensaje": "Notificación creada correctamente"
}

**Códigos HTTP**

| Código | Descripción |
| ------- | ------- |
| 201 |	Notificación creada |
| 400 |	Datos inválidos |
| 500 |	Error interno |

### **3.2 Consultar Notificación**

**Endpoint**

GET /api/v1/notificaciones/{idNotificacion}

**Response 200**

{
  "idNotificacion": "n12345",
  "idCliente": "c12345",
  "tipo": "EMAIL",
  "mensaje": "Bienvenido a Sky",
  "estado": "ENVIADA"
}

**Códigos HTTP**

|Código | Descripción|
| -------- | ------- |
|200 | Consulta exitosa |
|404 | Notificación no encontrada |
|500 | Error interno |

### **3.3 Listar Notificaciones**

**Endpoint**

GET /api/v1/notificaciones

**Response 200**

[
  {
    "idNotificacion": "n12345",
    "estado": "ENVIADA"
  }
]

**Códigos HTTP**

|Código | Descripción |
| ------- | ------- |
|200 | Consulta exitosa |
|500 | Error interno |

## **4. Validaciones**

**RFC**

Reglas:

- Campo obligatorio.
- Debe cumplir el formato RFC mexicano.
- No debe contener caracteres inválidos.

**Correo Electrónico**

Reglas:

- Campo obligatorio.
- Debe contener el símbolo @.
- Debe contener dominio válido.

Ejemplo:

usuario@dominio.com

**Teléfono**

Reglas:

- Campo obligatorio.
- Solo números.
- Longitud mínima de 10 dígitos.

Ejemplo:

5512345678

**Nombre**

Reglas:

-Campo obligatorio.
-Longitud mínima de 3 caracteres.
-No debe contener caracteres especiales inválidos.

Ejemplo:

Juan Perez

## **5. Manejo General de Errores**

Ejemplo de respuesta de error:

{
  "error": "Datos inválidos",
  "codigo": 400
}

Códigos utilizados:

|Código HTTP | Significado |
| -------- | -------- |
| 200 | Operación exitosa |
| 201 |	Recurso creado |
| 400 |	Solicitud inválida |
| 404 |	Recurso no encontrado |
| 409 |	Conflicto de datos |
| 500 |	Error interno del servidor |