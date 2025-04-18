from datetime import datetime

import bcrypt


class User:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = self._hash_password(password)
        self.created_at = datetime.utcnow()

    def _hash_password(self, password):
        return bcrypt.hashpw(password.encode('utf-8'), self.password.encode('utf-8'))
