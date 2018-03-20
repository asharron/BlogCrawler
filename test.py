import os
import app
import unittest
import tempfile

class BlogCrawlerTestCase(unittest.TestCase):
    
    def setup(self):
        self.app = app.app.test_client()

    def testDB(self):
        assert os.path.exists('./app.db'), "Database does not exists, Run db_create.py"
        print("Database is present")
                

if __name__ == '__main__':
    unittest.main()

