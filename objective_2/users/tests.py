from django.test import TestCase
from .crud import create_user
from users.models import UserRoles, Users

class CreateUserTestCase(TestCase):
    
    def test_create_user(self):
        role = UserRoles.objects.create(roleID=99, roleName='TestRole')
        
        created_user = create_user(
            role_id=role.roleID,
            username='testuser',
            password='password123',
            nickname='Test User',
            location='Test Location',
            email='test@example.com'
        )
        
        retrieved_user = Users.objects.get(username='testuser')
        
        self.assertEqual(created_user, retrieved_user)
        self.assertEqual(retrieved_user.nickname, 'Test User')
        self.assertEqual(retrieved_user.location, 'Test Location')
        self.assertEqual(retrieved_user.email, 'test@example.com')
