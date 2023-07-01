from django.urls import reverse
from rest_framework.test import APISimpleTestCase


class TaskSortingTestCase(APISimpleTestCase):

    def test_wrong_key(self):
        data = {'wrong_key': 'some_value'}
        url = reverse('get-tasks')
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data, {
            "build": [
                "This field is required."
            ]
        })

    def test_wrong_build(self):
        data = {'build': 'wrong_build'}
        url = reverse('get-tasks')
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.data, {
            "detail": "No such build exists!"
        })

    def test_get_sorted_tasks(self):
        data = {"build": "forward_interest_test"}
        url = reverse('get-tasks')
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, 200)
        expected_tasks = [
            "coloring_aqua_centaurs",
            "create_olive_centaurs",
            "read_yellow_centaurs",
            "bring_blue_centaurs",
            "create_maroon_centaurs",
            "upgrade_navy_centaurs",
            "train_purple_centaurs",
            "design_lime_centaurs",
            "create_teal_centaurs",
            "coloring_white_centaurs",
            "bring_olive_centaurs",
            "enable_yellow_centaurs"
        ]
        self.assertEqual(response.data, expected_tasks)
