from modules.logger import log


class ActionEngine:

    def __init__(self):

        self.actions = {}

        log("Action Engine iniciado")


    def register(self, name, function):

        self.actions[name] = function

        log(
            f"Acción registrada: {name}"
        )


    def execute(self, action):

        if ":" in action:

            name, value = action.split(":", 1)

        else:

            name = action
            value = None


        if name not in self.actions:

            log(
                f"Acción desconocida: {name}"
            )

            return False


        try:

            if value:

                self.actions[name](value)

            else:

                self.actions[name]()


            return True


        except Exception as e:

            log(
                f"Error ejecutando {action}: {e}"
            )

            return False