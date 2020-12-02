from container import Container


class LoadedContainer:
    def __init__(self, container_id, ship_code):
        self.container_id = container_id
        self.ship_code = ship_code


class TerminalDataFetcher:
    def fetch_data(self):

        return {
            'loaded-containers': [
                LoadedContainer("1", "le_france"),
                LoadedContainer("2", "le_france")
            ]
        }
