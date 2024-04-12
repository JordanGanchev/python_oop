import unittest

from project.social_media import SocialMedia


class TestSocialMedia(unittest.TestCase):
    def setUp(self) -> None:
        self.social = SocialMedia('dan', 'Instagram', 100, "people")

    def test_init_method(self):
        self.assertEqual('dan', self.social._username)
        self.assertEqual('Instagram', self.social._platform)


