import importlib
import zlib
from google.protobuf.descriptor import FieldDescriptor
from testing_data import order_data, quora_data, user_data
import json


def load_proto_module(proto_module_name_arg):
    """Dynamically load a Protobuf module."""
    return importlib.import_module(proto_module_name_arg)


def create_message(proto_module_param, message_type_param):
    """Dynamically create a Protobuf message."""
    return getattr(proto_module_param, message_type_param)()


def set_message_fields(message, data):
    """Recursively set fields in a Protobuf message from a dictionary with error handling, including parsing nested JSON strings."""
    for key, value in data.items():
        if not hasattr(message, key):
            print(f"Warning: {key} is not a valid field of {message.DESCRIPTOR.name}")
            continue

        field_descriptor = message.DESCRIPTOR.fields_by_name[key]

        if field_descriptor.label == FieldDescriptor.LABEL_REPEATED:
            field = getattr(message, key)
            if not isinstance(value, list):
                print(f"Error: Field {key} is a repeated field, but a non-list value was provided")
                continue
            for item in value:
                if field_descriptor.type == FieldDescriptor.TYPE_MESSAGE:
                    if isinstance(item, str):
                        item = json.loads(item)
                    sub_message = field.add()
                    set_message_fields(sub_message, item)
                else:
                    field.append(item)
        elif field_descriptor.type == FieldDescriptor.TYPE_MESSAGE:
            field = getattr(message, key)
            if isinstance(value, str):
                value = json.loads(value)
            if isinstance(value, dict):
                set_message_fields(field, value)
            else:
                print(f"Error: Field {key} is a message type, but a non-dict value was provided")
        else:
            if value is None:
                setattr(message, key, "")
                continue
            setattr(message, key, value)

    return message


def serialize_message(message):
    """Serialize a Protobuf message to a compressed binary string."""
    return zlib.compress(message.SerializeToString())


def deserialize_message(proto_module, message_type, binary_data):
    """Deserialize a compressed binary string to a Protobuf message."""
    message = create_message(proto_module, message_type)
    message.ParseFromString(zlib.decompress(binary_data))
    return message


# Example usage:
# proto_module_name = 'app.grpc.generated.user_pb2'
proto_module_name = 'app.grpc.generated.quora_data_pb2'
message_type = 'TopLevelMessage'

# Load the module dynamically
proto_module = load_proto_module(proto_module_name)

# Example dictionary data

message = create_message(proto_module, message_type)

# Set fields dynamically from the dictionary
set_message_fields(message, quora_data)

# Serialize the message to a compressed binary string
binary_data = serialize_message(message)

# Deserialize the compressed binary string back to a message
deserialized_message = deserialize_message(proto_module, message_type, binary_data)

# print(type(deserialized_message))
print(deserialized_message)