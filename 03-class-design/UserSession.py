from datetime import datetime

# Does this meet the SRP?
class UserSession:
    """Represents information about the User and their Session"""

    def __init__(self, id, name, start_date):
        self.user_id = id
        self.username = name
        self.user_since = start_date
        self.session_start_time = datetime.now()
        self.inactive_session_expiry = 3000

    def __str__(self):
        return 'UserSession(' + self.user_id + ')'


class User:
    """ Represents information about the User"""

    def __init__(self, id, name, start_date):
        self.id = id
        self.name = name
        self.since = start_date

    def __str__(self):
        return 'User(' + self.user_id + ')'

class Session:
    """Represents information about the User's Session"""

    def __init__(self, user, start_date):
        self.user = user
        self.start_time = datetime.now()
        self.inactive_expiry = 3000

    def __str__(self):
        return 'Session(' + self.start_time + ')'

def main():
    print('Starting')
    session = UserSession('123', 'John', '23/09/2018')
    print(session)
    print('Done')


if __name__ == '__main__':
    main()