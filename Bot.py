import time
from config import DRIVER_PATH,USERNAME,PASSWORD,URL,TIMEOUT,READ_TIME
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



HEADER = '\033[95m'
OKBLUE = '\033[94m'
OKCYAN = '\033[96m'
OKGREEN = '\033[92m'
WARNING = '\033[93m'
FAIL = '\033[91m'
ENDC = '\033[0m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'


def customPrint(text, texttype="MESSAGE"):
    if texttype == "WARNING":
        print(f"{WARNING}${texttype}: {text}{ENDC}")
    elif texttype == "SUCCESS":
        print(f"{OKGREEN}${texttype}: {text}{ENDC}")
    elif texttype == "INFO":
        print(f"{OKCYAN}${texttype}: {text}{ENDC}")
    elif texttype == "ERROR":
        print(f"{FAIL}${texttype}: {text}{ENDC}")
    elif texttype == "MESSAGE":
        print(f"{OKBLUE}${texttype}: {text}{ENDC}")
    else:
        print(f"{FAIL}{text}{ENDC}")


class Bot:
    visited=[]
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=DRIVER_PATH)
        self.driver.get(
            "https://myacademy.oracle.com/lmt/xlr8login.login?site=oa")
        self.parent_handle = self.driver.current_window_handle
        with open("visited.txt", 'r') as file:
            for line in file:
                self.visited.append(line.strip())

    def login(self):
        customPrint("Filling Username", "INFO")
        # fill username
        while True:
            try:
                self.driver.find_element_by_id(
                    "inputUsername").send_keys(USERNAME)
                break
            except:
                time.sleep(TIMEOUT)
        customPrint("Filled Username", "INFO")
        customPrint("Filling Password", "INFO")
        # fill password
        while True:
            try:
                self.driver.find_element_by_id(
                    "inputPassword").send_keys(PASSWORD)
                break
            except:
                time.sleep(TIMEOUT)
        customPrint("Filled Password", "INFO")
        # click on signin
        while True:
            try:
                self.driver.find_element_by_class_name(
                    "primary.btn.login").click()
                break
            except:
                time.sleep(TIMEOUT)
        customPrint("Next", "SUCCESS")
        return True

    def openChannel(self):
        while True:
            try:
                self.driver.find_element_by_class_name("tiles-content").click()
                break
            except:
                time.sleep(TIMEOUT)
        customPrint("Opened Channel", "INFO")
        return True

    def openLearningModule1(self):
        while True:
            try:
                self.driver.find_element_by_xpath(
                    "//a[@class='tiles-title']").click()
                """listoanchors = self.driver.find_elements_by_xpath("//a[@class='tiles-title']")
                a = None
                for anchor in listoanchors:
                    anchor."""
                break
            except:
                time.sleep(TIMEOUT)
        customPrint("Opened Module", "INFO")
        return True

    def openLearningModule2(self):
        while True:
            try:
                self.driver.find_elements_by_xpath(
                    "//a[@class='tiles-title']")[1].click()
                """listoanchors = self.driver.find_elements_by_xpath("//a[@class='tiles-title']")
                a = None
                for anchor in listoanchors:
                    anchor."""
                break
            except:
                time.sleep(TIMEOUT)
        customPrint("Opened Module", "INFO")
        return True

    def openLearningModule3(self):
        while True:
            try:
                self.driver.find_elements_by_xpath(
                    "//a[@class='tiles-title']")[2].click()
                """listoanchors = self.driver.find_elements_by_xpath("//a[@class='tiles-title']")
                a = None
                for anchor in listoanchors:
                    anchor."""
                break
            except:
                time.sleep(TIMEOUT)
        customPrint("Opened Module", "INFO")
        return True

    def openLearningModuleN(self, n=0):
        while True:
            try:
                self.driver.find_elements_by_css_selector(
                    'h4[class="title"]>a')[n].click()
                """listoanchors = self.driver.find_elements_by_xpath("//a[@class='tiles-title']")
                a = None
                for anchor in listoanchors:
                    anchor."""
                break
            except:
                time.sleep(TIMEOUT)
        customPrint("Opened Module", "INFO")
        return True

    def getFirstIncomplete(self):
        while True:
            try:
                collapsibles = self.driver.find_elements_by_class_name(
                    "learning-path--detail__section")

                collapsibles.pop(0)
                # collapsibles.pop(0)
                customPrint("Got Collapsables", "INFO")
                for collapsible in collapsibles:
                    items = None
                    try:
                        items = collapsible.find_elements_by_class_name(
                            "card")
                    except:
                        continue
                    for item in items:
                        try:
                            completed = item.find_element_by_class_name("course-badges")
                            quiz=item.find_element_by_class_name("title")
                            if completed:
                                pass
                            elif quiz in self.visited:
                                pass
                            print(completed)
                            pass
                        except:
                            print("RETURN")
                            return item
                return None
            except Exception as err:
                print(err)
                time.sleep(TIMEOUT)


    def completeOne(self, item):
        customPrint("Completing One", "INFO")
        while True:
            try:
                quiz=item.find_element_by_class_name("title")
                quiz_detect=quiz.text
                print(quiz_detect)
                
                if quiz_detect in self.visited:
                    return
                if "Quiz" in quiz_detect:
                    return
                box=item.find_element_by_tag_name("img").click()
                print("img clicked")
                return True
            except:
                time.sleep(TIMEOUT)
        return True

    def closeAllOtherHandles(self):
        handles = self.driver.window_handles
        size = len(handles)
        for x in range(size):
            if handles[x] != self.parent_handle:
                self.driver.switch_to_window(handles[x])
                print(self.driver.title)
                self.driver.close()
        self.driver.switch_to_window(self.parent_handle)
        customPrint("Closed All Other Handles", "INFO")

    def play(self):
        print("ulla vandhachu")
        while True:
            try:
                section = self.driver.find_element_by_class_name("section")
                # Find the div with the specified class
                main_div = section.find_element_by_class_name("main")
                course_div = main_div.find_element_by_class_name("course-details__intro")
                but_div= course_div.find_element_by_class_name("cta")
                
            except Exception as e:
                print("Exception occurred1:", e)
                time.sleep(TIMEOUT)
            try:
                # Find the anchor tag with the class "play" within the detail div
                play_button = but_div.find_element_by_tag_name("a")
                
                if play_button:
                    play_button.click()
                    customPrint("Clicked on play button", "SUCCESS")
                    time.sleep(READ_TIME)
                    self.switchTabs()

                    

                    
                else:
                    print("Play button not found within the detail div.")
            except Exception as e:
                print("Exception occurred:", e)
                time.sleep(TIMEOUT)
        return True
    def nextPPress(self):

        while True:
            try:
                wait = WebDriverWait(self.driver, 20)
                iframe = wait.until(EC.presence_of_element_located((By.ID, "content-iframe")))
                self.driver.switch_to.frame(iframe)

# Now, find the next button using the specified classes
                while True :
                    try:
                        
                                next_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".universal-control-panel__button_next, .universal-control-panel__button_right-arrow")))
                           
                                next_button.click()
                                print("Next button found.")
                    except Exception as e:
                        self.goBackToLearningPath()
                        self.driver.save_screenshot("test.png")
                        print("Failed to find or click the next button:", e)

            except:
                with open("visited.txt", 'w') as file:
                    for item in self.visited:
                        file.write("%s\n" % item)

                
    def switchTabs(self):
        
            try:
             new_tab_handle = self.driver.window_handles[-1]
             self.driver.switch_to.window(new_tab_handle)
             print("switched")
             self.driver.save_screenshot("sc.png")
             self.nextPPress()
            except:
                print("not switched")

    def nextPress(self):
        while True:
            try:
                mainTab = self.driver.find_element_by_xpath("main-container")
                n1 = mainTab.find_element_by_class_name("universal-control-panel")
                n2 = n1.find_element_by_class_name("universal-control-panel__container")
                n3= n2.find_element_by_class_name("universal-control-panel__button_right-arrow")
                
                n3.click()
                time.sleep(READ_TIME)

            except:
                print("button not found")

    def goBackToLearningPath(self):
        customPrint("Going back to learning path", "INFO")
        self.driver.back()
        self.driver.refresh()
        time.sleep(5)
        return True
        while True:
            try:
                course = self.driver.find_element_by_id("userCourseLPSContent")
                item = course.find_element_by_class_name(
                    "tiles-layout.table-tiles.three-col-tiles.clearboth")
                item.click()
                break
            except:
                time.sleep(TIMEOUT)

    def close(self):
        customPrint("Closed Bot", "INFO")
        self.driver.close()
