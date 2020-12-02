import unittest
from event_notifier import EventNotifier


class TestEventNotifier(unittest.TestCase):
    def setUp(self):
        self.event_notifier = EventNotifier()

    def test_threshold_crossed(client, amount):
        pass
