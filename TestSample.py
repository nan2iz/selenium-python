import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class TestSample(unittest.TestCase):
    def setUp(self):
        #for windows
        #self.driver = webdriver.Firefox(executable_path=r'c:\lib\geckodriver.exe')
        self.driver = webdriver.Firefox()

    def test_search_in_website(self):
        driver = self.driver
        driver.get("https://www.cpp.edu/")
        self.assertIn("Cal Poly Pomona", driver.title)
        elem = driver.find_element_by_name("viewport")

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()