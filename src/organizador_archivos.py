import shutil
from pathlib import Path

# Extension -> categoria. Si una extension no aparece aqui, se usa "Otros".
CATEGORIAS = {
    ".pdf": "Documentos",
    ".docx": "Documentos",
    ".txt": "Documentos",
    ".jpg": "Imagenes",
    ".png": "Imagenes",
    ".xlsx": "HojasDeCalculo",
    ".csv": "HojasDeCalculo",
}


def obtener_categoria(nombre_archivo: str) -> str:
    """
    Devuelve la categoria de un archivo segun su extension.

    Parametros:
        nombre_archivo (str): nombre del archivo, ej. "foto.jpg".

    Retorna:
        str: categoria correspondiente, ej. "Imagenes". Si la extension
        no esta registrada, retorna "Otros".
    """
    extension = Path(nombre_archivo).suffix.lower()
    return CATEGORIAS.get(extension, "Otros")


def organizar_archivos(directorio: str) -> dict:
    """
    Mueve cada archivo de "directorio" a una subcarpeta segun su categoria.

    Parametros:
        directorio (str): carpeta cuyos archivos se van a organizar.

    Retorna:
        dict: resumen con la cantidad de archivos movidos por categoria,
        por ejemplo {"Imagenes": 2, "Documentos": 1}.

    Errores:
        FileNotFoundError: si el directorio no existe.
    """
    ruta = Path(directorio)
    if not ruta.exists():
        raise FileNotFoundError(f"El directorio no existe: {directorio}")

    resumen = {}

    for archivo in list(ruta.iterdir()):
        if archivo.is_file():
            categoria = obtener_categoria(archivo.name)
            carpeta_destino = ruta / categoria
            carpeta_destino.mkdir(exist_ok=True)
            shutil.move(str(archivo), str(carpeta_destino / archivo.name))
            resumen[categoria] = resumen.get(categoria, 0) + 1

    return resumen
