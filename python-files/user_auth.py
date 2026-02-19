# User Authentication Module

class UserAuth:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def authenticate(self):
        # Sample authentication logic
        if self.username == 'admin' and self.password == 'password':
            return True
        return False

    def update_password(self, new_password):
        self.password = new_password

# Example usage:
if __name__ == '__main__':
    user = UserAuth('admin', 'password')
    if user.authenticate():
        print('Authenticated successfully!')
    else:
        print('Authentication failed.')
