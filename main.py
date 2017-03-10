from selenium import webdriver

driver = webdriver.Firefox(executable_path=r'c:\lib\geckodriver.exe')
driver.get("http://bronco-planner.com/")
assert "Bronco-Planner - CPP Student Organizer" in driver.title
driver.close()
