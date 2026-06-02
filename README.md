# **Sky Microservices Platform**

## **Descripción del Proyecto**

Sky es una empresa en expansión que requiere modernizar su infraestructura tecnológica mediante una arquitectura basada en microservicios.

Este proyecto tiene como objetivo diseñar una solución escalable para la gestión de clientes, validación de datos, notificaciones y auditoría, aplicando los principios de Domain-Driven Design (DDD), containerización con Docker y automatización mediante CI/CD.

La presente fase corresponde al análisis y diseño de la solución. La implementación en Python se realizará en etapas posteriores.

## **Objetivos**

- Gestionar información de clientes mediante servicios REST desacoplados.
- Validar datos de entrada de forma consistente.
- Procesar notificaciones y auditoría de cambios.
- Escalar cada microservicio de forma independiente.
- Automatizar despliegues mediante CI/CD.
- Aplicar principios de Domain-Driven Design (DDD).

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

## **Tecnologías Planificadas**

### **Backend**

- Python 3.12
- FastAPI
- Pydantic

### **Contenedores**

- Docker
- Docker Compose

### **Control de Versiones**

- Git
- GitHub

### **Integración Continua**

- GitHub Actions

## **Estrategia GitFlow**

Se utilizará una estrategia simplificada basada en GitFlow.

### **Rama Main**

Contendrá únicamente versiones estables listas para producción.

main

### **Rama Develop**

Contendrá el código integrado para pruebas.

develop

### **Ramas Feature**

Utilizadas para el desarrollo de nuevas funcionalidades.

Ejemplos:

- feature/client-service
- feature/notification-service
- feature/api-validation

## **Flujo de Trabajo**

1. Crear una rama feature desde develop.
2. Implementar cambios.
3. Realizar pruebas.
4. Crear Pull Request.
5. Revisar y aprobar cambios.
6. Integrar en develop.
7. Fusionar en main cuando la versión sea estable.

## **Estrategia CI/CD**

La automatización se realizará mediante GitHub Actions.

**Pipeline Planificado**

**Job 1: Lint**

Objetivo:

- Verificar calidad de código.
- Aplicar estándares de estilo.

Herramientas previstas:

- flake8
- black

**Job 2: Test**

Objetivo:

- Ejecutar pruebas unitarias.
- Validar funcionamiento básico.

Herramientas previstas:

- pytest

**Job 3: Build**

Objetivo:

- Construir imágenes Docker.
- Verificar que los contenedores puedan generarse correctamente.

**Job 4: Deploy (Futuro)**

Objetivo:

- Desplegar automáticamente la solución en el entorno definido.

## **Docker**

**Contenedores Planificados**

**Client Service**

Puerto:

8000

**Notification Service**

Puerto:

8001

**Red Docker**

Se utilizará una red dedicada:

sky-network

Permitiendo la comunicación interna entre los microservicios.

## **Ejecución Futura**

Una vez implementada la solución, la ejecución prevista será:

docker-compose up --build

Los servicios estarán disponibles en:

http://localhost:8000
http://localhost:8001

## **Estado del Proyecto**

Fase actual:

Diseño y Planificación

Próxima fase:

Implementación de microservicios en Python
Containerización con Docker
Automatización CI/CD