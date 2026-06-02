# Análisis de Dominion con Domain-Driven Design (DDD)
## 1. Dominio Principal y Subdominios
### **Dominio Principal: Gestión de Clientes**
La empresa Sky requiere una plataforma que permita administrar la información de sus clientes mediante servicios desacoplados, garantizando escalabilidad, mantenibilidad y facilidad de integración.
**Subdominios**
**Subdominio 1: Administración de Datos de Clientes**

Responsable del registro, consulta, actualización y eliminación de clientes.

**Subdominio 2: Validación de Datos**

Responsable de verificar la integridad y formato de los datos ingresados por los usuarios, incluyendo RFC, correo electrónico y número telefónico.

**Subdominio 3: Notificaciones y Auditoría**

Responsable del envío de notificaciones y del registro de eventos relevantes para auditoría y monitoreo.
