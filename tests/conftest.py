import pytest
from app.models.user import User


@pytest.fixture
def auth(client):
    class AuthActions:
        def login(self, username='azeez', password='mangowankillme'):
            if not User.find_by_username(username):
                User.create(username, 'azeezmuhammad24423@gmail.com', password)

            return client.post('/auth/login', json={
                'username': username,
                'password': password
            })

        def logout(self):
            return client.get('/auth/logout')

    return AuthActions()