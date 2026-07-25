import ast
from pathlib import Path

PROJECT = Path(__file__).resolve().parent.parent

IGNORE_DIRS = {
    "__pycache__",
    ".git",
    ".venv",
    "venv"
}

# Librerías estándar de Python
try:
    import sys
    STDLIB = set(sys.stdlib_module_names)
except AttributeError:
    STDLIB = set()

# Traducción import -> paquete pip
PACKAGE_MAP = {
    "serial": "pyserial",
    "cv2": "opencv-python",
    "PIL": "Pillow",
    "pycaw": "pycaw",
    "sounddevice": "sounddevice",
    "soundfile": "soundfile",
    "numpy": "numpy",
    "keyboard": "keyboard",
    "pyautogui": "PyAutoGUI",
    "obsws_python": "obsws-python",
    "comtypes": "comtypes",
    "psutil": "psutil"
}

imports = set()

for py in PROJECT.rglob("*.py"):

    if any(p in IGNORE_DIRS for p in py.parts):
        continue

    try:
        tree = ast.parse(py.read_text(encoding="utf8"))
    except Exception:
        continue

    for node in ast.walk(tree):

        if isinstance(node, ast.Import):

            for alias in node.names:

                imports.add(alias.name.split(".")[0])

        elif isinstance(node, ast.ImportFrom):

            if node.module:

                imports.add(node.module.split(".")[0])

requirements = set()

for module in sorted(imports):

    if module in STDLIB:
        continue

    if (PROJECT / module).exists():
        continue

    requirements.add(
        PACKAGE_MAP.get(module, module)
    )

req = PROJECT / "requirements.txt"

req.write_text(
    "\n".join(sorted(requirements)),
    encoding="utf8"
)

print("requirements.txt generado.")