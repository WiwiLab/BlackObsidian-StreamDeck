from datetime import datetime
from pathlib import Path

LOG_DIR = Path("logs")
LOG_DIR.mkdir(exist_ok=True)

archivo = LOG_DIR / f"{datetime.now():%Y-%m-%d}.log"


def log(msg):

    hora = datetime.now().strftime("%H:%M:%S")

    texto = f"[{hora}] {msg}"

    print(texto)

    try:

        with open(
            archivo,
            "a",
            encoding="utf-8"
        ) as f:

            f.write(texto + "\n")

    except:
        pass