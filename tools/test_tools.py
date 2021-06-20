import unittest
from os import chdir, pardir
from os import remove
from os.path import exists

import requests

from config import img_api_list
from plugins.eval import safe_eval
from plugins.exec import safe_exec
from plugins.solid_pic import gen_solid_pic, solid_pic_path
from tools import plugin_tools

chdir(pardir)


class TestPluginTools(unittest.TestCase):
    def test_plugin_tools(self):
        plugin_tools.load_plugins()
        self.assertTrue(plugin_tools.cmd_list)


class TestEvalExec(unittest.TestCase):
    def test_safe_eval(self):
        self.assertEqual(safe_eval(str({2, 0, 7, 7})), "{0, 2, 7}")
        self.assertEqual(safe_eval("1 + 1"), "operator no")

    def test_safe_exec(self):
        self.assertEqual(safe_exec("print(1 + 1)"), "2")
        self.assertEqual(safe_exec("__import__('os').system('whoami')"), "RuntimeError")


class TestPicture(unittest.TestCase):
    def test_solid_pic(self):
        if exists(solid_pic_path):
            remove(solid_pic_path)
        gen_solid_pic()
        self.assertTrue(exists(solid_pic_path))


class TestImgApi(unittest.TestCase):
    def test_img_api(self):
        for api in img_api_list:
            r = requests.get(api.get())
            self.assertEqual(r.status_code, 200)


if __name__ == "__main__":
    unittest.main()
