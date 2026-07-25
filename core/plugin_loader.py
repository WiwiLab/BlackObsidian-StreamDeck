from modules.logger import log


class PluginLoader:

    def __init__(self, app):

        self.app = app

        self.plugins = []


    def load(self, plugin):

        try:

            plugin.on_load(self.app)

            self.plugins.append(plugin)

            log(
                f"Plugin activo: {plugin.__class__.__name__}"
            )

        except Exception as e:

            log(
                f"Error cargando plugin: {e}"
            )


    def unload_all(self):

        for plugin in reversed(self.plugins):

            try:

                if hasattr(plugin, "on_unload"):

                    plugin.on_unload(self.app)

            except Exception as e:

                log(
                    f"Error cerrando {plugin.__class__.__name__}: {e}"
                )

        self.plugins.clear()