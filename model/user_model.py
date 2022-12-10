class User:
    def __init__(self, user_id, name):
        self.__user_id = user_id
        self.__name = name

    def get_user_name(self):
        return self.__name

    def get_user_id(self):
        return self.__user_id

class TeamMember(User):
    def __init__(self, user_id, name):
        User.__init__(self, user_id, name)
        self.__role = "Developer"

    def get_user_role(self):
        return self.__role