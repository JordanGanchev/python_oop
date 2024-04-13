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

    def test_setter_followers(self):
        with self.assertRaises(ValueError) as content:
            self.social.followers = -1
        self.assertEqual("Followers cannot be negative.", str(content.exception))

    def test_platform_if_not_allowed_platforms(self):
        with self.assertRaises(ValueError) as content:
            self.social.platform = 'telegram'
        self.assertEqual(f"Platform should be one of ['Instagram', 'YouTube', 'Twitter']", str(content.exception))

    def test_create_post_content(self):
        self.social.create_post('test')
        self.assertEqual([{'content': 'test', 'likes': 0, 'comments': []}], self.social._posts)

    def test_create_post_content_return_message(self):
        result = self.social.create_post('test')
        self.social._content_type = 'str'
        self.social._platform = 'Instagram'
        self.assertEqual(f"New people post created by dan on Instagram.", result)

    def test_like_post_if_points_less_posts(self):
        self.assertEqual("Invalid post index.", self.social.like_post(2))

    def test_like_post_if_points_less_10(self):
        new_post = {'content': 'post_content', 'likes': 0, 'comments': []}
        self.social._posts.append(new_post)
        self.assertEqual(f"Post liked by dan.", self.social.like_post(0))

    def test_like_post_if_points_less_0(self):
        new_post = {'content': 'post_content', 'likes': 12, 'comments': []}
        self.social._posts.append(new_post)
        self.assertEqual(f"Post has reached the maximum number of likes.", self.social.like_post(0))

    def test_comment_on_post_if_more_than_10_characters(self):
        new_post = {'content': 'post_content', 'likes': 12, 'comments': []}
        self.social._posts.append(new_post)
        result = self.social.comment_on_post(0, 'asdfghjklio')
        self.assertEqual(f"Comment added by dan on the post.", result)

    def test_comment_on_post_if_less_than_10_characters(self):
        new_post = {'content': 'post_content', 'likes': 12, 'comments': []}
        self.social._posts.append(new_post)
        result = self.social.comment_on_post(0, 'asdfghj')
        self.assertEqual("Comment should be more than 10 characters.", result)