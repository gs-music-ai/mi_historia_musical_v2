from pathlib import Path
import re

print("=" * 55)
print("🐞 INSPECTOR MURPHY v1.0")
print("=" * 55)

proyecto = Path(__file__).resolve().parent.parent

carpeta_capitulos = proyecto / "capitulos"
#print("Proyecto:", proyecto)
#print("Capítulos:", carpeta_capitulos)
#print(list(carpeta_capitulos.glob("*.py")))
carpeta_audio = proyecto / "audio"

patron = re.compile(r'st\.audio\("([^"]+)"\)')
#patron_imagen = re.compile(r'st\.image\("([^"]+)"\)')
patron_imagen = re.compile(r'st\.image\("([^"]+)"')
errores = 0
capitulos = 0
audios = 0
imagenes = 0
for archivo in sorted(carpeta_capitulos.glob("*.py")):
    capitulos += 1
    texto = archivo.read_text(encoding="utf-8")

    coincidencias = patron.findall(texto)

    for ruta in coincidencias:
        audios += 1
        archivo_audio = proyecto / ruta
        if archivo_audio.exists():

            print(f"✅ {archivo.name} -> {archivo_audio.name}")

        else:

            print(f"❌ {archivo.name}")

            print(f"    No encontré: {archivo_audio.name}")

            errores += 1

    coincidencias = patron_imagen.findall(texto)
    print(archivo.name, coincidencias)
    for ruta in coincidencias:

        imagenes += 1

        archivo_imagen = proyecto / ruta

        if archivo_imagen.exists():

            print(f"🖼️ {archivo.name} -> {archivo_imagen.name}")

        else:

            print(f"❌ {archivo.name}")

            print(f"    No encontré imagen: {archivo_imagen.name}")

            errores += 1
        
print()

if errores == 0:
    print(f"📚 Capítulos revisados : {capitulos}")
    print(f"🎵 Audios encontrados : {audios}")
    print(f"🖼️ Imágenes encontradas : {imagenes}")
    print()
    print("🎉 Proyecto consistente. No encontré problemas.")

else:

   print(f"🐞🐞 Murphy encontró {errores} travesura(s).")