class User:
    def __init__(self, name, login, email, location, avatar_url):
        self.name = name if name else "None"
        self.login = login if login else "none"
        self.email = email if email else "None"
        self.location = location if location else "None"
        self.avatar_url = avatar_url if avatar_url else "None"

    def get_login(self):
        return self.login
        
    def __str__(self):
        return self.name + '\n' + \
               self.login + '\n' + \
               self.email + '\n' + \
               self.location + '\n' + \
               self.avatar_url + '\n'
