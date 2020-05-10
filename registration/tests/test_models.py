from django.test import TestCase
from django.db.utils import IntegrityError
from registration.models import User


class UserModelTest(TestCase):
    def test_user_creation(self):
        """
        Tests if a user is created successfully with the given parameters
        """
        user = User.objects.create(
            username='johndoe',
            first_name='John',
            last_name='Doe',
            email='johndoe@example.com',
        )
        self.assertIsInstance(user, User)
        self.assertEqual(user, User.objects.get(username='johndoe'))
        self.assertIs(user.username, 'johndoe')
        self.assertIs(user.first_name, 'John')
        self.assertIs(user.last_name, 'Doe')
        self.assertIs(user.email, 'johndoe@example.com')

    def test_does_not_allow_duplicate_username(self):
        User.objects.create(
            username='johndoe',
            first_name='John',
            last_name='Doe',
            email='johndoe@example.com',
        )
        with self.assertRaisesMessage(
            IntegrityError,
            'UNIQUE constraint failed: registration_user.username',
        ):
            User.objects.create(
                username='johndoe',
                first_name='John',
                last_name='Doe',
                email='johndoe2@example.com',
            )

    def test_does_not_allow_duplicate_email(self):
        User.objects.create(
            username='johndoe',
            first_name='John',
            last_name='Doe',
            email='johndoe@example.com',
        )
        with self.assertRaisesMessage(
            IntegrityError,
            'UNIQUE constraint failed: registration_user.email',
        ):
            User.objects.create(
                username='johndoe2',
                first_name='John',
                last_name='Doe',
                email='johndoe@example.com',
            )

    def test_saves_correct_hash_password(self):
        user = User.objects.create(
            username='johndoe',
            first_name='John',
            last_name='Doe',
            email='johndoe@example.com',
        )
        user.set_password('Du94nn3343434')
        user.save()
        self.assertTrue(user.check_password('Du94nn3343434'))
        self.assertNotEqual(user.password, 'Du94nn3343434')
        self.assertFalse(user.check_password('Eu94nn3343434'))
