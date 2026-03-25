class TasksPrivateService:

    def __init__(self):
        self.password = None
        self.private_tasks = []

    def set_password(self, password):
        self.password = password

    def add_private_task(self, name_task, entered_password):
        if not self.valid_password(entered_password):
            return False
        self.private_tasks.append(name_task)
        return True

    def delete_private_task(self, index):
        if index < 0 or index >= len(self.private_tasks):
            return None
        return self.private_tasks.pop(index)

    def get_private_task_list(self, entered_password):
        if not self.valid_password(entered_password):
            return None
        return list(self.private_tasks)

    def valid_password(self, entered_password):
        return self.password is not None and entered_password == self.password