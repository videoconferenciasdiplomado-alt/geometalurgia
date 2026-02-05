import os

# Configuración
directorio = './' 
nuevo_bloque_css = """
/* Estilos añadidos automáticamente */
.header-content-box,
.header-compact-title,
.footer,
.section-title,
.subsection-title {
    text-wrap: balance;
}
"""

for nombre_archivo in os.listdir(directorio):
    if nombre_archivo.endswith('.html'):
        ruta = os.path.join(directorio, nombre_archivo)
        
        with open(ruta, 'r', encoding='utf-8') as f:
            contenido = f.read()
        
        # Evitar duplicados
        if ".header-content-box" in contenido and "text-wrap: balance;" in contenido:
            print(f"Saltando {nombre_archivo} (ya actualizado)")
            continue

        # Insertamos justo después de la apertura de <style>
        if "<style>" in contenido:
            nuevo_contenido = contenido.replace("<style>", f"<style>{nuevo_bloque_css}")
            
            with open(ruta, 'w', encoding='utf-8') as f:
                f.write(nuevo_contenido)
            print(f"✅ Procesado: {nombre_archivo}")
        else:
            print(f"❌ Error: {nombre_archivo} no tiene la etiqueta <style>")

print("\n¡Proceso terminado!")