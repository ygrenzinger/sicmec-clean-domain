from terminal_data_fetcher import TerminalDataFetcher
from client import Client
from event_notifier import EventNotifier
from container import Container


class TerminalDataProcessor:
    @classmethod
    def process(cls, clients, datas):
        for client in clients:
            for loaded_container in datas.get('loaded-containers', []):
                print(
                    f'loaded container {loaded_container.container_id} into {loaded_container.ship_code}')
                client.load_container_into_ship(
                    loaded_container.container_id, loaded_container.ship_code)


if __name__ == '__main__':
    event_notifier = EventNotifier()

    containers = get_containers_for_client()

    containers = {
        "1": Container("1", "SANOFI", 100),
        "2": Container("2", "SANOFI", 300)
    }

    client = Client(event_notifier, 200, containers)
    clients = [client]
    datas = TerminalDataFetcher().fetch_data()
    TerminalDataProcessor.process(clients, datas)
