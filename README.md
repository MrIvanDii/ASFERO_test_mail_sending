# ASFERO_test_mail_sending:

Test task for the position QA Automation Engineer в ASFERO

Write a test project using Python, Selenium.

# Test must be able to do the next instruction:

- Login to any email box
- Send from mails from current box to yourself with:
    Theme: Random string with 10 symbols (letters and numbers only)
    Body: Random string with 10 symbols (letters and numbers only)
- Check that all mails are delivered.
- Collect data from all incoming mails and save it as Object (Dictionary), where:
     Key is theme of mail
     Value is body of mail
- Send collected data to yourself as: “Received mail on theme {Theme} with message: {Body}. It contains {Count of letters} letters and {Count of numbers} numbers” (repeat for each mail)
- Delete all received mails except the last one


# Copying the repository and installing dependencies:
```
git clone https://github.com/MrIvanDii/ASFERO_test_mail_sending
cd ASFERO_test_mail_sending/ASFERO
python -m venv rest_env
rest_env\Scripts\activate (для OS Windows)
source rest_env/bin/activate (для OS Mac/Linux)
pip install -r requirements.txt
```
# Running tests:

Before running the tests, you should change pwd to the ASFERO project directory

# Launch arguments:

'-s' - show prints in progress

'-v' - verbose mode to see which tests have been run

# Start command:
```
py.test -s -v tests
```
