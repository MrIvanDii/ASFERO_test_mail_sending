import config
from pages.MailPages import LogInPage
from pages.LatterPage import AddLetterPage


def test_log_in(browser):
    login_page = LogInPage(browser)
    letter_page = AddLetterPage(browser)
    login_page.go_to_site()
    login_page.enter_login(config.login)
    login_page.enter_password_and_return(config.password)
    letter_page.get_source_of_page()


    for message in range(0, 3):
        login_page.go_to_letter_site()
        letter_page.enter_email(config.recipient)
        letter_page.enter_subject('2vj21n1v2b')
        letter_page.enter_text_of_letter('l5l2p5g3n1')
        letter_page.click_on_the_button_send()

    letter_page.click_on_the_button_letters()
    letter_page.get_source_of_page()
    letter_page.check_the_status()
    letter_page.collect_data_head()
    letter_page.collect_links_messages()
    letter_page.collect_body_message()
    letter_page.click_on_the_button_letters()
    letter_page.send_the_last_masseges()
    letter_page.enter_email(config.recipient)
    letter_page.enter_subject('Final letter of the test')
    letter_page.click_on_the_button_send()
    letter_page.click_on_the_button_letters()


