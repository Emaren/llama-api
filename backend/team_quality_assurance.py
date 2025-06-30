class TeamQualityAssurance:
    def __init__(self):
        self.issues = []

    def report_issue(self, issue):
        self.issues.append(issue)

    def get_issues(self):
        return self.issues

    def clear_issues(self):
        self.issues.clear()
