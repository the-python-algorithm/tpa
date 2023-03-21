import ctypes

from enum import Enum, unique
from abc import ABCMeta, abstractmethod


@unique
class TPAErrorCategory(Enum):
    """
    An enum that defines the a unique value for each sub-module/feature in the TPA Project
    """
    Sorting = 0
    Searching = 1
    DataStructure = 2
    StringManipulation = 3
    BitOperation = 4
    Caching = 5


@unique
class TPAErrorSeverity(Enum):
    """
    An enum define the severity for each custom error class.
    """
    EMERG = 10
    ALERT = 11
    CRIT = 12
    ERR = 13
    WARNING = 14
    NOTICE = 15
    INFO = 16
    DEBUG = 17


@unique
class TPACommonErrorTypes(Enum):
    """
    An enum that list down the supported error types.
    """
    Invalid = 101
    Conflict = 102
    NotFound = 103
    AlreadyExist = 104
    Timeout = 106
    NotSupported = 107
    InternalError = 109


class _TPAErrorCodeBits(ctypes.Structure):
    """
    Class that define the structure for the error codes
    """
    _fields_ = [
        ("error_type", ctypes.c_uint8, 8),
        ("error_category", ctypes.c_uint8, 8),
        ("error_severity", ctypes.c_uint8, 8),
        ("error_number", ctypes.c_uint8, 8)
    ]


class _TPAErrorCode(ctypes.Union):
    """
    A union that generate a unique value for a specific error based upon the error bit fields.
    """
    __anonymous__ = ("bits",)
    __fields__ = [
        ("bits", _TPAErrorCodeBits),
        ("value", ctypes.c_uint32)
    ]

    def __init__(self, err_type, err_category, err_severity, err_number, *args, **kwargs):
        self.error_type = err_type
        self.error_category = err_category
        self.error_severity = err_severity
        self.error_number = err_number
        super().__init__(*args, **kwargs)


@unique
class TPAErrorNumbers(Enum):
    """
    An enum class that defines the subsequent error number based on the issue.
    """
    Unknown = 0
    InvalidValue = 1
    MissingArgs = 2
    NotNone = 3


class TPABaseException(Exception):
    """
    A base exception class for the entire TPA library. Every custom exception needs to implement
    the methods of this class. This class can be integrated with the DB to store the raised
    exceptions and their code for the future reference.
    """
    __metaclass__ = ABCMeta

    @abstractmethod
    def __init__(self, msg, err_type, err_severity, err_category, err_number):
        self.err_dict = {
            "errorType": err_type,
            "errorSeverity": err_severity,
            "errorCategory": err_category.name,
            "errorNumber": err_number
        }
        err_code = _TPAErrorCode(err_type=err_type,
                                 err_category=err_category,
                                 err_severity=err_severity,
                                 err_number=err_number)
        err_code = hex(err_code.value)

        # TODO: Add a mechanism that will push the exceptions to the database if available.
        #  We should implement a plugin based architecture for this.

        err_msg = "{} - {}".format(err_code, msg)
        super(TPABaseException, self).__init__(err_msg)
