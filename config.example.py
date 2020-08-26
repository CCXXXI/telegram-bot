from datetime import datetime

self_url = 'example.com'

# noinspection SpellCheckingInspection
token = '123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11'
safe_exec_api = 'http://example.com/safe_exec_api'


class ImgApi:
    def __init__(self, url: str):
        self.url = url
        self.sep = '?' if '?' not in self.url else '&'

    def get(self) -> str:
        return f"{self.url}{self.sep}timestamp={datetime.now().timestamp()}"


api_url_list = [
    'http://example.com/image_api',
]

img_api_list = list(map(ImgApi, api_url_list))

cheater_list = [
    'cheater语录',
]
