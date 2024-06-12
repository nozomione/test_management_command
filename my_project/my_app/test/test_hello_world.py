from django.test import TestCase
from django.core.management import call_command
from io import StringIO
import sys


class TestHelloWorld(TestCase):
    def call_command(self):
        out = StringIO()
        sys.stdout = out
        call_command("hello_world", stdout=out)
        return out.getvalue().replace("\n", "")

    def test_hello_world(self):
        result = self.call_command()
        expected_value = "Hello World"
        self.assertEquals(result, expected_value)
