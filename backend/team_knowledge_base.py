class TeamKnowledgeBase:
    def __init__(self):
        self.knowledge = {}

    def add_knowledge(self, topic, data):
        if topic not in self.knowledge:
            self.knowledge[topic] = []
        self.knowledge[topic].append(data)

    def query_knowledge(self, topic):
        return self.knowledge.get(topic, [])
