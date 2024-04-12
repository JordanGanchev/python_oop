import unittest

from project.social_media import SocialMedia


class TestSocialMedia(unittest.TestCase):
    def setUp(self) -> None:
        self.social = SocialMedia('dan', 'Instagram', 100, "people")

    def test_init_method(self):
        self.assertEqual('dan', self.social._username)
        self.assertEqual('Instagram', self.social._platform)
        self.assertEqual(None, self.social._validate_and_set_platform('Instagram'))
        self.assertEqual(100, self.social.followers)
        self.assertEqual('people', self.social._content_type)
        self.assertEqual([], self.social._posts)

    def test_platform_if_not_allowed_platforms(self)
        pass:
