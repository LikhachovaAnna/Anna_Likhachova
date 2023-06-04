from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")

driver = webdriver.Chrome(options=options)

driver.get("https://opensource-demo.orangehrmlive.com/")

# Очікування появи форми входу
wait = WebDriverWait(driver, 10)
username_input = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '[name="username"]')))
password_input = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '[name="password"]')))
login_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[type="submit"]')))

# Заповнення форми входу
username_input.send_keys("Admin")
password_input.send_keys("admin123")
login_button.click()

# Очікування завантаження сторінки після входу
job_menu_item = wait.until(EC.element_to_be_clickable((By.XPATH, '//span[text()="Admin"]')))
job_menu_item.click()

job_titles_menu_item = wait.until(EC.element_to_be_clickable((By.XPATH, '//span[contains(text(), "Job")]')))
job_titles_menu_item.click()

job_title_menu_item = wait.until(EC.element_to_be_clickable((By.XPATH, '//a[text()="Job Titles"]')))
job_title_menu_item.click()

# Додавання нової посади
add_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[contains(@class, "oxd-button") and contains(@class, "oxd-button--medium") and contains(@class, "oxd-button--secondary")]')))
add_button.click()

job_title_input_element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'div[data-v-957b4417] input[data-v-1f99f73c]')))
job_title_input_element.send_keys("Student or Intern")


job_description_input = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'div[data-v-957b4417] textarea[data-v-bd337f32]')))
job_description_input.send_keys("Free text up to 20 chars")

#note_input = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'placeholder["Add note"]')))
#note_input.send_keys("Note")

save_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[contains(@class, "oxd-button") and contains(@class, "oxd-button--medium") and contains(@class, "oxd-button--secondary")]')))
save_button.click()



# Перевірка, що зміни відображаються на сторінці Job Titles
element_text = "Student or Intern"  # Текст, який шукаємо

# Знайти всі рядки таблиці
table_rows = driver.find_elements(By.CSS_SELECTOR, 'div[data-v-0d5ef602]')

# Перевірити кожен рядок таблиці на наявність елемента з заданим текстом
for row in table_rows:
    cell_text = row.find_element(By.CSS_SELECTOR, 'div[data-v-6c07a142]').text
    if cell_text == element_text:
        print("Елемент з текстом '{Student or Intern}' знайдений.".format(element_text))
        break
else:
    print("Елемент з текстом '{Student or Intern}' не знайдений.".format(element_text))
# Вибір поля з новим посадовим званням і видалення його
checkbox = driver.find_element(By.XPATH, f'//a[text()="Student or Intern"]/preceding-sibling::input[@type="checkbox"]')
checkbox.click()

delete_button = driver.find_element(By.ID, 'btnDelete')
delete_button.click()

confirm_delete_button = wait.until(EC.element_to_be_clickable((By.ID, 'dialogDeleteBtn')))
confirm_delete_button.click()

driver.quit()