from django.test import TestCase
from .models import Profile, Image


class ProfileTest(TestCase):

    def setUp(self):
        self.new_profile = Profile(photo='image.png', bio='generous')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_profile, Profile))

    def test_save_method(self):
        self.new_profile.save_profile()
        profile = Profile.objects.all()
        self.assertTrue(len(profile)>0)

    def test_delete_method(self):
        self.new_profile.save_profile()
        self.new_profile.delete_profile()
        profile = Profile.objects.all()
        self.assertTrue(len(profile)==0)

    def test_update_profile(self):
        self.new_profile.save_profile()
        self.new_profile.update_bio(self.new_profile.id,'mySelf')
        updated_bio = Profile.objects.filter(bio="mySelf")
        self.assertTrue(len(updated_bio)>0)

    
