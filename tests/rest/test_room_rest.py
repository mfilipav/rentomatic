import json
from unittest import mock

from rentomatic.domain.room import Room

room_dict = {
    "code": "3251a5bd-86be-428d-8ae9-6e51a8048c33",
    "size": 200,
    "price": 10,
    "longitude": -0.09998975,
    "latitude": 51.75436293,
}

rooms = [Room.from_dict(room_dict)]


@mock.patch("application.rest.room.room_list_use_case")
def test_get(mock_use_case, client):
    mock_use_case.return_value = rooms

    # 'client' is a fixture which is one of the fixtures provided by 
    # pytest-flask, automatically loads 'app' from 'conftest.py'
    http_response = client.get("/rooms")

    # client object simulates an HTTP client that can access the 
    # API endpoints and store the responses of the server
    response = json.loads(http_response.data.decode("UTF-8"))
    print('response:\n', response)
    assert response == [room_dict]
    mock_use_case.assert_called()
    assert http_response.status_code == 200
    assert http_response.mimetype == "application/json"