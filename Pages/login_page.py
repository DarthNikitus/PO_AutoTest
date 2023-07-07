import time

from locators.locators import LoginPageLocators, StartPageLocators

from Pages.base_page import BasePage
from generator import generated_pass_number



class LoginPage(BasePage):
    locators = LoginPageLocators()

    def filing_login_pass(self):
        login = 'Nikitus'
        password = 'Razdoburdin1'
        self.element_is_visible(self.locators.LOGIN).send_keys(login)
        self.element_is_visible(self.locators.PASS).send_keys(password)
        self.element_is_visible(self.locators.BUTTON_LOGIN).click()
        return

    def check_login(self):
        txt = self.elements_are_visible(self.locators.BUTTON_EXIT).text
        return txt


class StartPage(BasePage):
    locators = StartPageLocators()

    def add_visitors(self):
        txt = 'Посетители'
        last_name = 'Autotest'
        first_name = 'Test'
        self.element_is_visible(self.locators.MENU).click()
        time.sleep(3)
        self.element_is_visible(self.locators.VISITORS).click()
        time.sleep(1)
        self.element_is_visible(self.locators.BUTTON_ADD_VISITORS).click()
        self.element_is_visible(self.locators.LAST_NAME).send_keys(last_name)
        self.element_is_visible(self.locators.FIRST_NAME).send_keys(first_name)
        time.sleep(1)
        self.element_is_visible(self.locators.SAVE_PERSON).click()
        return last_name, first_name

    def add_access_group(self):
        name_access_group = 'Авто'
        self.element_is_visible(self.locators.MENU).click()
        self.element_is_visible(self.locators.ACCESS_GROUP).click()
        self.element_is_visible(self.locators.BUTTON_ADD_VISITORS).click()
        self.element_is_visible(self.locators.NAME_ACCESS_GROUP).send_keys(name_access_group)
        self.element_is_visible(self.locators.SAVE_AG).click()
        return name_access_group

    def add_my_application(self):
        last_name = 'Autotest '
        name_access_group = 'Авто'
        first_name = 'Test'
        self.element_is_visible(self.locators.MENU).click()
        self.element_is_visible(self.locators.MY_APPLICATION).click()
        self.element_is_visible(self.locators.BUTTON_ADD_VISITORS).click()
        time.sleep(2)
        element = self.element_is_visible(self.locators.BUTTON_DAWN_DROP).text
        time.sleep(2)
        self.element_is_visible(self.locators.BUTTON_DAWN_DROP).click()  # .send_keys(last_name)
        #print(f' Элемент - {element}') # пустое значение
        self.element_is_visible(self.locators.INPUT_VISITORS).click()  # иногда падает тут - понять в чем плавающая ошибка, возможно дело в локаторе
        #time.sleep(6)
        self.element_is_visible(self.locators.ACCESS_GROUP_IN_MY_APP).send_keys(name_access_group)
        #time.sleep(3)
        self.element_is_visible(self.locators.INPUT_ACCESS_GROUP_IN_MY_APP).click()
        self.element_is_visible(self.locators.BUTTON_IN_PROCESSING).click()
        #time.sleep(3)
        self.element_is_visible(self.locators.CLOSE_WINDOW_MY_APP).click()

    def open_incoming(self):
        #self.element_is_visible(self.locators.MENU).click()  # закомментить при необходимости
        self.element_is_visible(self.locators.INCOMING).click()
        self.element_is_visible(self.locators.FIRST_STRING_IN_TABLE).click()


    def agreement_application(self):
        self.element_is_visible(self.locators.AGREEMENT_BUTTON).click()
        number_pass = generated_pass_number()  # сделать рандомную генерацию
        #print(number_pass)


    def issue_pass(self):
        txt_1 = self.element_is_visible(self.locators.STATUS_AGREEMENT).text
        # print(txt_1) # написать функцию которая парсит текст и находит слово в []
        self.element_is_visible(self.locators.THREE_POINT_AGREEMENT).click()
        self.element_is_visible(self.locators.BUTTON_ISSUE_PASS).click()
        return txt_1
        # ТЕПЕРЬ МЫ ТУТ УРАААА
        #  сделать проверку если есть окно - то делаем согласие - если нет то идем сразу на выдачу

    def signing_receiving_pass(self, txt_1):
        # if self.parser_status(txt_1) == "Согласуется":
        #     # # approve согласие на новом пользаке
        #     self.element_is_visible(self.locators.BUTTON_OK_PATTERN_APPROVE).click()
        #     # ТЕПЕРЬ МЫ ТУТ УРАААА
        #     time.sleep(5)
        #     self.element_is_visible(self.locators.CHECK_BOX_APPROVE).click()  # не находит этот локатор (чек бокс)
        #     self.element_is_clickable(self.locators.CHECK_BOX_APPROVE).click()
        #     self.element_is_visible(self.locators.SAVE_APPROVE).click()
        # # выдача пропуска
        # # сделать рандомный выбор HEX / DEC
        time.sleep(5)
        #self.element_is_visible(self.locators.INPUT_NUMBER_PASS).send_keys(number_pass) # не отрабатывает
        self.element_is_visible(self.locators.BUTTON_OK_NUMBER_PASS).click()
        txt_3 = self.element_is_visible(self.locators.STATUS_AGREEMENT).text
        print(txt_3)
        self.element_is_visible(self.locators.CLOSE_WINDOW_MY_APP).click()
        #self.element_is_visible(self.locators.CLOSE_WINDOW_MY_APP).click()
        # статусы Согласуется - разрешено - обработано

    def reject_application(self):
        self.element_is_visible(self.locators.REJECT_BUTTON).click()

    def annul_application(self):
        self.element_is_visible(self.locators.ANNUL_BUTTON).click()

    def withdraw_pass(self):
        #url = 'http://localhost/listedData/passDictionaryActive'
        #open(url)
        self.element_is_visible(self.locators.BUTTON_ACTIVE_PASS).click()

        self.element_is_visible(self.locators.CHOOSE_FIRST_LINE).click()

        self.element_is_visible(self.locators.BUTTON_WITHDROW).click()

        self.element_is_visible(self.locators.BUTTON_OK_PATTERN_APPROVE).click()
        self.element_is_visible(self.locators.CLOSE_WINDOW_ACTIVATE_PASS).click()

    def copy_application(self):
        #открыть заявку которую копировать
        self.element_is_visible(self.locators.MENU).click()
        self.element_is_visible(self.locators.MY_APPLICATION).click()
        self.element_is_visible(self.locators.CHOOSE_FIRST_LINE).click()

        # copy
        self.element_is_visible(self.locators.COPY_APPLICATION_BUTTON).click()
        self.element_is_visible(self.locators.BUTTON_IN_PROCESSING).click()


        # перенести в другое
    def add_another_pass(self):
        self.element_is_visible(self.locators.AGREEMENT_BUTTON).click()
        self.element_is_visible(self.locators.THREE_POINT_AGREEMENT).click()
        self.element_is_visible(self.locators.BUTTON_ISSUE_ANOTHER_PASS).click()
        self.element_is_visible(self.locators.BUTTON_YES_PO).click()

    def check_pass(self):
        pass


    # def create_area(self):
    #     name = 'Площадка3'
    #     self.element_is_visible(self.locators.MENU).click()
    #     self.element_is_visible(self.locators.SETTINGS_OPERATOR).click()
    #     self.element_is_visible(self.locators.ROOT_SETTINGS).click()
    #     self.element_is_visible(self.locators.AREA).click()
    #     self.element_is_visible(self.locators.BUTTON_RADIO_CERTAIN).click()
    #     self.element_is_visible(self.locators.BUTTON_SAVE_AREA).click()
    #     # self.element_is_visible(self.locators.INPUT_NAME_AREA).click()
    #     # self.element_is_visible(self.locators.INPUT_NAME_AREA).send_keys(name)


    # def create_passage(self):
    #     name_readers = 'Считыватель_тест'
    #     name_passage = 'тп_тест'
    #     self.element_is_visible(self.locators.MENU).click()
    #     self.element_is_visible(self.locators.READERS).click()
    #     self.element_is_visible(self.locators.BUTTON_READERS_ADD).click()
    #     self.element_is_visible(self.locators.READERS_NAME).click()
    #     self.element_is_visible(self.locators.READERS_NAME).send_keys(name_readers)
    #     self.element_is_visible(self.locators.BUTTON_SAVE_READERS).click()
    #     self.element_is_visible(self.locators.PASSAGE_POINT).click()
    #     self.element_is_visible(self.locators.BUTTON_ADD_PASSAGE).click()
    #     self.element_is_visible(self.locators.BUTTON_NAME_PASSAGE).click()
    #     self.element_is_visible(self.locators.INPUT_NAME_PASSAGE).send_keys(name_passage)
    #     self.element_is_visible(self.locators.BUTTON_INPUT_READERS).click()
    #     self.element_is_visible(self.locators.INPUT_READERS_NAME).click()
    #     self.element_is_visible(self.locators.BUTTON_INPUT_OUTERS).click()
    #     self.element_is_visible(self.locators.INPUT_OUTERS_NAME).click()
    #     self.element_is_visible(self.locators.BUTTON_SAVE_PASSAGE).click()


    # def create_monitor(self):
    #     name='Монитор_тест'
    #     self.element_is_visible(self.locators.MENU).click()
    #     self.element_is_visible(self.locators.MONITOR).click()
    #     self.element_is_visible(self.locators.BUTTON_ADD_MONITOR).click()
    #     self.element_is_visible(self.locators.BUTTON_NAME_MONITOR).click()
    #     self.element_is_visible(self.locators.INPUT_NAME_MONITOR).send_keys(name)
    #     self.element_is_visible(self.locators.BUTTON_CHOOSE_PASSAGES).click()
    #     self.element_is_visible(self.locators.BUTTON_CHOOSE_PASSAGE).click()
    #     self.element_is_visible(self.locators.BUTTON_SAVE_PASSAGE).click()
    # def parser_status(txt):
    #     text = txt.split('[', 1)[1].split(']')[0]
    #     return text



