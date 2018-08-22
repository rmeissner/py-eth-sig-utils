from ethereum import utils
from eth_abi import encode_single, encode_abi

def createStructDefinition(name, schema):
    schemaTypes = [ (schemaType['type'] + " " + schemaType['name']) for schemaType in schema ]
    return name + "(" + ",".join(schemaTypes) + ")"

def findDependencies(name, types, dependencies):
    if name in dependencies:
        return
    schema = types.get(name)
    if not schema:
        return
    dependencies.add(name)
    for schemaType in schema:
        findDependencies(schemaType['type'], types, dependencies)

def createSchema(name, types):
    arrayStart = name.find("[")
    cleanName = name if arrayStart < 0 else name[:arrayStart]
    dependencies = set()
    findDependencies(cleanName, types, dependencies)
    dependencies.discard(cleanName)
    dependencyDefinitions = [ createStructDefinition(dependency, types[dependency]) for dependency in sorted(dependencies) if types.get(dependency) ]
    return createStructDefinition(cleanName, types[cleanName]) + "".join(dependencyDefinitions)

def createSchemaHash(name, types):
    return encode_single('bytes32', utils.sha3(createSchema(name, types)))

def encodeValue(dataType, value, types):
    if (dataType == 'string'):
        return encode_single('bytes32', utils.sha3(value))
    elif (dataType == 'bytes'):
        return encode_single('bytes32', utils.sha3(utils.scan_bin(value)))
    elif (types.get(dataType)):
        return encode_single('bytes32', utils.sha3(encodeData(dataType, value, types)))
    elif (dataType.endswith("]")):
        arrayType = dataType[:dataType.index("[")]
        return encode_single('bytes32', utils.sha3(b"".join([ encodeData(arrayType, arrayValue, types) for arrayValue in value ])))
    else:
        return encode_single(dataType, value)

def logginEncodeValue(dataType, value, types):
    print(dataType, value, utils.encode_hex(encodeValue(dataType, value, types)), sep=" >>> ")
    return encodeValue(dataType, value, types)

def encodeData(name, data, types):
    return createSchemaHash(name, types) + b"".join([ encodeValue(schemaType['type'], data[schemaType['name']], types) for schemaType in types[name] ])

def createStructHash(name, data, types):
    return utils.sha3(encodeData(name, data, types))

def encodeTypedData(data):
    assert data
    types = data.get("types")
    assert types
    domainSchema = types.get("EIP712Domain")
    assert domainSchema and type(domainSchema) is list

    primaryType = data.get("primaryType")
    assert primaryType
    domain = data.get("domain")
    assert domain
    # TODO check domain object against schema
    message = data.get("message")
    assert message

    domainHash = createStructHash("EIP712Domain", domain, types)
    messageHash = createStructHash(primaryType, message, types)
    return utils.encode_hex(utils.sha3(bytes.fromhex('19') + bytes.fromhex('01') + domainHash + messageHash))