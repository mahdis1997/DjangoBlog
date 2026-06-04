from django.contrib.auth import get_user_model
from django.test import TestCase
from .models import Post
from django.urls import reverse

# class BlogTests(TestCase):
#     @classmethod
#     def setUpTestData(cls):
#         cls.user = get_user_model().objects.create_user(
#             username="mah",email="m@y.com",password="123"
#         )
#         cls.post = Post.objects.create(
#             title ="AI",
#             body ="PYTHON WITH AI",
#             author =cls.user,
#         )
#     def test_post_model(self):
#             self.assertEqual(self.post.title, "AI")
#             self.assertEqual(self.post.body, "PYTHON WITH AI")
#             self.assertEqual(self.post.author.username, "mah")
#             self.assertEqual(str(self.post), "AI")
#             self.assertEqual(self.post.get_absolute_url(), "/post/1")

#     def test_url_exists_at_correct_location_listview(self): 
#         response = self.client.get("/")
#         self.assertEqual(response.status_code, 200)

#     def test_url_exists_at_correct_location_detailview(self): 
#         response = self.client.get("/post/1/")
#         self.assertEqual(response.status_code, 200)

#     def test_post_listview(self): 
#         response = self.client.get(reverse("home"))
#         self.assertEqual(response.status_code, 200)
#         self.assertContains(response, "PYTHON WITH AI")
#         self.assertTemplateUsed(response, "home.html")

#     def test_post_detailview(self): 
#         response = self.client.get(reverse("post_detail",
#         kwargs={"pk": self.post.pk}))
#         no_response = self.client.get("/post/100000/")
#         self.assertEqual(response.status_code, 200)
#         self.assertEqual(no_response.status_code, 404)
#         self.assertContains(response, "AI")
#         self.assertTemplateUsed(response, "post_detail.html")
# def test_post_createview(self): # new
#     response = self.client.post(
#         reverse("post_new"),
#             {
#             "title": "New title",
#             "body": "New text",
#             "author": self.user.id,
#             },
#     )
#     self.assertEqual(response.status_code, 302)
#     self.assertEqual(Post.objects.last().title, "New title")
#     self.assertEqual(Post.objects.last().body, "New text")
# def test_post_updateview(self): # new
#     response = self.client.post(
#         reverse("post_edit", args="1"),
#         {
#         "title": "Updated title",
#         "body": "Updated text",
#         },
# )
#     self.assertEqual(response.status_code, 302)
#     self.assertEqual(Post.objects.last().title, "Updated title")
#     self.assertEqual(Post.objects.last().body, "Updated text")

# def test_post_deleteview(self): # new
#     response = self.client.post(reverse("post_delete", args="1"))
#     self.assertEqual(response.status_code, 302)
from django.test import TestCase
from django.contrib.auth.models import User
from .models import Post

class PostModelTest(TestCase):
    def setUp(self):
        # ایجاد یک کاربر تستی
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
        
        # ایجاد یک پست تستی
        self.post = Post.objects.create(
            title='Test Post',
            author=self.user,
            body='This is a test post body.'
        )
    
    def test_post_creation(self):
        """آیا پست به درستی ساخته می‌شود؟"""
        self.assertEqual(self.post.title, 'Test Post')
        self.assertEqual(self.post.author.username, 'testuser')
        self.assertEqual(self.post.body, 'This is a test post body.')
    
    def test_post_str_method(self):
        """آیا متد __str__ درست کار می‌کند؟"""
        self.assertEqual(str(self.post), 'Test Post')
    
    def test_get_absolute_url(self):
        """آیا متد get_absolute_url درست کار می‌کند؟"""
        self.assertEqual(self.post.get_absolute_url(), f'/post/{self.post.id}/')