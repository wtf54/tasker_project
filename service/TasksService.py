class TasksService:
    """
    
    """
    
    def __init__(self):

        self.tasks = []
        self.deleted_tasks = []
        self.planned_tasks = []

    def add_task(self, name_task: str):
        self.tasks.append(name_task)

    def delete_task(self, index_task: int):
        if index_task < 0 or index_task >= len(self.tasks):
            return None
        deleted_task = self.tasks.pop(index_task)
        self.deleted_tasks.append(deleted_task)
        return deleted_task

    def get_task_list(self):
        return list(self.tasks)

    def find_tasks(self, word):
        w = word.lower()
        return [i for i in self.tasks if w in i.lower()]

    def get_deleted_task_list(self):
        return list(self.deleted_tasks)

    def add_planned_task(self, name_task: str, due_date: str):
        self.planned_tasks.append({"name": name_task, "due_date": due_date})

    def get_planned_tasks(self):
        return list(self.planned_tasks)
