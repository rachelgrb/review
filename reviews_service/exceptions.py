# List of global exceptions


class NotFoundError(RuntimeError):
    """
    Object not found error
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class AlreadyExistError(RuntimeError):
    """
    Object already exists
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class ValidationError(RuntimeError):
    """
    Object has invalid data
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
