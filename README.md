# **Sky Microservices Platform**

## **Descripción del Proyecto**

Sky es una empresa en expansión que requiere modernizar su infraestructura tecnológica mediante una arquitectura basada en microservicios.

Este proyecto tiene como objetivo diseñar una solución escalable para la gestión de clientes, validación de datos, notificaciones y auditoría, aplicando los principios de Domain-Driven Design (DDD), containerización con Docker y automatización mediante CI/CD.

La presente fase corresponde al análisis y diseño de la solución. La implementación en Python se realizará en etapas posteriores.

**Objetivos**

-Gestionar información de clientes mediante servicios REST desacoplados.
-Validar datos de entrada de forma consistente.
-Procesar notificaciones y auditoría de cambios.
-Escalar cada microservicio de forma independiente.
-Automatizar despliegues mediante CI/CD.
-Aplicar principios de Domain-Driven Design (DDD).

## **Arquitectura Propuesta**

La solución estará compuesta por dos microservicios principales:

## **Client Service**

Responsable de:

- Registro de clientes.
- Consulta de clientes.
- Actualización de clientes.
- Eliminación de clientes.
- Validación de datos.

Puerto planificado:

8000

## **Notification Service**

Responsable de:

- Generación de notificaciones.
- Registro de auditoría.
- Historial de eventos.
- Comunicación con otros servicios.

Puerto planificado:

8001

## **Estructura del Proyecto**

```text
sky-platform/
├── docs/
│   ├── DDD.md
│   ├── architecture.md
│   └── API.md
│
├── client-service/
│   ├── app/
│   ├── tests/
│   ├── Dockerfile
│   └── requirements.txt
│
├── notification-service/
│   ├── app/
│   ├── tests/
│   ├── Dockerfile
│   └── requirements.txt
│
├── .github/
│   └── workflows/
│       └── ci-cd.yml
│
├── docker-compose.yml
├── .gitignore
└── README.md
```