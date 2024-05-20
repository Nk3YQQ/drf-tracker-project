from rest_framework import status
from rest_framework.test import APITestCase

from habit.models import Habit
from users.services import create_user, create_other_user


class HabitAPITestCase(APITestCase):
    """Тестирование модели привычки"""

    def setUp(self) -> None:
        """Установка данных"""

        user = create_user()
        other_user = create_other_user()

        self.user = user
        self.other_user = other_user

        response = self.client.post("/users/login/", data={"email": "test.testov@mail.ru", "password": "123qwe456rty"})

        response_for_other_user = self.client.post(
            "/users/login/", data={"email": "ivan.ivanov@mail.ru", "password": "123qwe456rty"}
        )

        self.token = response.json()["access"]
        self.other_user_token = response_for_other_user.json()["access"]

        self.header = {"Authorization": f"Bearer {self.token}"}
        self.other_user_header = {"Authorization": f"Bearer {self.other_user_token}"}

        self.habit_data = {
            "place": "дома",
            "time": "19:00",
            "action": "сделать гимнастику",
            "periodicity": "daily",
            "reward": "5 печенек",
            "estimated_time": 115,
        }

        self.habit = {
            "user": self.user,
            "place": "дома",
            "time": "19:00",
            "action": "сделать гимнастику",
            "periodicity": "daily",
            "reward": "5 печенек",
            "estimated_time": 115,
        }

        self.public_habit = {
            "user": self.user,
            "place": "дома",
            "time": "19:00",
            "action": "сделать гимнастику",
            "periodicity": "daily",
            "reward": "5 печенек",
            "estimated_time": 115,
            "is_public": True,
        }

        self.patch_data = {"action": "прокачивать пресс"}

    def test_create_habit(self):
        """Тестирование создания привычки"""

        response = self.client.post("/habits/create/", data=self.habit_data, headers=self.header)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        self.assertTrue(Habit.objects.all().exists())
        self.assertEqual(response.json()["user"], self.user.pk)

    def test_habit_list(self):
        """Тестирование списка привычек"""

        Habit.objects.create(**self.habit)

        response = self.client.get("/habits/", headers=self.header)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(Habit.objects.count(), 1)

    def test_habit_retrieve(self):
        """Тестирование одной привычки"""

        habit = Habit.objects.create(**self.habit)

        response = self.client.get(f"/habits/{habit.pk}/", data=self.habit, headers=self.header)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_habit_retrieve_for_other_user(self):
        """Тестирование одной привычки для другого пользователя"""

        habit = Habit.objects.create(**self.habit)
        public_habit = Habit.objects.create(**self.public_habit)

        response = self.client.get(f"/habits/{habit.pk}/", data=self.habit, headers=self.other_user_header)

        response_to_public_habit = self.client.get(
            f"/habits/public/{public_habit.pk}/", data=self.habit, headers=self.other_user_header
        )

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        self.assertEqual(response_to_public_habit.status_code, status.HTTP_200_OK)

    def test_habit_update(self):
        """Тестирование обновления привычки"""

        habit = Habit.objects.create(**self.habit)

        response = self.client.patch(f"/habits/edit/{habit.pk}/", data=self.patch_data, headers=self.header)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_habit_update_for_other_user(self):
        """Тестирование обновления привычки для другого пользователя"""

        habit = Habit.objects.create(**self.habit)

        response = self.client.patch(f"/habits/edit/{habit.pk}/", data=self.patch_data, headers=self.other_user_header)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_habit_destroy(self):
        """Тестирование удаления привычки"""

        habit = Habit.objects.create(**self.habit)

        response = self.client.delete(f"/habits/destroy/{habit.pk}/", headers=self.header)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_habit_destroy_for_other_user(self):
        """Тестирование удаления привычки для другого пользователя"""

        habit = Habit.objects.create(**self.habit)

        response = self.client.delete(f"/habits/destroy/{habit.pk}/", headers=self.other_user_header)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
