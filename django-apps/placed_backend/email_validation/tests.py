from datetime import datetime
from django.core import mail
from django.test import TestCase
from django.utils import timezone
from rest_framework.test import APITestCase
from email_validation.models import EmailValidation, EXPIRES_DAYS


class EmailValidationModelTestCase(TestCase):
    fixtures = ['data/user.json', 'data/group.json', 'data/emailvalidation.test.csv.json', 'data/users.csv.json',
    'data/course.json', 'data/people_list.json', 'data/module.json',
    'data/exemplar_project_proposal.json']

    def setUp(self):
        self.email_validation = EmailValidation.objects.get_info('lindsay.norman@geekwagon.info', 'df506515883ac02763da1399680578d9')

    def test_exist(self):
        result = EmailValidation.objects.exists('lindsay.norman@geekwagon.info', 'df506515883ac02763da1399680578d9')
        self.assertTrue(result)

    def test_get_info(self):
        self.assertIsInstance(self.email_validation, EmailValidation)

    def test_is_used(self):
        self.email_validation.used_by = self.email_validation.requested_by
        self.assertTrue(self.email_validation.is_used())

    def test_is_not_used(self):
        self.assertFalse(self.email_validation.is_used())

    def test_confirm(self):
        self.email_validation.confirm()
        self.assertTrue(self.email_validation.is_used())

        self.assertEqual(self.email_validation.used_by, self.email_validation.requested_by)

    def test_has_not_expired(self):
        self.assertFalse(self.email_validation.has_expired())

    def test_has_expired(self):
        self.email_validation.expires = datetime(2015, 1, 1, tzinfo=timezone.get_default_timezone())
        self.assertTrue(self.email_validation.has_expired())

    def test_set_expires(self):
        self.email_validation.set_expires()
        time_to_expire = self.email_validation.expires - timezone.now()
        self.assertGreaterEqual(EXPIRES_DAYS, time_to_expire.days)
        self.assertLessEqual(EXPIRES_DAYS-1, time_to_expire.days)

    def test_is_valid(self):
        self.assertTrue(self.email_validation.is_valid())

    def test_is_not_valid_because_is_used(self):
        self.email_validation.used_by = self.email_validation.requested_by
        self.assertFalse(self.email_validation.is_valid())

    def test_is_not_valid_because_has_expired_and_is_used(self):
        self.email_validation.expires = datetime(2015, 1, 1, tzinfo=timezone.get_default_timezone())
        self.email_validation.used_by = self.email_validation.requested_by
        self.assertFalse(self.email_validation.is_valid())

    def test_is_not_valid_because_has_expired(self):
        self.email_validation.expires = datetime(2015, 1, 1, tzinfo=timezone.get_default_timezone())
        self.assertFalse(self.email_validation.is_valid())

    def test_check_email_and_code_is_valid(self):
        result = EmailValidation.objects.is_valid('lindsay.norman@geekwagon.info', 'df506515883ac02763da1399680578d9')
        self.assertTrue(result)

    def test_email(self):
        self.email_validation.send_mail()
        self.assertEqual(len(mail.outbox), 1)
        # Verify that the subject of the first message is correct.
        self.assertEqual(mail.outbox[0].subject, 'Placed Invitation')
        self.assertEqual(mail.outbox[0].to[0], self.email_validation.email)


class EmailValidationAPITestCase(APITestCase):
    pass
