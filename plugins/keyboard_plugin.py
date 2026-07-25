import keyboard

from core.plugin import Plugin
from modules.logger import log


class KeyboardPlugin(Plugin):

    def on_load(self, app):

        app.actions.register(
            "shortcut",
            self.shortcut
        )

        log(
            "Keyboard Plugin iniciado"
        )


    def shortcut(self, keys):

        try:

            keyboard.send(keys)

            log(
                f"Shortcut ejecutado: {keys}"
            )

        except Exception as e:

            log(
                f"Error shortcut: {e}"
            )