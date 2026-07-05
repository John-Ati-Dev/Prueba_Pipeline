import pytest

from src.organizador_archivos import obtener_categoria, organizar_archivos


def test_obtener_categoria_documento():
    assert obtener_categoria("informe.pdf") == "Documentos"


def test_obtener_categoria_imagen():
    assert obtener_categoria("foto.JPG") == "Imagenes"


def test_obtener_categoria_desconocida():
    assert obtener_categoria("archivo.xyz") == "Otros"


def test_organizar_archivos_mueve_a_subcarpetas(tmp_path):
    (tmp_path / "informe.pdf").write_text("contenido")
    (tmp_path / "foto.png").write_text("contenido")

    resumen = organizar_archivos(str(tmp_path))

    assert resumen == {"Documentos": 1, "Imagenes": 1}
    assert (tmp_path / "Documentos" / "informe.pdf").exists()
    assert (tmp_path / "Imagenes" / "foto.png").exists()


def test_organizar_archivos_directorio_inexistente():
    with pytest.raises(FileNotFoundError):
        organizar_archivos("carpeta_que_no_existe")
