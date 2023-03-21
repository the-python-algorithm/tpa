from the_python_algorithm.common.base_exception import (
    TPABaseException, TPACommonErrorTypes, TPAErrorNumbers, TPAErrorSeverity, TPAErrorCategory)


class SortingFilterFunctionException(TPABaseException):
    """
    Exception class raised when the filter function is None.
    """
    def __init__(self, msg=None):
        error_type = TPACommonErrorTypes.Invalid
        error_num = TPAErrorNumbers.NotNone
        severity = TPAErrorSeverity.ERR
        feature = TPAErrorCategory.Sorting
        msg_str = "Filter function cannot be empty. It defaults to <lambda x: x>"
        err_msg = "{}: {}".format(self.__class__.__name__, msg if msg else msg_str)
        super(SortingFilterFunctionException, self).__init__(
            err_msg, err_type=error_type, err_severity=severity, err_category=feature,
            err_number=error_num)


class IncorrectSortingDataException(TPABaseException):
    """
    Exception to be raised when the incorrect data in passed while performing sorting operation.
    """
    def __init__(self, msg=None):
        error_type = TPACommonErrorTypes.Invalid
        error_num = TPAErrorNumbers.NotNone
        severity = TPAErrorSeverity.ERR
        feature = TPAErrorCategory.Sorting
        msg_str = "Incorrect data passed, input data cannot be empty."
        err_msg = "{}: {}".format(self.__class__.__name__, msg if msg else msg_str)
        super(IncorrectSortingDataException, self).__init__(
            err_msg, err_type=error_type, err_severity=severity, err_category=feature,
            err_number=error_num)


class BubbleSortGenericException(TPABaseException):
    """
    Exception to be raised when the incorrect data in passed while performing sorting operation.
    """

    def __init__(self, msg=None):
        error_type = TPACommonErrorTypes.Invalid
        error_num = TPAErrorNumbers.NotNone
        severity = TPAErrorSeverity.ERR
        feature = TPAErrorCategory.Sorting
        msg_str = "Incorrect data passed, input data cannot be empty."
        err_msg = "{}: {}".format(self.__class__.__name__, msg if msg else msg_str)
        super(BubbleSortGenericException, self).__init__(
            err_msg, err_type=error_type, err_severity=severity, err_category=feature,
            err_number=error_num)
