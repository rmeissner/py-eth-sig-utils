from ethereum import utils
from main import *

def testSignTypeData():
    print("Test Simple")
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
    #print(createSchema("Mail", data["types"]))
    assert 'Mail(Person from,Person to,string contents)Person(string name,address wallet)' == createSchema("Mail", data["types"])
    #print(utils.encode_hex(createSchemaHash("Mail", data["types"])))
    assert 'a0cedeb2dc280ba39b857546d74f5549c3a1d7bdc2dd96bf881f76108e23dac2' == utils.encode_hex(createSchemaHash("Mail", data["types"]))
    #print(utils.encode_hex(encodeData(data["primaryType"], data["message"], data["types"])))
    assert 'a0cedeb2dc280ba39b857546d74f5549c3a1d7bdc2dd96bf881f76108e23dac2fc71e5fa27ff56c350aa531bc129ebdf613b772b6604664f5d8dbe21b85eb0c8cd54f074a4af31b4411ff6a60c9719dbd559c221c8ac3492d9d872b041d703d1b5aadf3154a261abdd9086fc627b61efca26ae5702701d05cd2305f7c52a2fc8' == utils.encode_hex(encodeData(data["primaryType"], data["message"], data["types"]))
    #print(utils.encode_hex(createStructHash(data["primaryType"], data["message"], data["types"])))
    assert 'c52c0ee5d84264471806290a3f2c4cecfc5490626bf912d01f240d7a274b371e' == utils.encode_hex(createStructHash(data["primaryType"], data["message"], data["types"]))
    #print(utils.encode_hex(createStructHash('EIP712Domain', data["domain"], data["types"])))
    assert 'f2cee375fa42b42143804025fc449deafd50cc031ca257e0b194a650a912090f' == utils.encode_hex(createStructHash('EIP712Domain', data["domain"], data["types"]))
    #print(encodeTypedData(data))
    assert 'be609aee343fb3c4b28e1df9e632fca64fcfaede20f02e86244efddf30957bd2' == encodeTypedData(data)

def testSignTypeDataArray():
    print("Test Arrays")
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
                { "name": 'to', "type": 'Person[]' },
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
            "to": [{
                "name": 'Bob',
                "wallet": '0xbBbBBBBbbBBBbbbBbbBbbbbBBbBbbbbBbBbbBBbB',
            }],
            "contents": 'Hello, Bob!',
        }, 
    }

    #print(createSchema("Mail", data["types"]))
    assert 'Mail(Person from,Person[] to,string contents)Person(string name,address wallet)' == createSchema("Mail", data["types"])
    #print(utils.encode_hex(createSchemaHash("Mail", data["types"])))
    assert 'dd57d9596af52b430ced3d5b52d4e3d5dccfdf3e0572db1dcf526baad311fbd1' == utils.encode_hex(createSchemaHash("Mail", data["types"]))
    #print(utils.encode_hex(encodeData(data["primaryType"], data["message"], data["types"])))
    assert 'dd57d9596af52b430ced3d5b52d4e3d5dccfdf3e0572db1dcf526baad311fbd1fc71e5fa27ff56c350aa531bc129ebdf613b772b6604664f5d8dbe21b85eb0c8cd54f074a4af31b4411ff6a60c9719dbd559c221c8ac3492d9d872b041d703d1b5aadf3154a261abdd9086fc627b61efca26ae5702701d05cd2305f7c52a2fc8' == utils.encode_hex(encodeData(data["primaryType"], data["message"], data["types"]))
    #print(utils.encode_hex(createStructHash(data["primaryType"], data["message"], data["types"])))
    assert '25192142931f380985072cdd991e37f65cf8253ba7a0e675b54163a1d133b8ca' == utils.encode_hex(createStructHash(data["primaryType"], data["message"], data["types"]))
    #print(utils.encode_hex(createStructHash('EIP712Domain', data["domain"], data["types"])))
    assert 'f2cee375fa42b42143804025fc449deafd50cc031ca257e0b194a650a912090f' == utils.encode_hex(createStructHash('EIP712Domain', data["domain"], data["types"]))
    #print(encodeTypedData(data))
    assert '0659335d0565297a1855731b0382d06cda439ea8e352de57c6f6499436a2b84e' == encodeTypedData(data)

def testSignTypeDataArrayBytes():
    print("Test Arrays and Bytes")
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
                { "name": 'to', "type": 'Person[]' },
                { "name": 'contents', "type": 'string' },
                { "name": 'payload', "type": 'bytes' }
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
            "to": [{
                "name": 'Bob',
                "wallet": '0xbBbBBBBbbBBBbbbBbbBbbbbBBbBbbbbBbBbbBBbB',
            }],
            "contents": 'Hello, Bob!',
            "payload": '0x25192142931f380985072cdd991e37f65cf8253ba7a0e675b54163a1d133b8ca'
        }, 
    }

    #print(createSchema("Mail", data["types"]))
    assert 'Mail(Person from,Person[] to,string contents,bytes payload)Person(string name,address wallet)' == createSchema("Mail", data["types"])
    #print(utils.encode_hex(createSchemaHash("Mail", data["types"])))
    assert '3dddc94d13b9ebab8e68f1428610e81839fcd751bdee402b12d2b3de3aace1fd' == utils.encode_hex(createSchemaHash("Mail", data["types"]))
    #print(utils.encode_hex(encodeData(data["primaryType"], data["message"], data["types"])))
    assert '3dddc94d13b9ebab8e68f1428610e81839fcd751bdee402b12d2b3de3aace1fdfc71e5fa27ff56c350aa531bc129ebdf613b772b6604664f5d8dbe21b85eb0c8cd54f074a4af31b4411ff6a60c9719dbd559c221c8ac3492d9d872b041d703d1b5aadf3154a261abdd9086fc627b61efca26ae5702701d05cd2305f7c52a2fc8fac776d21ae071a32c362d4c20ba6586779708a56cad3a78d01b37ecb5744298' == utils.encode_hex(encodeData(data["primaryType"], data["message"], data["types"]))
    #print(utils.encode_hex(createStructHash(data["primaryType"], data["message"], data["types"])))
    assert '813d832c9580a8bb0d4e2f5e85eb4466ef05a6ddaae7c020800da77fb573fe4e' == utils.encode_hex(createStructHash(data["primaryType"], data["message"], data["types"]))
    #print(utils.encode_hex(createStructHash('EIP712Domain', data["domain"], data["types"])))
    assert 'f2cee375fa42b42143804025fc449deafd50cc031ca257e0b194a650a912090f' == utils.encode_hex(createStructHash('EIP712Domain', data["domain"], data["types"]))
    #print(encodeTypedData(data))
    assert '78b9817f84906558ebb57f26f079e66887f444978b98d09e68a3468d48492f85' == encodeTypedData(data)

def testSignTypeDataBytes():
    print("Test Bytes")
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
                { "name": 'contents', "type": 'string' },
                { "name": 'payload', "type": 'bytes' }
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
            "payload": '0x25192142931f380985072cdd991e37f65cf8253ba7a0e675b54163a1d133b8ca'
        }, 
    }

    #print(createSchema("Mail", data["types"]))
    assert 'Mail(Person from,Person to,string contents,bytes payload)Person(string name,address wallet)' == createSchema("Mail", data["types"])
    #print(utils.encode_hex(createSchemaHash("Mail", data["types"])))
    assert '43999c52db673245777eb64b0330105de064e52179581a340a9856c32372528e' == utils.encode_hex(createSchemaHash("Mail", data["types"]))
    #print(utils.encode_hex(encodeData(data["primaryType"], data["message"], data["types"])))
    assert '43999c52db673245777eb64b0330105de064e52179581a340a9856c32372528efc71e5fa27ff56c350aa531bc129ebdf613b772b6604664f5d8dbe21b85eb0c8cd54f074a4af31b4411ff6a60c9719dbd559c221c8ac3492d9d872b041d703d1b5aadf3154a261abdd9086fc627b61efca26ae5702701d05cd2305f7c52a2fc8fac776d21ae071a32c362d4c20ba6586779708a56cad3a78d01b37ecb5744298' == utils.encode_hex(encodeData(data["primaryType"], data["message"], data["types"]))
    #print(utils.encode_hex(createStructHash(data["primaryType"], data["message"], data["types"])))
    assert 'e004bdc1ca57ba9ad5ea8c81e54dcbdb3bfce2d1d5ad92113f0871fb2a6eb052' == utils.encode_hex(createStructHash(data["primaryType"], data["message"], data["types"]))
    #print(utils.encode_hex(createStructHash('EIP712Domain', data["domain"], data["types"])))
    assert 'f2cee375fa42b42143804025fc449deafd50cc031ca257e0b194a650a912090f' == utils.encode_hex(createStructHash('EIP712Domain', data["domain"], data["types"]))
    #print(encodeTypedData(data))
    assert 'b4aaf457227fec401db772ec22d2095d1235ee5d0833f56f59108c9ffc90fb4b' == encodeTypedData(data)

testSignTypeData()
testSignTypeDataArray()
testSignTypeDataBytes()
testSignTypeDataArrayBytes()