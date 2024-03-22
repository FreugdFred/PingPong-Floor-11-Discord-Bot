from typing import Callable, Any
from services.message_data import MessageData

def admin_only(func: Callable) -> Callable:
    """
    Decorator to restrict access to a function to administrators only.

    Args:
        func (Callable): The function to be decorated.

    Returns:
        Callable: Decorated function with admin access check.
    """
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        """
        Wrapper function to check if the message author is an administrator.

        Args:
            *args: Positional arguments passed to the decorated function.
            **kwargs: Keyword arguments passed to the decorated function.

        Returns:
            Any: Result of the decorated function if the author is an administrator,
                 otherwise returns a message indicating lack of admin privileges.
        """
        message_data: MessageData = args[0]
        # Check if the message author is in the list of administrators
        if message_data.author not in message_data.admins:
            return "You are not an admin, suck on it!"

        # If the author is an admin, execute the decorated function
        result: Any = func(*args, **kwargs)
        return result

    return wrapper
