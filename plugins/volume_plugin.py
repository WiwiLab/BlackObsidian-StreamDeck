from core.plugin import Plugin
from modules.logger import log
import pyautogui


class ToolsPlugin(Plugin):

    def on_load(self, app):

        app.actions.register(
            "screenshot",
            self.screenshot
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