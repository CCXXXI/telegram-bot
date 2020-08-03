import unittest
from os import chdir, pardir

chdir(pardir)


class TestPluginTools(unittest.TestCase):
    def test_plugin_tools(self):
        from tools import plugin_tools
        plugin_tools.load_plugins()
        for cmd in plugin_tools.cmd_list:
            print(*cmd.command)
        self.assertTrue(plugin_tools.cmd_list)


if __name__ == '__main__':
    unittest.main()
