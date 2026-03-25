from base.Controller import Controller
from service.TasksPrivateService import TasksPrivateService
from service.TasksService import TasksService
from service.UIService import UIService


class InputUserController(Controller):
    def __init__(self):
        self.tasks_private_service = TasksPrivateService()
        self.ui_service = UIService()
        self.tasks_service = TasksService()

    def start_handle_user_input(self):
        while True:
            self.ui_service.menu()
            choice = input("Что вы хотите сделать?: ")
            match choice:
                case "1":
                    self.handle_add_task()
                case "2":
                    self.handle_add_private_task()
                case "3":
                    self.handle_remove_task()
                case "4":
                    self.handle_remove_private_task()
                case "5":
                    self.handle_show_tasks()
                case "6":
                    self.handle_show_deleted_tasks()
                case "7":
                    self.handle_show_private_tasks()
                case "8":
                    self.handle_set_private_password()
                case "9":
                    self.handle_planner()
                case "10":
                    self.handle_search_tasks()
                case _:
                    print("Нет такого варианта! Попробуйте еще раз!")

    def handle_show_tasks(self):
        
        self.ui_service.print_tasks_list_title()

        list_tasks = self.tasks_service.get_task_list()

        if len(list_tasks) == 0:
            self.ui_service.print_elements_not_found_in_tasks_list()
            return False

        for k, v in enumerate(list_tasks):
            print(f"{k} - {v}")

        return None



    def handle_remove_task(self):
        if self.handle_show_tasks() is False:
            return

        try:
            index_task = int(input("Введите индекс задачи: "))

            if not self.tasks_service.delete_task(index_task):
                print("Ошибка при удалении задачи!")

        except ValueError:
            self.ui_service.print_user_input_is_not_valid("Нужно ввести число")



    def handle_add_task(self):
        self.ui_service.print_add_task()
        task = input("Введите название задачи: ")

        if not self.valid_str(task):
            self.ui_service.print_user_input_is_not_valid("Название задачи не соотвествует нормам!")
            return
        self.tasks_service.add_task(task)
        self.ui_service.print_task_add_success(task, is_private_task=False)



    def handle_add_private_task(self):
        self.ui_service.print_add_private_task()
        private_task = input("Введите название приватной задачи: ")
        user_password = input("Введите пароль: ")

        if not self.valid_str(private_task):
            self.ui_service.print_user_input_is_not_valid("Название приватной задачи не соотвествует нормам!")
            return

        if not self.valid_str(user_password):
            self.ui_service.print_user_input_is_not_valid("Пароль не соответствует нормам")
            return

        ok = self.tasks_private_service.add_private_task(private_task, user_password)
        if not ok:
            self.ui_service.password_is_not_valid(user_password)
            return

        self.ui_service.print_task_add_success(private_task, is_private_task=True)



    def handle_show_private_tasks(self):
        self.ui_service.print_private_tasks_list_title()

        entered_password = input("Введите пароль для доступа к личным задачам: ")
        private_list_tasks = self.tasks_private_service.get_private_task_list(entered_password)

        if private_list_tasks is None:
            self.ui_service.password_is_not_valid(entered_password)
            return False

        if len(private_list_tasks) == 0:
            self.ui_service.print_elements_not_found_in_tasks_list()
            return False

        for k, v in enumerate(private_list_tasks):
            print(f"{k} - {v}")

        return None



    def handle_remove_private_task(self):
        self.ui_service.print_private_tasks_list_title()

        entered_password = input("Введите пароль для доступа к личным задачам: ")
        private_list_tasks = self.tasks_private_service.get_private_task_list(entered_password)

        if private_list_tasks is None:
            self.ui_service.password_is_not_valid(entered_password)
            return

        if len(private_list_tasks) == 0:
            self.ui_service.print_elements_not_found_in_tasks_list()
            return

        for k, v in enumerate(private_list_tasks):
            print(f"{k} - {v}")

        try:
            index_task = int(input("Введите индекс приватной задачи для удаления: "))
        except ValueError:
            self.ui_service.print_user_input_is_not_valid("Нужно ввести число")
            return

        deleted_private_task = self.tasks_private_service.delete_private_task(index_task)
        if deleted_private_task is None:
            self.ui_service.print_user_input_is_not_valid("Номера нет в списке")
            return

        self.ui_service.print_task_delete_success(deleted_private_task)



    def handle_show_deleted_tasks(self):
        self.ui_service.print_deleted_tasks_list_title()

        deleted_list_tasks = self.tasks_service.get_deleted_task_list()

        if len(deleted_list_tasks) == 0:
            self.ui_service.print_elements_not_found_in_deleted_tasks_list()
            return False

        for k, v in enumerate(deleted_list_tasks):
            print(f"{k} - {v}")

        return None



    def handle_set_private_password(self):
        self.ui_service.print_set_private_password()
        new_password = input("Введите новый пароль для личного списка: ")

        if not self.valid_str(new_password):
            self.ui_service.print_user_input_is_not_valid("Пароль не соответствует нормам")
            return
        else:
            print('Пароль был успешно установлен!')

        self.tasks_private_service.set_password(new_password)



    def handle_planner(self):
        self.ui_service.print_planner_menu()
        choice = input("Выберите действие планировщика: ")

        match choice:
            case "1":
                self.handle_add_planned_task()
            case "2":
                self.handle_show_planned_tasks()
            case _:
                self.ui_service.print_user_input_is_not_valid("Нет такого варианта в планировщике")



    def handle_add_planned_task(self):
        task_name = input("Введите название задачи: ")
        date = input("Введите дату (например, 2026-02-23 или любое удобное для вас описание): ")

        if not self.valid_str(task_name):
            self.ui_service.print_user_input_is_not_valid("Название задачи не соотвествует нормам!")
            return

        if not self.valid_str(date):
            self.ui_service.print_user_input_is_not_valid("Дата не соотвествует нормам!")
            return

        self.tasks_service.add_planned_task(task_name, date)
        print(f'Запланированная задача "{task_name}" на "{date}" добавлена.')



    def handle_show_planned_tasks(self):
        self.ui_service.print_planned_tasks_title()
        planned_tasks = self.tasks_service.get_planned_tasks()

        if not planned_tasks:
            print("Нет запланированных задач")
            return

        for index, task in enumerate(planned_tasks):
            print(f'{index} - {task["name"]} (когда: {task["due_date"]})')

    def handle_search_tasks(self):
        word = input("Слово: ")
        if not self.valid_str(word):
            print("Введите непустое слово.")
            return
        found = self.tasks_service.find_tasks(word)
        if not found:
            print("Ничего не найдено.")
            return
        for i in found:
            print(i)