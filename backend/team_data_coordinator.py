class TeamDataCoordinator:
    def __init__(self):
        self.data_store = {}

    def store_data(self, key, data):
        self.data_store[key] = data

    def retrieve_data(self, key):
        return self.data_store.get(key)
