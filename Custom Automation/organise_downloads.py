import time
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# User credentials (should be securely stored)
LIBRARY_URL = "https://www.lib.uchicago.edu/"

# Create a function to log in to the library portal and renew books
def login_and_renew_books():
    # Set up Selenium WebDriver (make sure you have Chrome installed)
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    # Open the library login page
    driver.get(f"{LIBRARY_URL}/login")
    time.sleep(2)

    # Find the login fields and enter credentials
    borrow_request = driver.find_element(By.ID, "//ul[@class=\"nav navbar-nav\"]/li[2]/a")  # Adjust the selector to match the form
    renew_link = driver.find_element(By.ID, "(//li[contains(@class,\"dropdown open\")]/ul//a)[2]")

    # Navigate to the borrowed books page
    driver.get(f"{LIBRARY_URL}/borrowed_books")
    time.sleep(2)

    # Parse the borrowed books list (this will depend on the page structure)
    soup = BeautifulSoup(driver.page_source, 'html.parser')

    books = soup.find_all("div", class_="borrowed-book")  # Adjust the selector to match your library's structure

    # Check if any books need renewal and renew them
    for book in books:
        title = book.find("h3", class_="book-title").text.strip()
        due_date = book.find("span", class_="due-date").text.strip()

        # You can check if the book is near the due date and renew it
        if "Due Soon" in due_date:  # Example condition
            renew_button = book.find("button", class_="renew-button")
            if renew_button:
                renew_button.click()
                print(f"Renewed: {title}")
            else:
                print(f"No renew button found for {title}")
        else:
            print(f"Book '{title}' does not need renewal yet.")

    # Close the browser after task completion
    driver.quit()


if __name__ == "__main__":
    login_and_renew_books()
