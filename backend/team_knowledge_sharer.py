class TeamKnowledgeSharer:
    def __init__(self):
        self.knowledge_base = {}

    def add_knowledge(self, topic, info):
        self.knowledge_base[topic] = info

    def get_knowledge(self, topic):
        return self.knowledge_base.get(topic)
