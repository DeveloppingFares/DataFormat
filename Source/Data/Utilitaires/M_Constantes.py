from enum import Enum


class E_Format(Enum):
    bitfield = "bitfield"
    buffer = "buffer"
    enumerate = "enumerate"
    field = "field"
    package = "package"
    processed = "processed"
    range = "range"
    reference = "reference"
    dependance = "dependance"

    @classmethod
    def from_str(cls, label):
        if label == 'bitfield':
            return cls.bitfield
        elif label == 'buffer':
            return cls.buffer
        elif label == 'enumerate':
            return cls.enumerate
        elif label == 'field':
            return cls.field
        elif label == 'package':
            return cls.package
        elif label == 'processed':
            return cls.processed
        elif label == 'range':
            return cls.range
        elif label == 'reference':
            return cls.reference
        elif label == 'dependance':
            return cls.dependance
        else:
            raise NotImplementedError


class E_Extension(Enum):
    JSON = ".json"

    @classmethod
    def from_str(cls, label):
        if label in ('.json', '.JSON'):
            return cls.JSON
        else:
            raise NotImplementedError
