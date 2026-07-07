from pathlib import Path
import re

print("=" * 55)
print("🐞 INSPECTOR MURPHY v1.0")
print("=" * 55)

proyecto = Path(__file__).resolve().parent.parent

carpeta_capitulos = proyecto / "capitulos"
print("Proyecto:", proyecto)
print("Capítulos:", carpeta_capitulos)
print(list(carpeta_capitulos.glob("*.py")))
carpeta_audio = proyecto / "audio"

patron = re.compile(r'st\.audio\("([^"]+)"\)')

errores = 0
capitulos = 0
audios = 0
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

print()

if errores == 0:
    print(f"📚 Capítulos revisados : {capitulos}")
    print(f"🎵 Audios encontrados : {audios}")
    print()
    print("🎉 Todos los audios existen.")

else:

    print(f"🐞 Encontré {errores} problema(s).")