import time

import yaml
from module import Site

with open("testdata.yaml") as f:
    testdata = yaml.safe_load(f)

site = Site(testdata["address"])


# css_selector="span.mdc-text-field__ripple"
# print(site.get_element_property("css",css_selector,"height"))

def test_step1(x_selector_1, x_selector_2, x_selector_3, btn_selector, expected_result_1):
    input1 = site.find_element("xpath", x_selector_1)
    input1.send_keys("test")
    input2 = site.find_element("xpath", x_selector_2)
    input2.send_keys("test2")
    btn = site.find_element("css", btn_selector)
    btn.click()
    err_label = site.find_element("xpath", x_selector_3)
    result = err_label.text
    site.close()
    assert result == expected_result_1, 'test1 failed'


def test_step2(x_selector_1, x_selector_2, btn_selector, expected_result_1, x_selector_4,
               expected_result_2):
    site = Site(testdata["address"])
    time.sleep(2)
    input1 = site.find_element('xpath', x_selector_1)
    input1.clear()
    input1.send_keys(testdata['username'])
    input2 = site.find_element('xpath', x_selector_2)
    input2.clear()
    input2.send_keys(testdata['password'])
    btn_selector = 'button'
    btn = site.find_element('css', btn_selector)
    btn.click()
    time.sleep(2)
    link1 = site.find_element('xpath', x_selector_4)
    result = link1.text
    #res=site.close()

    assert result == expected_result_2, 'test2 failed'


def test_step3(btn_add_post, title_new_post, descr_new_post, content_new_post, btn_save_post, new_post_name):

    add_post = site.find_element('xpath', btn_add_post)
    add_post.click()
    time.sleep(5)
    inp_title = site.find_element('xpath', title_new_post)
    inp_title.clear()
    inp_title.send_keys(testdata["title"])
    input_desc = site.find_element('xpath', descr_new_post)
    input_desc.clear()
    input_desc.send_keys(testdata["description"])
    input_content = site.find_element('xpath', content_new_post)
    input_content.clear()
    input_content.send_keys(testdata["content"])
    btn_save = site.find_element('css', btn_save_post)
    btn_save.click()
    time.sleep(5)
    new_post_name = site.find_element('xpath', new_post_name)
    result = new_post_name.text
    site.close()

    assert result == testdata["title"], 'test3 failed'
