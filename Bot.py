import time
from congif import DRIVER_PATH,USERNAME,PASSWORD,URL,TIMEOUT,READ_TIME
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
        self.driver.get("https://myacademy.oracle.com/lmt/xlr8login.login?site=oa")
    # Connect to the existing Chrome session
        #options = webdriver.ChromeOptions()
        #self.driver = webdriver.Chrome(options=options)





        self.parent_handle = self.driver.current_window_handle
        with open("visited.txt", 'r') as file:
            for line in file:
                self.visited.append(line.strip())

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
                            comp=False
                            try:
                                completed = item.find_element_by_class_name("course-badges")
                                comp=True
                            except:
                                comp=False
                            quiz=item.find_element_by_tag_name("a")

                            quizzer=quiz.find_element_by_tag_name("span").text
                            print(quizzer)
                            if comp==True:
                                comp=False
                                print("completed badge!!")
                                pass
                            elif quiz in self.visited:
                                print("in visited")
                                pass
                            elif "Quiz" in quizzer:
                                print("in quiz")
                            
                                pass
                            else:
                                self.completeOne(item)
                        except Exception as e:
                            print(e)
                            print("RETURN")
                            return item
                return None
            except Exception as err:
                print(err)
                time.sleep(TIMEOUT)
    quiz_detect=""

    def completeOne(self, item):
        customPrint("Completing One", "INFO")
        while True:
            try:
                quiz=item.find_element_by_class_name("title")
                global quiz_detect
                quiz_detect=quiz.text
                print(quiz_detect)
                self.visited.append(quiz_detect)
                
                if "Quiz" in quiz_detect:
                    print("is quiz")
                    self.visited.append(quiz_detect)
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
                    self.nextPPress()
                    

                    
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
                        
                        max_wait_time = 10  # seconds

# Start time for measuring elapsed time
                        start_time = time.time()

                        while True:
                            try:
                                # Check if the next button is clickable
                                next_button = WebDriverWait(self.driver, 1).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".universal-control-panel__button_next, .universal-control-panel__button_right-arrow")))
                                # If found, click on it and exit the loop
                                next_button.click()
                                break
                            except (self.NoSuchElementException, TimeoutError):
                                # If the button is not found within 1 second or if it's not clickable, check elapsed time
                                elapsed_time = time.time() - start_time
                                # If the elapsed time exceeds the maximum wait time, exit the loop
                                if elapsed_time > max_wait_time:
                                    print("Button not found within the maximum wait time. Proceeding without waiting.")
                                    break
                        print("Next button found.")
                    except Exception as e:
                        self.visited.append()
                        self.goBackToLearningPath()
                        self.driver.save_screenshot("test.png")
                        print("Failed to find or click the next button:", e)

            except:
                self.visited.append(quiz_detect)
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


    def goBackToLearningPath(self):
        customPrint("Going back to learning path", "INFO")
        self.driver.back()
        self.driver.refresh()
        time.sleep(5)
        return True


    def close(self):
        customPrint("Closed Bot", "INFO")
        self.driver.close()
