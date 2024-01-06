import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand
from models import storage


class TestHBNBCommand(unittest.TestCase):
    """Test cases for console"""
    @classmethod
    def setUpClass(cls):
        """Set up the testing environment"""
        cls.console = HBNBCommand()

    @classmethod
    def tearDownClass(cls):
        """Clean up the testing environment"""
        del cls.console
        try:
            storage.reload()
        except FileNotFoundError:
            pass

    def setUp(self):
        """Set up before each test"""
        storage.reload()
        # Replace sys.stdin with a new StringIO object
        self.console.stdin = StringIO()

    def tearDown(self):
        """Clean up after each test"""
        # Close the StringIO object to simulate the behavior of sys.stdin
        self.console.stdin.close()

    def test_quit(self):
        """Test the quit method"""
        with self.assertRaises(SystemExit):
            self.console.onecmd("quit")

    @patch('sys.stdout', new_callable=StringIO)
    def test_help_quit(self, mock_stdout):
        """Test the help_quit method"""
        self.console.onecmd("help quit")
        output = mock_stdout.getvalue().strip()
        self.assertEqual(output, "Exits the program with formatting")

    def test_do_EOF(self):
        """Test the do_EOF method"""
        with self.assertRaises(SystemExit):
            self.console.onecmd("EOF")

    @patch('sys.stdout', new_callable=StringIO)
    def test_help_EOF(self, mock_stdout):
        """Test the help_EOF method"""
        self.console.onecmd("help EOF")
        output = mock_stdout.getvalue().strip()
        self.assertEqual(output, "Exits the program without formatting")

    def test_empty_line(self):
        """ Ensure that line is empty"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("")
            output = f.getvalue().strip()
        self.assertEqual(output, "")

    def test_create_no_param(self):
        """ Ensure that model is created without parameters"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create State")
            output = f.getvalue().strip()
        self.assertTrue(output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_do_create(self, mock_stdout):
        """Test the do_create method"""
        self.console.onecmd("create BaseModel")
        output = mock_stdout.getvalue().strip()
        self.assertTrue(output)  # Check if output is not empty

    @patch('sys.stdout', new_callable=StringIO)
    def test_help_create(self, mock_stdout):
        """Test the help_create method"""
        self.console.onecmd("help create")
        output = mock_stdout.getvalue().strip()
        self.assertTrue(output)  # Check if output is not empty

    # Add similar test methods for other commands...


if __name__ == '__main__':
    unittest.main()
