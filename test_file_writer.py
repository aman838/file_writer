import  unittest
import os
from file_writer import create_file

class TestFileCreation(unittest.TestCase):
    def setUp(self):
        print("hi")
        
    def test_file_is_created_and_written(self):
        # Call the function
        create_file()

        # Check if file exists
        self.assertTrue(os.path.exists("first_file.txt"))

        # Check content
        with open("first_file.txt", "r") as f:
            content = f.read()
        self.assertEqual(content, "my first file")

    def tearDown(self):
        # Clean up the file after test
        if os.path.exists("first_file.txt"):
            os.remove("first_file.txt")

if __name__ == "__main__":
    unittest.main()
