class UIService:
    def __init__(self):
        pass

    def menu(self):
        print(
            "~~~ Ежедневник ~~~\n"
            "1. Добавить задачу\n"
            "2. Добавить личную задачу\n"
            "3. Удалить задачу\n"
            "4. Удалить личную задачу\n"
            "5. Список задач\n"
            "6. Удаленные задачи\n"
            "7. Личные задачи\n"
            "8. Задать пароль для личного доступа\n"
            "9. Планировщик задач\n"
            "10. Поиск по слову\n"
        )

    def print_add_task(self):
        print("~~~ Добавить задачу ~~~")

    def print_add_private_task(self):
        print("~~~ Добавить приватную задачу ~~~")

    def print_set_private_password(self):
        print("~~~ Установить пароль для личного списка ~~~")

    def print_user_input_is_not_valid(self, error_msg):
        print(f"Неверно введено значение: {error_msg}\n")

    def print_delete_tasks(self):
        print("~~~ Удалить задачу ~~~")

    def print_task_add_success(self, task_name, is_private_task):
        print(f'Задача "{task_name}" была успешно добавлена в {"личный список" if is_private_task else "общий список"}\n')

    def print_task_delete_success(self, deleted_task):
        print(f'Задача "{deleted_task}" была успешно удалена\n')

    def print_tasks_list_title(self):
        print("~~~ Список задач ~~~")

    def print_private_tasks_list_title(self):
        print("~~~ Список приватных задач ~~~")

    def print_deleted_tasks_list_title(self):
        print("~~~ Удаленные задачи ~~~")

    def print_planner_menu(self):
        print(
            "~~~ Планировщик задач ~~~\n"
            "1. Добавить запланированную задачу\n"
            "2. Показать все запланированные задачи\n"
        )

    def print_planned_tasks_title(self):
        print("~~~ Запланированные задачи ~~~")

    def print_elements_not_found_in_tasks_list(self):
        print("В списке задач нет элементов\n")

    def print_elements_not_found_in_deleted_tasks_list(self):
        print("В списке удаленных задач нет элементов\n")

    def password_is_not_valid(self, entered_password):
        print(f"Пароль '{entered_password}' неверный\n")