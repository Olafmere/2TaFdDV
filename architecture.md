# ** Diseño de Arquitectura de Microservicios **
## **1. Descripción General**

La empresa Sky requiere una plataforma escalable basada en microservicios para la gestión de clientes, validación de datos, notificaciones y auditoría. La solución será desarrollada en Python y desplegada mediante contenedores Docker, utilizando integración y entrega continua con GitHub Actions.

La arquitectura propuesta sigue los principios de Domain-Driven Design (DDD), separando claramente las responsabilidades de cada servicio y permitiendo su escalabilidad independiente.

## **2. Arquitectura General**

**Diagrama de Arquitectura**

```mermaid
graph TD
    A[Usuario]
    B[Client Service<br/>Puerto 8000]
    C[Notification Service<br/>Puerto 8001]
    D[Auditoría y Logs]

    A --> B
    B -->|REST API| C
    C --> D
```

## **3. Microservicios Propuestos**

### **3.1 Client Service**

**Responsabilidad**

Gestionar toda la información relacionada con los clientes.

**Funciones**

-Registrar clientes.
-Consultar clientes.
-Actualizar clientes.
-Eliminar clientes.
-Validar datos de entrada.
-Solicitar generación de notificaciones.

**Puerto**

8000

**Contexto DDD**

Gestión de Clientes.

## **3.2 Notification Service**

**Responsabilidad**

Gestionar notificaciones y auditoría del sistema.

**Funciones**

-Generar notificaciones.
-Registrar eventos.
-Mantener historial de auditoría.
-Enviar mensajes a clientes.

**Puerto**

8001

**Contexto DDD**

Notificaciones y Auditoría.

## **4. Capas Internas de los Microservicios**

Cada microservicio seguirá una arquitectura en capas.

### **Capa Controller / Routes**

**Responsabilidades:**

Exponer endpoints REST.
Recibir solicitudes HTTP.
Validar parámetros básicos.

**Ejemplos:**

POST /clientes
GET /clientes/{id}

### **Capa Business Logic**

**Responsabilidades:**

-Aplicar reglas de negocio.
-Gestionar entidades y agregados.
-Ejecutar validaciones.

**Ejemplos:**

-Verificar RFC válido.
-Evitar registros duplicados.

### **Capa Data Access**

**Responsabilidades:**

-Persistencia de datos.
-Consultas a base de datos.
-Operaciones CRUD.

## **5. Comunicación Entre Servicios**

La comunicación se realizará mediante REST síncrono.

**Flujo General**

```mermaid
graph TD
    A[Cliente Service]
    B[Notification Service]

    A -->|HTTP REST| B
```
El Client Service enviará solicitudes al Notification Service cuando ocurra un evento relevante.

Ejemplo:

- Cliente creado.
- Cliente actualizado.
- Cliente eliminado.