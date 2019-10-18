from .. import utils
from eth_abi import encode_single, encode_abi

def create_struct_definition(name, schema):
    schemaTypes = [ (schemaType['type'] + " " + schemaType['name']) for schemaType in schema ]
    return name + "(" + ",".join(schemaTypes) + ")"

def find_dependencies(name, types, dependencies):
    if name in dependencies:
        return
    schema = types.get(name)
    if not schema:
        return
    dependencies.add(name)
    for schemaType in schema:
        find_dependencies(schemaType['type'], types, dependencies)

def create_schema(name, types):
    arrayStart = name.find("[")
    cleanName = name if arrayStart < 0 else name[:arrayStart]
    dependencies = set()
    find_dependencies(cleanName, types, dependencies)
    dependencies.discard(cleanName)
    dependencyDefinitions = [ create_struct_definition(dependency, types[dependency]) for dependency in sorted(dependencies) if types.get(dependency) ]
    return create_struct_definition(cleanName, types[cleanName]) + "".join(dependencyDefinitions)

def create_schema_hash(name, types):
    return encode_single('bytes32', utils.sha3(create_schema(name, types)))

def encode_value(dataType, value, types):
    if (dataType == 'string'):
        return encode_single('bytes32', utils.sha3(value))
    elif (dataType == 'bytes'):
        return encode_single('bytes32', utils.sha3(utils.scan_bin(value)))
    elif (types.get(dataType)):
        return encode_single('bytes32', utils.sha3(encode_data(dataType, value, types)))
    elif (dataType.endswith("]")):
        arrayType = dataType[:dataType.index("[")]
        return encode_single('bytes32', utils.sha3(b"".join([ encode_data(arrayType, arrayValue, types) for arrayValue in value ])))
    else:
        return encode_single(dataType, value)

def encode_data(name, data, types):
    return create_schema_hash(name, types) + b"".join([ encode_value(schemaType['type'], data[schemaType['name']], types) for schemaType in types[name] ])

def create_struct_hash(name, data, types):
    return utils.sha3(encode_data(name, data, types))

def encode_typed_data(data):
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

    domainHash = create_struct_hash("EIP712Domain", domain, types)
    messageHash = create_struct_hash(primaryType, message, types)
    return utils.sha3(bytes.fromhex('19') + bytes.fromhex('01') + domainHash + messageHash)