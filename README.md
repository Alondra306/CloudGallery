# ☁️ CloudGallery: Almacenamiento en AWS S3

Este proyecto es una aplicación web desarrollada con **Python (Flask)** que permite a los usuarios cargar archivos directamente a un bucket de **Amazon S3**. La aplicación está diseñada para demostrar la integración de servicios de cómputo (EC2) con servicios de almacenamiento escalable de AWS.

##  Características
* **Carga de Archivos:** Interfaz sencilla para subir documentos e imágenes.
* **Seguridad:** Uso de **IAM Roles** (`LabInstanceProfile`) para evitar credenciales expuestas en el código.
* **Monitoreo:** Integración con **CloudWatch** para revisar el estado del servidor.
* **Gestión CLI:** Administración de objetos mediante **AWS CLI**.

## Tecnologías Utilizadas
* **Backend:** Flask (Python 3)
* **Infraestructura:** AWS EC2 (t2.micro)
* **Almacenamiento:** Amazon S3
* **SDK de AWS:** Boto3
* **Seguridad:** AWS IAM

## Estructura del Proyecto
```bash
CloudGallery/
├── app.py              # Servidor principal Flask
├── templates/          # Carpeta de plantillas HTML
│   └── index.html      # Interfaz de usuario
├── Documentacion.pdf   # Guía técnica y análisis de costos
└── README.md           # Descripción del proyecto
