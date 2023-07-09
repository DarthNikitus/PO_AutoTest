import time

from Pages.login_page import LoginPage, StartPage

"""Авторизация  Обдумать над чеком автоизации"""


def test_login_form(driver):
    login_page = LoginPage(driver, 'https://practice2023.passoffice.ru/auth/login')
    login_page.open()
    time.sleep(0.1)
    login_page.filing_login_pass()
    time.sleep(0.1)
    # #now_url = driver.getCurrenUrl()
    # answer = login_page.check_login()
    # print(answer)
    # assert answer in 'Выход'
    return driver.current_url
    #TODO  - сделать проверку что авторизация прошла успешна - можно по урл


"""Создание посетителя"""


def test_add_viitor(driver):
    url = test_login_form(driver)
    start_page = StartPage(driver, url)
    start_page.add_visitors()
    return driver.current_url
    # time.sleep(3)

    # TODO - сделать удаление посетителя
    # TODO - сделать проверку что создан посетитель


"""Создание Группы Доступа"""


def test_add_access_group(driver):
    url = test_login_form(driver)
    start_page = StartPage(driver, url)
    start_page.add_access_group()


"""Создание заявки"""


def test_create_my_application(driver):
    url = test_login_form(driver)
    start_page = StartPage(driver, url)
    start_page.add_my_application()

    start_page.open_incoming()
    """Перевод заявки в согласие и выдача заявки"""
    start_page.agreement_application()
    #txt_1 = start_page.issue_pass()
    #start_page.signing_receiving_pass(txt_1)

    # time.sleep(2)


    # TODO - сделать проверку что создалась заявка и то что она в обработке
    # TODO - сделать удаление заявки

def test_withdraw_pass(driver):
    url = test_login_form(driver)
    start_page = StartPage(driver, url)
    start_page.withdraw_pass()

def test_copy_application(driver):
    url = test_login_form(driver)
    start_page = StartPage(driver, url)
    start_page.copy_application()
    start_page.open_incoming()
    start_page.add_another_pass()
    start_page.signing_receiving_pass('a')


def test_create_area(driver):
    url = test_login_form(driver)
    start_page = StartPage(driver, url)
    start_page.create_area()
    start_page.give_permission_area()

def test_create_passage(driver):
    url = test_login_form(driver)
    start_page = StartPage(driver, url)
    start_page.create_passage()


def test_create_monitor(driver):
    url = test_login_form(driver)
    start_page = StartPage(driver, url)
    start_page.create_monitor()

# def test_add_anything_pass(driver):
#     url = test_create_my_application(driver)
#     start_page = StartPage(driver, url)
#     start_page.copy_application()
