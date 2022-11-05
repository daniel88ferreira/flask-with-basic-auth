from unittest import TestCase

from app.main import create_app


class Test(TestCase):

    def setUp(self) -> None:
        app = create_app()
        self.app = app.test_client()

    def test_index(self):
        """
        Test the index
        """
        response = self.app.get('/', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.text, "Hello, World!")
