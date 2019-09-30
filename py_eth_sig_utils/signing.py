from . import utils
from eth_utils import big_endian_to_int
from .eip712 import encode_typed_data

def signature_to_v_r_s(signature):
    v = utils.safe_ord(signature[64])
    r = big_endian_to_int(signature[0:32])
    s = big_endian_to_int(signature[32:64])
    return v, r, s

def v_r_s_to_signature(v, r, s):
    return r.to_bytes(32, 'big') + s.to_bytes(32, 'big') + v.to_bytes(1, 'big')

def sign_typed_data(data, private_key):
    msg_hash = encode_typed_data(data)
    return utils.ecsign(msg_hash, private_key)

def recover_typed_data(data, v, r, s):
    msg_hash = encode_typed_data(data)
    public_key = utils.ecrecover_to_pub(msg_hash, v, r, s)
    address_bytes = utils.sha3(public_key)[-20:]
    return utils.checksum_encode(address_bytes)