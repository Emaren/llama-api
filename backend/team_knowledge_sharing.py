class TeamKnowledgeSharing:
    def __init__(self):
        self.shared_knowledge = {}

    def share(self, topic, info):
        if topic not in self.shared_knowledge:
            self.shared_knowledge[topic] = []
        self.shared_knowledge[topic].append(info)

    def retrieve(self, topic):
        return self.shared_knowledge.get(topic, [])
