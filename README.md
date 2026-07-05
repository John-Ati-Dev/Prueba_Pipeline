# Taller de Automatización — Organizador de Archivos

Proyecto para el taller "Caso Práctico – Estrategia de Automatización"
(Maestría en Ingeniería en Software, UNEMI).

## Proceso automatizado

Un script que organiza los archivos de una carpeta (por ejemplo, la carpeta
de Descargas) moviéndolos automáticamente a subcarpetas según su tipo:
`Documentos`, `Imagenes`, `HojasDeCalculo` u `Otros` si la extensión no está
registrada.

##  Pruebas unitarias

En `tests/test_organizador_archivos.py`, usando `pytest` y la fixture
`tmp_path`:

- clasificación correcta para documentos, imágenes y extensiones
  desconocidas;
- que `organizar_archivos` mueva los archivos a las subcarpetas correctas;
- que se lance `FileNotFoundError` si la carpeta no existe.

Ejecutar localmente:

```bash
pip install -r requirements.txt
pytest -v
```

## Parte 4 — Automatización con GitHub Actions

El workflow `.github/workflows/python-ci.yml` se ejecuta en cada `push` o
`pull request` a `main`/`master`, y:

1. instala Python 3.10;
2. instala dependencias (`requirements.txt`);
3. ejecuta `pytest -v`;
4. muestra el resultado de las pruebas en el log de Actions.
