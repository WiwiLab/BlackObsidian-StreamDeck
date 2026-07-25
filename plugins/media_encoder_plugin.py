import keyboard

from core.plugin import Plugin
from modules.logger import log


class MediaEncoderPlugin(Plugin):

    def on_load(self, app):

        app.actions.register(
            "media",
            self.media_action
        )

        log(
            "Media Encoder Plugin iniciado"
        )


    def media_action(self, action):

        try:

            if action == "vol_up":

                keyboard.send(
                    "volume up"
                )


            elif action == "vol_down":

                keyboard.send(
                    "volume down"
                )


            elif action == "mute":

                keyboard.send(
                    "volume mute"
                )


            elif action == "playpause":

                keyboard.send(
                    "play/pause media"
                )


        except Exception as e:

            log(
                f"Media Error: {e}"
            )