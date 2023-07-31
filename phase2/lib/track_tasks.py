class TrackTasks:
    def __init__(self):
        self.tasks = []
    def add(self, task):
        self.tasks.append(task)

    def list_incomplete(self):
        # Returns: a list of incomplete tasks
        # Side-effects: none
        return self.tasks # No code here yet

    def mark_complete(self, index):
        if index < 0 or index >= len(self.tasks):
            raise Exception("No such task to mark complete")
        del self.tasks[index]
