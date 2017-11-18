from DatabaseController import MongoController

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
        return self.name.encode('ascii', 'ignore').decode('ascii') + '\n' + \
               self.login.encode('ascii', 'ignore').decode('ascii') + '\n' + \
               self.email.encode('ascii', 'ignore').decode('ascii') + '\n' + \
               self.location.encode('ascii', 'ignore').decode('ascii') + '\n' + \
               self.avatar_url.encode('ascii', 'ignore').decode('ascii') + '\n'

    def save_user(self):
        user = {"name": self.name,
                "login": self.login,
                "email": self.email,
                "location": self.location,
                "avatar_url": self.avatar_url}

        MongoController.MongoController.get_instance().save_user(user)
