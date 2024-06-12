from django.test import TestCase
from django.core.management import call_command
from io import StringIO


class TestHelloWorld(TestCase):
    def call_command(self):
        out = StringIO()
        call_command("hello_world", stdout=out)
        return out.getvalue()

    def test_hello_world(self):
        out = self.call_command()
        expected_value = "Hello World"
        self.assertEquals(out, expected_value)
