import unittest
from client import Client
from container import Container
from unittest.mock import Mock


class TestClient(unittest.TestCase):
    def setUp(self):
        self.event_notifier = Mock(
            threshold_crossed=Mock(), threshold_restored=Mock())
        containers = {
            "1": Container("1", "SANOFI", 100),
            "2": Container("2", "SANOFI", 300)
        }
        self.client = Client(self.event_notifier, 200, containers)

    def test_send_no_event_when_(self):
        self.client.load_container_into_ship("1", "le_france")
        self.event_notifier.threshold_crossed.assert_not_called()

    def test_send_ship_threshold_crossed_event(self):
        self.client.load_container_into_ship("2", "le_france")
        self.event_notifier.threshold_crossed.assert_called_once_with(
            self.client, 300)


if __name__ == '__main__':
    unittest.main()
