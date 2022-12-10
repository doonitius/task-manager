from model.user_model import User,TeamMember

def user_login(user_id, user_name):
    user = TeamMember(user_id, user_name)

    print("Hello,", user.get_user_name(), user.get_user_role())

    return user

def get_user_info(user):
    
    print(user.get_user_name(), user.get_user_role())

    return user.get_user_name(),user.get_user_role()