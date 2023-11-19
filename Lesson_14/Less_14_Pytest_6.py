from Less_14_Task_6 import User, Project
import pytest


@pytest.fixture(scope="session", autouse=True)
def create_json():
    content = """
[
      {
        "name": "Sergey",
        "id": "1",
        "level": "4"
      },
      {
        "name": "Vlad",
        "id": "2",
        "level": "3"
      },
      {
        "name": "Elena",
        "id": "3",
        "level": "5"
      }
]
    """
    with open("new_json.json", "w") as file:
        file.write(content)


@pytest.fixture(scope="session")
def instance_low_level_user():
    return User("Vlad", "2", "3")


@pytest.fixture(scope="session")
def instance_high_level_user():
    return User("Elena", "3", "5")


def test_user_exists(instance_high_level_user):
    project = Project()
    users = project.read_json()
    assert instance_high_level_user in users


if __name__ == "__main__":
    pytest.main(["-v"])
