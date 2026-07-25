"""
BlackObsidian Studios StreamDeck
Main Launcher
"""

from core.app import App
from modules.logger import log
from plugins.audio_plugin import AudioPlugin
from plugins.obs_plugin import OBSPlugin
from plugins.recorder_plugin import RecorderPlugin
from plugins.launcher_plugin import LauncherPlugin
from modules.app_scanner import scan
from plugins.tools_plugin import ToolsPlugin
from plugins.keyboard_plugin import KeyboardPlugin
from plugins.media_encoder_plugin import MediaEncoderPlugin


def main():

    log("===================================")
    log(" BlackObsidian Studios StreamDeck ")
    log("===================================")

    scan()

    app = App()

    # Load plugins
    audio_plugin = AudioPlugin()
    app.plugins.load(audio_plugin)

    obs_plugin = OBSPlugin()
    app.plugins.load(obs_plugin)

    recorder_plugin = RecorderPlugin()
    app.plugins.load(recorder_plugin)

    launcher_plugin = LauncherPlugin()
    app.plugins.load(launcher_plugin)

    tools_plugin = ToolsPlugin()
    app.plugins.load(tools_plugin)

    keyboard_plugin = KeyboardPlugin()
    app.plugins.load(keyboard_plugin)

    media_plugin = MediaEncoderPlugin()
    app.plugins.load(media_plugin)
    

    log("Sistema iniciado")

    try:

        while app.running:

            comando = input("> ")

            app.events.handle(comando)

    except KeyboardInterrupt:

        log("Cerrando StreamDeck")

        app.stop()


if __name__ == "__main__":

    main()