from users.models import UserRoles, Users

def create_user(role_id, username, password, nickname, location, email):

    try:
        role = UserRoles.objects.get(roleID=role_id)
    except UserRoles.DoesNotExist:
        raise Exception('Invalid roleID')

    # Create a new User object
    user = Users(
        roleID=role,
        username=username,
        password=password,
        nickname=nickname,
        location=location,
        email=email
    )
    
    user.save()
    
    return user