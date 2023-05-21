from django.test import TestCase
from apps.users.models import User
from apps.blogs.models import Rating, Article
from .services import compute_user_similarity

class UserSimilarityTest(TestCase):
    def setUp(self):
        # Создание пользователей и оценок для тестирования
        self.user1 = User.objects.create(username='user1')
        self.user2 = User.objects.create(username='user2')
        self.user3 = User.objects.create(username='user3')

        article1 = Article.objects.create(title="Article 1", content="Content 1", owner=self.user1)
        article2 = Article.objects.create(title="Article 2", content="Content 2", owner=self.user1)
        article3 = Article.objects.create(title="Article 3", content="Content 3", owner=self.user1)

        # Создание оценок пользователей
        Rating.objects.create(user=self.user1, article=article1, rating=4)
        Rating.objects.create(user=self.user1, article=article2, rating=5)
        Rating.objects.create(user=self.user2, article=article1, rating=2)
        Rating.objects.create(user=self.user2, article=article2, rating=3)
        Rating.objects.create(user=self.user3, article=article2, rating=4)
        Rating.objects.create(user=self.user3, article=article3, rating=5)

    def test_user_similarity(self):
        # Вызов функции compute_user_similarity для тестирования
        similarities = compute_user_similarity(self.user1, [self.user2, self.user3])
        print(similarities)

        # Проверка ожидаемых результатов
        self.assertEqual(len(similarities), 2)
        self.assertEqual(similarities[0][1], self.user3.id)
        self.assertAlmostEqual(similarities[0][0], 1.0, places=4)
        self.assertEqual(similarities[1][1], self.user2.id)
        self.assertAlmostEqual(similarities[1][0], 0.9962405881956831, places=4)
