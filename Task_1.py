# Задача #1 : Создай класс Task, который позволяет управлять задачами (делами). У задачи должны быть атрибуты: описание задачи, срок выполнения и статус (выполнено/не выполнено).
# Реализуй функцию для добавления задач, отметки выполненных задач и вывода списка текущих (не выполненных) задач.

class Task:
    tasks = []  # общий список для всех задач

    def __init__(self, description, deadline, status=False):
        self.description = description
        self.deadline = deadline
        self.status = status

    def mark_as_completed(self):
        self.status = True

    @classmethod
    def add_task(cls, description, deadline):
        task = Task(description, deadline)
        cls.tasks.append(task)
        print(f'Задача "{task.description}" добавлена, срок выполнения: {task.deadline}')

    @classmethod
    def show_all_tasks(cls):
        task_status = False  # Проверка наличия невыполненных задач
        for task in cls.tasks:
            if not task.status:
                task_status = True
                print(f'Описание: {task.description}, Срок: {task.deadline}, Статус: Не выполнено')
        if not task_status:
            print("Все задачи выполнены или нет добавленных задач.")

    @classmethod
    def complete_task(cls, description):
        for task in cls.tasks:
            if task.description == description:
                task.mark_as_completed()
                print(f'Задача "{description}" отмечена как выполненная.')
                return
        print(f'Задача с описанием "{description}" не найдена.')

Task.add_task('Выучить Python', '11.10.2025')
Task.add_task('Сделать домашку', '11.06.2025')

Task.show_all_tasks()

Task.complete_task('Сделать домашку')

Task.show_all_tasks()