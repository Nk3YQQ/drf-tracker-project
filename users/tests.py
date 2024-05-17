from rest_framework import status
from rest_framework.test import APITestCase

from users.services import create_user, create_other_user


class UserAPITestCase(APITestCase):
    """ Тестирование модели пользователя """

    def setUp(self) -> None:
        """ Установка данных """

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

        self.patch_data = {"first_name": "Test1"}

    def test_user_retrieve(self):
        """ Тестирование просмотра пользователя """

        response = self.client.get(
            f'/users/{self.user.pk}/',
            headers=self.header
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_user_retrieve_for_other_user(self):
        """ Тестирование просмотра пользователя для другого пользователя"""

        response = self.client.get(
            f'/users/{self.user.pk}/',
            headers=self.other_user_header
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_user_update(self):
        """ Тестирование обновления пользователя """

        response = self.client.patch(
            f'/users/edit/{self.user.pk}/',
            data=self.patch_data,
            headers=self.header
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_user_update_for_other_user(self):
        """ Тестирование обновления пользователя для другого пользователя"""

        response = self.client.patch(
            f'/users/edit/{self.user.pk}/',
            data=self.patch_data,
            headers=self.other_user_header
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_403_FORBIDDEN
        )

    def test_user_destroy(self):
        """ Тестирование удаление пользователя """

        response = self.client.delete(
            f'/users/destroy/{self.user.pk}/',
            headers=self.header
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )

    def test_user_destroy_for_other_user(self):
        """ Тестирование удаление пользователя для другого пользователя """

        response = self.client.delete(
            f'/users/destroy/{self.user.pk}/',
            headers=self.other_user_header
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_403_FORBIDDEN
        )