"""
Параметризация - выбор языка

1. Создайте GitHub-репозиторий, в котором будут лежать файлы conftest.py и test_items.py.
2. Добавьте в файл conftest.py обработчик, который считывает из командной строки параметр language.
3. Реализуйте в файле conftest.py логику запуска браузера с указанным языком пользователя.
Браузер должен объявляться в фикстуре browser и передаваться в тест как параметр.
4. В файл test_items.py напишите тест, который проверяет, что страница товара на сайте содержит кнопку добавления в корзину.
Например, можно проверять товар, доступный по http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/.
5. Тест должен запускаться с параметром language следующей командой:

pytest -sv --language=en test_items.py

6. Отправить ссылку на данный репозиторий в качестве ответа на данное задание.
7. Отправить решение на рецензирование другим учащимся. Решение на рецензирование можно отправить только один раз.
8. Проверьте решения минимум трех других учащихся, чтобы получить баллы за задание.
"""


link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_guest_should_see_btn_add_to_basket(browser):
    # test find button "Add to basket"
    browser.get(link)
    assert browser.find_element_by_css_selector(".btn-add-to-basket"), "Button not found."


"""
$ pytest -sv --tb=short --browser_name=firefox --language=en test_items.py 
================================================================== test session starts ===================================================================
platform linux -- Python 3.8.5, pytest-5.1.1, py-1.10.0, pluggy-0.13.1 -- /usr/bin/python3.8
cachedir: .pytest_cache
rootdir: /home/ku/Python/stepik/stepik_automation_test/Chapter3, inifile: pytest.ini
plugins: rerunfailures-9.1.1
collected 1 item                                                                                                                                         

Chapter3/les6_9_language_test/test_items.py::test_guest_should_see_btn_add_to_basket 
start test.. 
browser: firefox 
language: en
PASSED
quit browser..

=================================================================== 1 passed in 9.49s ====================================================================
"""
