from modules.logger import log


class Dispatcher:

    def __init__(self):

        self.plugins = []


    def register(self, plugin):

        self.plugins.append(plugin)

        log(
            f"Plugin cargado: {plugin.__class__.__name__}"
        )


    def dispatch(self, event):

        for plugin in self.plugins:

            try:

                plugin.on_event(event)

            except Exception as e:

                log(
                    f"{plugin.__class__.__name__}: {e}"
                )