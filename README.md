# 📄 Analizador de Archivos de Texto (Fork Mejorado)
Aplicación web en Flask para análisis de archivos de texto con nuevas funcionalidades y mejoras. Fork del proyecto original con características adicionales.

## 🌟 Características agregadas

### Nuevas Funcionalidades
- 🕒 **Historial de análisis**:
  - Muestra los últimos 10 archivos analizados
  - Detalles por archivo:
    - 📛 Nombre del archivo
    - 📆 Fecha y hora de análisis
    - 📦 Tipo de archivo
    - ⚖️ Peso del archivo

## 🛠 Estructura Actualizada del Proyecto

```
analizador_archivos/
├── app.py                # Nueva lógica de historial
├── static/
│   └── css/
│       └── styles.css    
├── templates/
│   ├── index.html        # Nueva sección de historial + estilos
│   └── resultado.html    
└── uploads/              
└── analysis_history.json       # Almacenamiento de registros (nuevo)
```

## 🚧 Futuras Mejoras Planeadas

### Próximas Características
- 🔎 Búsqueda en historial
- 📈 Gráficos estadísticos interactivos
- 🗑️ Opción para borrar registros del historial
- 📤 Exportar historial completo a CSV


## 🌐 Cómo Acceder y Usar el Historial

El panel de historial está disponible directamente en la página principal:
1. Sube un archivo para análisis
2. Desplázate hacia abajo en la página inicial
3. Encuentra la sección "Mostrar Historial"
4. Visualiza detalles de análisis anteriores
5. Los registros se actualizan automáticamente