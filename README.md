# 📄 Analizador de Archivos de Texto
Una aplicación web desarrollada en Flask que analiza archivos de texto, mostrando sus metadatos y estadísticas de contenido, con interfaz optimizada para móviles.

## 🌟 Características principales

- 🔍 Analiza cualquier archivo de texto
- 📊 Proporciona información detallada:
  - 📝 Extensión y tamaño del archivo
  - 📅 Fecha de creación
  - 📈 Estadísticas de contenido (líneas, palabras, caracteres)
- 📥 Genera un resumen descargable
- 📱 Interfaz responsive optimizada para móviles
- 🎨 Diseño moderno con CSS personalizado

## 🚀 Instalación y uso

### Requisitos previos
- Python 3.8+
- pip (Gestor de paquetes de Python)

### Pasos para ejecutar

1. **Clonar el repositorio**
   ```bash
   git clone https://github.com/P13tr0/Mis-Proyectos.git analizador-archivos
   cd analizador-archivos
   ```

2. **Instalar dependencias**
   ```bash
   pip install flask werkzeug
   ```

3. **Ejecutar la aplicación**
   ```bash
   python app.py
   ```

4. **Acceder desde el navegador**
   - Computadora: `http://localhost:5000`
   - Teléfono (misma red WiFi): `http://<ip-local>:5000`

## 🛠 Estructura del proyecto

```
analizador_archivos/
├── app.py                # Aplicación principal Flask
├── static/
│   └── css/
│       └── styles.css    # Estilos CSS personalizados
├── templates/
│   ├── index.html        # Página de inicio
│   └── resultado.html    # Página de resultados
└── uploads/              # Directorio para archivos subidos
```

--------------

## 🌐 Cómo acceder desde diferentes dispositivos

### En la misma red local:
1. Conecta todos los dispositivos a la misma red WiFi
2. Ejecuta la aplicación con:
   ```bash
   python app.py
   ```
3. Accede desde otros dispositivos usando la IP de tu computadora:
   ```
   http://<tu-ip-local>:5000
   ```

### Desde cualquier lugar usando ngrok:
1. Descarga ngrok desde https://ngrok.com/download
2. Ejecuta:
   ```bash
   ./ngrok http 5000
   ```
3. Comparte la URL generada (ej: `https://abcd1234.ngrok.io`)
