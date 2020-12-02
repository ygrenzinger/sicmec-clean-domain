
class EventNotifier:
    def __init__(self):
        pass

    def threshold_crossed(self, client, amount):
        print("threshold_crossed")

    def threshold_restored(self, client, amount):
        print("threshold_restored")
