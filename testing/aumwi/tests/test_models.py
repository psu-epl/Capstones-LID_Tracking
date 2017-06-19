# test_models.py

import pytest   # This is the test interpreter. Must install pytest to use.
pytestmark = pytest.mark.django_db  # Use pytest marks to tell pytest-django your test needs database access.
                                    # Must install pytest-django to use.
                                    # http://pytest-django.readthedocs.io/en/latest/database.html
from aumwi.models import User, ModuleList, AuthUser, UsageLog # mixer doesn't need this. For use with e.g. users = User.objects.all()
from django.test import TestCase # Allows use of assertEqual
from mixer.backend.django import mixer # Test fixture creator. Must install mixer.
from django.db import IntegrityError, transaction

class TestUser(TestCase):
    def test_init(self):
        obj = mixer.blend('aumwi.User')
        users = User.objects.all()
        self.assertEqual(len(users), 1), 'Should create a User instance.'

    def test_unique_fields(self): #Exception raised when the relational integrity of the database is affected
        with self.assertRaises(IntegrityError):
            # roll back transaction to a clean state before letting the IntegrityError bubble up
            with transaction.atomic():
                # This code executes inside a transaction.
                user1 = mixer.blend('aumwi.User', id = '5dad0428-1da1-4d6d-8cd2-ca88ad23a6f6')
                user2 = User(
                id = '5dad0428-1da1-4d6d-8cd2-ca88ad23a6f6',
                username = 'tinyrobotarmy',
                full_name = 'Your Mom',
                email = 'dontpantsme@gmail.com',
                rfid = 9223372036854775807,
                )
                user2.save(force_insert = True), 'Should raise IntegrityError: User.id'
        with self.assertRaises(IntegrityError):
            with transaction.atomic():
                user1 = mixer.blend('aumwi.User', username = 'SilverwareGolem')
                user2 = mixer.blend('aumwi.User', username = 'SilverwareGolem'),'Should raise IntegrityError: User.username'
        with self.assertRaises(IntegrityError):
            with transaction.atomic():
                user1 = mixer.blend('aumwi.User', email = 'dontpantsme@gmail.com')
                user2 = mixer.blend('aumwi.User', email = 'dontpantsme@gmail.com'),'Should raise IntegrityError: User.email'
        with self.assertRaises(IntegrityError):
            with transaction.atomic():
                user1 = mixer.blend('aumwi.User', rfid = '922337203685477580')
                user2 = mixer.blend('aumwi.User', rfid = '922337203685477580'), 'Should raise IntegrityError: User.rfid'

    def test_empty_fields(self): #Exception raised when the relational integrity of the database is affected
        '''
        I am not testing User.id here. This test does not work for the id,
        I think because the system is designed to assign one at the time of saving.
        '''
        with self.assertRaises(IntegrityError):
            # roll back transaction to a clean state before letting the IntegrityError bubble up
            with transaction.atomic():
                # This code executes inside a transaction.
                obj = mixer.blend('aumwi.User', username = None),'Should raise IntegrityError: User.username'
        with self.assertRaises(IntegrityError):
            with transaction.atomic():
                obj = mixer.blend('aumwi.User', email = None),'Should raise IntegrityError: User.email'
        with self.assertRaises(IntegrityError):
            with transaction.atomic():
                obj = mixer.blend('aumwi.User', rfid = None), 'Should raise IntegrityError: User.rfid'

class TestModuleList(TestCase):
    def test_init(self):
        obj = mixer.blend('aumwi.ModuleList')
        modules = ModuleList.objects.all()
        self.assertEqual(len(modules), 1), 'Should create a ModuleList instance.'

    def test_unique_fields(self): #Exception raised when the relational integrity of the database is affected
        with self.assertRaises(IntegrityError):
            # roll back transaction to a clean state before letting the IntegrityError bubble up
            with transaction.atomic():
                # This code executes inside a transaction.
                mod1 = mixer.blend('aumwi.ModuleList', id = 'b099ce7e-fa35-4a1c-a418-c0be75c677f9' )
                mod2 = ModuleList(
                id = 'b099ce7e-fa35-4a1c-a418-c0be75c677f9',
                smid = 9223372036854775800,
                name = 'Soldering Iron: Hunka Hunka Burning Metal'
                )
                mod2.save(force_insert = True), 'Should raise IntegrityError: ModuleList.id'

    def test_empty_fields(self): #Exception raised when the relational integrity of the database is affected
        '''
        I am not testing Module.id here. This test does not work for the id,
        I think because the system is designed to assign one at the time of saving.
        '''
        with self.assertRaises(IntegrityError):
            # roll back transaction to a clean state before letting the IntegrityError bubble up
            with transaction.atomic():
                # This code executes inside a transaction.
                obj = mixer.blend('aumwi.ModuleList', smid = None ), 'Should raise IntegrityError: ModuleList.smid'
        with self.assertRaises(IntegrityError):
            with transaction.atomic():
                obj = mixer.blend('aumwi.ModuleList', name = None ), 'Should raise IntegrityError: ModuleList.name'

class TestAuthUser(TestCase): # Must explicitly be given inputs
    def test_init(self):
        obj = mixer.blend('aumwi.AuthUser',
        user_id = 'f92f4747-7cd4-4afd-990b-8d0185370038',
        smid_id = 'a9147eda-ed55-4b9c-bff0-192a6d580a6b')
        a_user = AuthUser.objects.all()
        self.assertEqual(len(a_user), 1), 'Should create an AuthUser instance.'

class TestUsageLog(TestCase): # Must explicitly be given inputs
    def test_init(self):
        obj = mixer.blend('aumwi.UsageLog',
        user_id = '5dad0428-1da1-4d6d-8cd2-ca88ad23a6f6',
        smid_id = '087e4535-15dd-4381-a2f5-a2ba938ff880',
        )
        u_log = UsageLog.objects.all()
        self.assertEqual(len(u_log), 1), 'Should create a UsageLog instance.'
