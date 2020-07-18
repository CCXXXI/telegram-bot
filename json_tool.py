import json


def test_conf():
    with open('config.json') as f:
        conf: dict = json.load(f)
        print(f'{conf=}')


def get_conf(name: str):
    with open('config.json') as f:
        conf: dict = json.load(f)
        return conf[name]


def set_conf(name: str, value):
    with open('config.json', 'r') as f:
        conf: dict = json.load(f)
    conf[name] = value
    with open('config.json', 'w') as f:
        f.write(json.dumps(conf))


test_conf()
if __name__ == '__main__':
    pass
