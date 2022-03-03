import pyfirmata


class Connection:
    port: str
    connection: pyfirmata.Arduino

    def __init__(self, port: str):
        self.set_port(port)
        self.connection = pyfirmata.Arduino(port)

    @property
    def get_port(self) -> str:
        return self.port

    def set_port(self, port: str):
        self.port = port
        self.connection = pyfirmata.Arduino(port)

    @property
    def get_connection(self) -> object:
        return self.connection

    def exit(self) -> None:
        self.connection.exit()
