from selenium import webdriver

#firefox
driver = webdriver.Firefox(executable_path=r'c:\lib\geckodriver.exe')
driver.get("http://bronco-planner.com/")
assert "Bronco-Planner - CPP Student Organizer" in driver.title
driver.close()

#chrome
driver = webdriver.Chrome(executable_path=r'c:\lib\chromedriver.exe')
driver.get("http://bronco-planner.com/")
assert "Bronco-Planner - CPP Student Organizer" in driver.title
driver.close()