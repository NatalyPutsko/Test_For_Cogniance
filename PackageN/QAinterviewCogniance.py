import requests
import unittest
import json
from random import choice

DEFAULT_HEADER = 'application/json'

SUCCESS = 200
ADDED = 201
INCORRECT_HEADER = 400
NOT_FOUND = 404

NAME = ('A. N.', 'E. V.', 'D. B.', 'Z. T.', 'M. G.')
POSITION = ('intern1', "intern2", 'intern3', 'intern4', 'intern5')


class TestQainteviewCogniance(unittest.TestCase):
    def __init__(self, *a, **kw):
        super(TestQainteviewCogniance, self).__init__(*a, **kw)
        self.host = 'qainterview.cogniance.com'
        self.process = 'candidates'
        self.url = 'http://{}/{}'.format(self.host, self.process)

    def test_new_account(self):
        name = "{}".format(choice(NAME))
        position = "{}".format(choice(POSITION))
        kwargs = {'name': name, 'position': position}
        response_code, text = self._new_account(**kwargs)
        self.assertEqual(response_code, ADDED)
        self.assertIn(name, self._give_list_of_candidates('name'))

    def test_for_retrieving(self):
        response_code, accounts = self._get_accounts()
        self.assertEqual(response_code, SUCCESS)
        self.assertGreater(len(accounts.get('candidates')), 1)

        response_code, account = self._get_accounts(identificator=10)
        self.assertEqual(response_code, SUCCESS)
        self.assertTrue(isinstance(account.get('candidate'), dict))

    def test_for_incorrect_header(self):
        kwargs = {'name': '', 'position': '', 'headers': None}
        response_code, text = self._new_account(**kwargs)
        self.assertEqual(response_code, INCORRECT_HEADER)

    def test_for_deletion(self):
        identificator = choice(self._give_list_of_candidates('cand_id'))
        response_code, text = self._deletion_of_account(identificator)
        self.assertEqual(response_code, NOT_FOUND)
        self.assertIn(identificator, self._give_list_of_candidates('cand_id'))

    def _get_accounts(self, identificator=None):
        _url = self.url
        if identificator:
            _url = "{}/{}".format(self.url, identificator)
        _response = requests.get(_url)
        return _response.status_code, _response.json()

    def _give_list_of_candidates(self, key):
        _, data = self._get_accounts()
        return map(lambda x: x.get(key), data.get('candidates'))

    def _new_account(self, name, position, headers=DEFAULT_HEADER):
        _headers = {'content-type': headers}
        _payload = json.dumps({'name': name, 'position': position})
        _response = requests.post(self.url, data=_payload, headers=_headers)
        return _response.status_code, _response.json()

    def _deletion_of_account(self, identificator):
        _response = requests.delete("{}/{}".format(self.url, identificator))
        return _response.status_code, _response.json()


suite = unittest.TestLoader().loadTestsFromTestCase(TestQainteviewCogniance)
unittest.TextTestRunner(verbosity=2).run(suite)
