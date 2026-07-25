import subprocess
import sys
from pathlib import Path
import importlib.util

PACKAGE_IMPORT = {
    "PyAutoGUI": "pyautogui",
    "opencv-python": "cv2",
    "pyserial": "serial",
    "obsws-python": "obsws_python"
}

req = Path("requirements.txt")

if not req.exists():

    print("No existe requirements.txt")

    quit()

for package in req.read_text().splitlines():

    package = package.strip()

    if not package:
        continue

    module = PACKAGE_IMPORT.get(package, package)

    if importlib.util.find_spec(module):

        print(f"✔ {package}")

    else:

        print(f"Instalando {package}...")

        subprocess.check_call([
            sys.executable,
            "-m",
            "pip",
            "install",
            package
        ])

print("\nTodo listo.")