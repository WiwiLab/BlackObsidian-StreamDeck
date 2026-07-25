import json
import os

from pathlib import Path

from modules.logger import log


PROGRAMAS = {

    "operagx": [
        "opera.exe",
        "launcher.exe"
    ],

    "discord": [
        "Discord.exe",
        "Update.exe"
    ],

    "obs": [
        "obs64.exe"
    ],

    "davinci": [
        "Resolve.exe"
    ],

    "inventor": [
        "Inventor.exe"
    ],

    "lunar": [
        "Lunar Client.exe",
        "Lunar Client-Qt.exe"
    ],

    "word": [
        "WINWORD.EXE"
    ],

    "excel": [
        "EXCEL.EXE"
    ]

}


CARPETAS = [

    os.environ.get("ProgramFiles", ""),

    os.environ.get("ProgramFiles(x86)", ""),

    os.environ.get("LOCALAPPDATA", ""),

    os.environ.get("APPDATA", "")

]


def cargar_apps():

    archivo = Path("config/apps.json")

    if not archivo.exists():

        return {}


    with open(

        archivo,

        encoding="utf-8"

    ) as f:

        return json.load(f)



def necesita_busqueda(apps):

    for nombre in PROGRAMAS:

        if nombre not in apps:

            return True


        ruta = apps[nombre]


        if not Path(ruta).exists():

            return True


    return False



def buscar():

    encontrados = {}


    for carpeta in CARPETAS:

        if not carpeta:
            continue


        carpeta = Path(carpeta)


        if not carpeta.exists():
            continue


        for raiz, _, archivos in os.walk(carpeta):

            for archivo in archivos:


                for nombre, ejecutables in PROGRAMAS.items():


                    if archivo in ejecutables:


                        ruta = str(
                            Path(raiz) / archivo
                        )


                        ruta_lower = ruta.lower()


                        # Evita falsos positivos de launcher.exe

                        if nombre == "operagx":

                            if (
                                "opera" not in ruta_lower
                                and "opera gx" not in ruta_lower
                            ):

                                continue



                        if nombre not in encontrados:


                            encontrados[nombre] = ruta


                            log(
                                f"Encontrado: {nombre}"
                            )



    return encontrados



def guardar(nuevos):

    archivo = Path("config/apps.json")

    apps = cargar_apps()


    for nombre, ruta in nuevos.items():

        if (
            nombre not in apps
            or not Path(apps[nombre]).exists()
        ):

            apps[nombre] = ruta



    with open(

        archivo,

        "w",

        encoding="utf-8"

    ) as f:


        json.dump(

            apps,

            f,

            indent=4,

            ensure_ascii=False

        )



    log(
        "apps.json actualizado"
    )



def scan():

    apps = cargar_apps()


    if not necesita_busqueda(apps):

        log(
            "Escáner: configuración actual válida"
        )

        return apps



    log(
        "Escaneando aplicaciones..."
    )


    encontrados = buscar()


    guardar(
        encontrados
    )


    return encontrados