import pytest


from application.app import create_app


@pytest.fixture
def app():
    """
    'app' object simulates an HTTP client that can access the API endpoints
    and store the responses of the server.
    """
    app = create_app("testing")

    return app
