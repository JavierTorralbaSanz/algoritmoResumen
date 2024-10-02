import hashlib

print("Introduzca el resumen del archivo a buscar")
resumen=input()

encontrado=False
cont=0
while not encontrado:
    cont=cont+1
    localizacionArchivo = "/home/javier/imagen/imagen{}.jpg".format(cont)
    md5_hash = hashlib.md5()

    with open(localizacionArchivo, 'rb') as f:
        for bloque in iter(lambda: f.read(4096), b""):
            md5_hash.update(bloque)

    resumen_md5 = md5_hash.hexdigest()
    if (resumen_md5==resumen):
        encontrado=True

print(f"El archivo que buscas es {localizacionArchivo}")