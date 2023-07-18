from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

### Initialize Browser (Chrome)
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)
driver.get("https://qa.unair.ac.id/qa/gate/login")

### Login Phase
## Verify current page is login page 
def check_login():
    try:
       driver.find_element(By.XPATH, "//div[@class='title-name company-pattern company-pattern-custom']")
    except NoSuchElementException:
        return False
    return True

## Login process
while check_login() == False:
    driver.find_element(By.NAME, 'userid').send_keys("NIM_MAHASISWA")
    driver.find_element(By.NAME, 'password').send_keys("PASS_MAHASISWA")
    driver.find_element(By.CSS_SELECTOR, ".btn.btn-flat.btn-primary").click()

### Sistem Penjamin Mutu (SIM) Kuesioner Phase
driver.find_element(By.ID, "link-kuesioner").click()
driver.find_element(By.XPATH, "//div[@class='role_box']").click()

### 'Evaluasi Tahunan' Page Phase (Autofill)
## Initialize required variables 
list_qna = ["KINERJA TIM DOSEN DALAM PERKULIAHAN (Jenjang Sarjana & Diploma)", "KINERJA TENAGA ADMINISTRASI DEPARTEMEN",
            "KINERJA SUB BAGIAN FAKULTAS", "KINERJA DOSEN DALAM PERWALIAN"]
list_id_dropdown = ["idmk", "idunit", "idunit", "dosen"]
def dropdown_counter(dropdown):
    return len(Select(dropdown).options)

## Autofill dropdowns & radio buttons
def autofill(curr_qna):
    # Choose kuesioner
    sleep(2)
    driver.find_element(By.XPATH, f"//p[text()='{list_qna[curr_qna]}']").click()
    # Find dropdown 
    curr_drop = driver.find_element(By.ID, list_id_dropdown[curr_qna])
    qty_drop = dropdown_counter(curr_drop)-1
    # Dropdown loops, autofill radio buttons
    for i in range(qty_drop):
        sleep(2)
        curr_drop = driver.find_element(By.ID, list_id_dropdown[curr_qna])
        curr_drop.click()
        curr_drop.send_keys(Keys.ARROW_DOWN, Keys.ENTER)
        radio_button = driver.find_elements(By.XPATH, "//input[@type='radio' and @value='26']")
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        for button in radio_button:
            button.click()
        if curr_qna == 0:
            add_drop = driver.find_element(By.ID, 'dosen')
            add_drop.click()
            add_drop.send_keys(Keys.ARROW_DOWN, Keys.ENTER)
        driver.find_element(By.XPATH, "//i[@class='fa fa-save']").click()
        confirm_alert = driver.switch_to.alert
        sleep(1)
        confirm_alert.accept()
        driver.find_element(By.XPATH, "//i[@class='fa fa-chevron-left']").click()
        try:
            driver.find_element(By.XPATH, f"//p[text()='{list_qna[curr_qna]}']").click()
        except NoSuchElementException:
            break

## Call autofill function
autofill(0)
autofill(1)
autofill(2)
autofill(3)