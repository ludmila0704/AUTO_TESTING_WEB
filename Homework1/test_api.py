import requests
import yaml

S = requests.Session()

with open("config.yaml", encoding='utf-8') as f:
    data = yaml.safe_load(f)
    address_posts = data['address_posts']


def test_create_post(get_token):
    res = S.post(url=address_posts, headers={'X-Auth-Token': get_token},
                 data={'title': 'sea', 'description': 'A sea is a large body',
                       'content': 'A sea is a large body|salt water that is surrounded'
                                  ' in whole or in part by land. More broadly, "the sea" '
                                  'is the interconnected system of Earths salty. '
                                  ' spring and foreshadows autumn.'})

    assert res.ok


def test_rest(get_token, post_description):
    res = S.get(url=address_posts, headers={'X-Auth-Token': get_token}).json()['data']
    r = [i['description'] for i in res]

    assert post_description in r
