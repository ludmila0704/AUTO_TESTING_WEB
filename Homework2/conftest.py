import pytest
import yaml

with open('testdata.yaml', encoding='utf-8') as f:
    userdata = yaml.safe_load(f)
    username = userdata['username']


@pytest.fixture()
def x_selector_1():
    return """//*[@id="login"]/div[1]/label/input"""


@pytest.fixture()
def x_selector_2():
    return """//*[@id="login"]/div[2]/label/input"""


@pytest.fixture()
def x_selector_3():
    return """//*[@id="app"]/main/div/div/div[2]/h2"""


@pytest.fixture()
def btn_selector():
    return 'button'


@pytest.fixture()
def expected_result_1():
    return '401'


@pytest.fixture()
def x_selector_4():
    return """//*[@id="app"]/main/nav/ul/li[3]/a"""


@pytest.fixture()
def expected_result_2():
    return f'Hello, {username}'


@pytest.fixture()
def btn_add_post():  # btn  +
    return """#create-btn"""


@pytest.fixture()
def title_new_post():
    return '//*[@id="create-item"]/div/div/div[1]/div/label/input'


@pytest.fixture()
def descr_new_post():
    return """//*[@id="create-item"]/div/div/div[2]/div/label/span/textarea"""


@pytest.fixture()
def content_new_post():
    return """//*[@id="create-item"]/div/div/div[3]/div/label/span/textarea"""


@pytest.fixture()
def btn_save_post():
    return """.mdc-button__label"""


@pytest.fixture()
def new_post_name():  # проверяем титл
    return """//*[@id="app"]/main/div/div[1]/h1"""
# Название поста на странице поста сразу после его создания

