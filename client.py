from enum import Enum


class ThresholdStatus(Enum):
    SAFE = 1
    CROSSED = 2


class LocationState:
    def __init__(self, containers, threshold_status):
        self.containers = containers
        self.threshold_status = threshold_status

    def __str__(self):
        return f'Containers {self.containers} and status {self.threshold_status}'

    def amount(self):
        return sum([c.amount for c in self.containers])


class Client:
    def __init__(self, event_notifier, ship_threshold, followed_containers={}):
        self.event_notifier = event_notifier
        self.ship_threshold = ship_threshold
        self.location_state_by_ship = {}
        self.followed_containers = followed_containers

    def __str__(self):
        return f'Client ship_threshold {self.ship_threshold} location_state_by_ship {self.location_state_by_ship}'

    def is_concerned_by(self, container_id):
        return container_id in self.followed_containers

    def load_container_into_ship(self, container_id, ship_code):
        if not self.is_concerned_by(container_id):
            return

        location_state = self.get_location_state_by_ship(ship_code)
        container = self.followed_containers[container_id]

        location_state.containers.add(container)
        if location_state.threshold_status == ThresholdStatus.SAFE and location_state.amount() > self.ship_threshold:
            self.event_notifier.threshold_crossed(
                self, location_state.amount())
        elif location_state.threshold_status == ThresholdStatus.CROSSED and location_state.amount() <= self.ship_threshold:
            self.event_notifier.threshold_restored(
                self, location_state.amount())

        self.location_state_by_ship[ship_code] = location_state

    def get_location_state_by_ship(self, ship_code):
        location_state = self.location_state_by_ship.get(ship_code)
        if location_state is None:
            return LocationState(set(), ThresholdStatus.SAFE)
        else:
            return location_state
