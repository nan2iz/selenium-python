import math, operator

from PIL import Image
from selenium import webdriver


driver = webdriver.Chrome()
driver.get("http://bronco-planner.com/")
assert "Bronco-Planner - CPP Student Organizer" in driver.title
driver.save_screenshot("01.png")
driver.close()

driver = webdriver.Firefox()
driver.get("http://bronco-planner.com/")
assert "Bronco-Planner - CPP Student Organizer" in driver.title
driver.save_screenshot("02.png")
driver.close()

i1 = Image.open("01.png").histogram()
i2 = Image.open("02.png").histogram()

rms = math.sqrt(reduce(operator.add, map(lambda a,b: (a-b)**2, i1, i2))/len(i1))
