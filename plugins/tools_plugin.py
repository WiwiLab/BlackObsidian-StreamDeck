from core.plugin import Plugin
from modules.logger import log

import pyautogui
import subprocess


class ToolsPlugin(Plugin):

    def on_load(self, app):

        app.actions.register(
            "screenshot",
            self.screenshot
        )

        app.actions.register(
            "mute",
            self.mute
        )

        app.actions.register(
            "desktop",
            self.desktop
        )

        log(
            "Tools Plugin iniciado"
        )



    def screenshot(self, args=None):

        imagen = pyautogui.screenshot()

        imagen.save(
            "screenshot.png"
        )

        log(
            "Captura guardada"
        )



    def mute(self, args=None):

        subprocess.run(
            [
                "powershell",
                "-Command",
                "(New-Object -ComObject WScript.Shell).SendKeys([char]173)"
            ]
        )

        log(
            "Volumen cambiado"
        )



    def desktop(self, args=None):

        subprocess.run(
            [
                "powershell",
                "-Command",
                "(New-Object -ComObject Shell.Application).ToggleDesktop()"
            ]
        )

        log(
            "Mostrando escritorio"
        )