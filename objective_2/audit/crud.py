from audit.models import UserRoles, Users

def create_user(role_id, username, password, nickname, location, email):
    try:
        role = UserRoles.objects.get(roleID=role_id)
    except UserRoles.DoesNotExist:
        raise Exception('Invalid roleID')
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

def read_user(id):
    try:
        user = Users.objects.get(pk=id)
    except Users.DoesNotExist:
        raise Exception('User does not exist.')
    return user

def update_user(id, key, value):
    user = read_user(id)
    user.update(key=value)

def delete_user(id):
    user = read_user(id)
    user.delete()
    return True