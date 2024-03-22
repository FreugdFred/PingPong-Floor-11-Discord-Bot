from dotenv import load_dotenv
import os


class MissingApiTokenError(Exception):
    pass


def get_api_key() -> str:
    """
    Retrieves the API token from the environment variables.

    Returns:
        str: The API token.

    Raises:
        MissingApiTokenError: If no API token is provided in the .env file.
    """
    load_dotenv()
    api_token = os.environ.get("TOKEN")

    if not api_token:
        raise MissingApiTokenError(
            "No API token provided, add an API token to the .env file"
        )

    return api_token
