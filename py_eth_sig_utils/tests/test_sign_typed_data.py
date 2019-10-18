import unittest
from .. import utils
from ..signing import *

class TestSignTypedData(unittest.TestCase):

    data = {
        "types": {
            "EIP712Domain": [
                { "name": 'name', "type": 'string' },
                { "name": 'version', "type": 'string' },
                { "name": 'chainId', "type": 'uint256' },
                { "name": 'verifyingContract', "type": 'address' },
            ],
            "Person": [
                { "name": 'name', "type": 'string' },
                { "name": 'wallet', "type": 'address' }
            ],
            "Mail": [
                { "name": 'from', "type": 'Person' },
                { "name": 'to', "type": 'Person' },
                { "name": 'contents', "type": 'string' }
            ]
        },
        "primaryType": 'Mail',
        "domain": {
            "name": 'Ether Mail',
            "version": '1',
            "chainId": 1,
            "verifyingContract": '0xCcCCccccCCCCcCCCCCCcCcCccCcCCCcCcccccccC',
        },
        "message": {
            "from": {
                "name": 'Cow',
                "wallet": '0xCD2a3d9F938E13CD947Ec05AbC7FE734Df8DD826',
            },
            "to": {
                "name": 'Bob',
                "wallet": '0xbBbBBBBbbBBBbbbBbbBbbbbBBbBbbbbBbBbbBBbB',
            },
            "contents": 'Hello, Bob!',
        },
    }

    def test_sign(self):
        private_key = utils.sha3('cow')
        signature = v_r_s_to_signature(*sign_typed_data(self.data, private_key)).hex()
        self.assertEqual(signature, '4355c47d63924e8a72e509b65029052eb6c299d53a04e167c5775fd466751c9d07299936d304c153f6443dfa05f40ff007d72911b6f72307f996231605b915621c')

    def test_recover(self):
        signer_address = recover_typed_data(self.data, *signature_to_v_r_s(bytes.fromhex('4355c47d63924e8a72e509b65029052eb6c299d53a04e167c5775fd466751c9d07299936d304c153f6443dfa05f40ff007d72911b6f72307f996231605b915621c')))
        self.assertEqual('0xCD2a3d9F938E13CD947Ec05AbC7FE734Df8DD826', signer_address)

if __name__ == '__main__':
    unittest.main()