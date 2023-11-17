"""
📌 На семинаре 13 был создан проект по работе с пользователями (имя, id, уровень).
📌 Напишите 3-7 тестов pytest для данного проекта.
📌 Используйте фикстуры.
"""

import json


class LevelError(Exception):
    pass


class AccessError(Exception):
    pass


class User:
    def __init__(self, name, _id, level):
        self.name = name
        self._id = _id
        self.level = level

    def __str__(self):
        return (
            f"Создан пользователь {self.name}, уровень = {self.level}, id = {self._id}"
        )

    def to_dict(self):
        return {"name": self.name, "id": self._id, "level": self.level}

    def __eq__(self, other: object) -> bool:
        return self.name == other.name and self._id == other._id


class Project:
    file_name = "new_json.json"

    def __init__(self):
        self.lst_users = self.read_json()

    def read_json(self):
        lst_users = []
        store_id = set()
        try:
            with open(self.file_name, "r", encoding="utf-8") as f:
                user_data = json.load(f)
                for user in user_data:
                    lst_users.append(User(user["name"], user["id"], user["level"]))
                    store_id.add(user["id"])
        except FileNotFoundError as e:
            print(e)
        return lst_users

    def auth_user(self):
        name = input("Введите имя: ")
        _id = input("Введите id: ")
        level = None
        my_user = User(name, _id, level)
        for user in self.lst_users:
            if my_user == user:
                my_user.level = user.level
                return my_user
        raise AccessError(_id)

    def add_user(self, creator: User, creature: User):
        if int(creator.level) > int(creature.level):
            raise LevelError(creature.level)
        self.lst_users.append(creature)
        return self.lst_users

    def save_json(self):
        with open(self.file_name, "w", encoding="utf-8") as f:
            """генерируем список словарей по данным пользователей из списка"""
            res_users = [i.to_dict() for i in self.lst_users]
            """т.к. i сейчас  - это объект (экземпляр класса User), то можем обратиться через точечную нотацию 
            к методу данного класса"""
            json.dump(res_users, f, indent=2)


if __name__ == "__main__":
    project = Project()
    my_user = project.auth_user()

    while True:
        name = input("Name: ")
        if name == "help":
            break
        if not name:
            print("Имя не должно быть пустым")
            continue
        _id = input("id: ")
        level = input("level: ")
        if int(level) not in range(1, 8):
            print("Уровень доступа должен быть от 1 до 7")
            continue

        project.add_user(my_user, User(name, _id, level))

    project.save_json()
