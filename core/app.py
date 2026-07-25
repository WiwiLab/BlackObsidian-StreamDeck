from core.dispatcher import Dispatcher
from core.action_engine import ActionEngine

from modules.mode_manager import ModeManager
from modules.logger import log
from core.profile_manager import ProfileManager
from core.event_handler import EventHandler
from core.plugin_loader import PluginLoader

from modules.serial_manager import SerialManager


class App:

    def __init__(self):

        self.running = True

        self.dispatcher = Dispatcher()

        self.actions = ActionEngine()

        self.mode = ModeManager()

        self.profile = ProfileManager()

        self.events = EventHandler(self)

        self.plugins = PluginLoader(self)

        # Comunicación con ESP32
        self.serial = SerialManager()

        self.serial.iniciar(
            self.events.handle
        )

        log("Aplicación cargada")


    def stop(self):

        if not self.running:
            return

        self.running = False

        # Cierra todos los plugins
        self.plugins.unload_all()

        # Detiene la comunicación serial
        self.serial.detener()

        log("Aplicación detenida")