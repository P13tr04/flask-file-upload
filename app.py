from flask import Flask, render_template, request, send_file
import os
import json
from datetime import datetime
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB
HISTORY_FILE = 'analysis_history.json'
MAX_HISTORY = 10

def cargar_historial():
    """Carga el historial desde el archivo JSON"""
    try:
        with open(HISTORY_FILE, 'r') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def guardar_historial(historial):
    """Guarda el historial en el archivo JSON"""
    with open(HISTORY_FILE, 'w') as f:
        json.dump(historial[:MAX_HISTORY], f, indent=2)

# Crear directorios necesarios
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

def analizar_archivo(ruta_archivo):
    """Analiza el archivo y devuelve sus datos"""
    nombre = os.path.basename(ruta_archivo)
    nombre_base, extension = os.path.splitext(nombre)
    peso = os.path.getsize(ruta_archivo)
    fecha_creacion = datetime.fromtimestamp(os.path.getctime(ruta_archivo)).strftime('%Y-%m-%d %H:%M:%S')
    
    num_lineas = num_palabras = num_caracteres = 0
    
    with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
        for linea in archivo:
            num_lineas += 1
            num_caracteres += len(linea)
            num_palabras += len(linea.split())
    
    return {
        'nombre': nombre,
        'extension': extension,
        'peso_bytes': peso,
        'peso_kb': round(peso/1024, 2),
        'fecha_creacion': fecha_creacion,
        'num_lineas': num_lineas,
        'num_palabras': num_palabras,
        'num_caracteres': num_caracteres
    }

def generar_resumen(resultado):
    """Genera el contenido del archivo de resumen"""
    return f"""=== RESUMEN DE ANÁLISIS ===

 Archivo: {resultado['nombre']}
 Extensión: {resultado['extension']}
 Tamaño: {resultado['peso_kb']} KB ({resultado['peso_bytes']} bytes)
 Fecha de creación: {resultado['fecha_creacion']}

 ESTADÍSTICAS:
→ Líneas: {resultado['num_lineas']}
→ Palabras: {resultado['num_palabras']}
→ Caracteres: {resultado['num_caracteres']}"""

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'archivo' not in request.files:
            return render_template('index.html', error=" No se seleccionó ningún archivo")
            
        archivo = request.files['archivo']
        
        if archivo.filename == '':
            return render_template('index.html', error=" El archivo está vacío")
        
        if archivo:
            filename = secure_filename(archivo.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            archivo.save(filepath)
            
            try:
                resultado = analizar_archivo(filepath)
                nombre_salida = request.form.get('nombre_salida', 'resumen.txt')

                if not nombre_salida.endswith('.txt'):
                    nombre_salida += '.txt'

                resumen_path = os.path.join(app.config['UPLOAD_FOLDER'], nombre_salida)
                with open(resumen_path, 'w', encoding='utf-8') as f:
                    f.write(generar_resumen(resultado))

                # Registrar en historial
                historial = cargar_historial()
                historial.insert(0, {
                    'nombre': resultado['nombre'],
                    'fecha': datetime.now().isoformat(),
                    'tamaño': resultado['peso_kb'],
                    'tipo': resultado['extension']
                })
                guardar_historial(historial)

                return render_template('resultado.html', 
                                    resultado=resultado,
                                    archivo_resumen=nombre_salida,
                                    historial=historial[:10])  # Mostrar últimos 10 en vista rápida

            except Exception as e:
                return render_template('index.html', error=f" Error: {str(e)}")

    return render_template('index.html', historial=cargar_historial()[:10])

@app.route('/descargar/<filename>')
def descargar(filename):
    path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    return send_file(path, as_attachment=True)

@app.route('/historial')
def ver_historial():
    historial = cargar_historial()
    print(f"Cargando Historial: {historial}")
    return render_template('historial.html', historial=historial)

# ========== FILTROS TEMPLATE ==========
@app.template_filter('datetime_format')
def format_datetime(iso_fecha):
    try:
        dt = datetime.fromisoformat(iso_fecha)
        return datetime.fromisoformat(iso_fecha).strftime('%d/%m/%Y %H:%M')
    except:
        return iso_fecha

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
