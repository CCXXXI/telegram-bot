import unittest

from requests import post

url = 'http://127.0.0.1:5000/'
test_q = 'Q test'
test_a = 'A test'


class ApiTest(unittest.TestCase):
    def test_api(self):
        r = post(url + 'get_q').json()
        self.assertFalse(any(q['q'] == test_q for q in r))

        post(url + 'add_q', json={'q': test_q})
        r = post(url + 'get_q', json={'q': test_q}).json()
        self.assertEqual(len(r), 1)
        r = r[0]
        self.assertEqual(r['q'], test_q)
        self.assertEqual(r['vote'], 0)

        post(url + 'vote_q_up', json={'q': test_q})
        r = post(url + 'get_q', json={'q': test_q}).json()
        self.assertEqual(r[0]['vote'], 1)

        r = post(url + 'get_a', json={'q': test_q}).json()
        self.assertFalse(r)

        post(url + 'add_a', json={'q': test_q, 'a': test_a})
        r = post(url + 'get_a', json={'q': test_q}).json()
        self.assertEqual(len(r), 1)
        r = r[0]
        self.assertEqual(r['q'], test_q)
        self.assertEqual(r['a'], test_a)
        self.assertEqual(r['vote'], 0)

        post(url + 'vote_a_down', json={'q': test_q, 'a': test_a})
        r = post(url + 'get_a', json={'q': test_q}).json()
        self.assertEqual(r[0]['vote'], -1)

        for _ in range(10):
            post(url + 'vote_a_down', json={'q': test_q, 'a': test_a})
        r = post(url + 'get_a', json={'q': test_q}).json()
        self.assertFalse(r)

        post(url + 'del_a', json={'q': test_q, 'a': test_a})
        post(url + 'del_q', json={'q': test_q})
        r = post(url + 'get_q', json={'q': test_q}).json()
        self.assertFalse(r)


if __name__ == '__main__':
    unittest.main()
