from django.test import TestCase
from user.models import User
from datetime import datetime,timedelta

# Create your tests here.
class TestArticleService(TestCase):
    def test_you_can_create_an_article_after_3minutes(self) -> None:
        join_date = user.join_date.date()
        now = (datetime.now() - timedelta(=3)).date()

        if join_date <= now:
            title = request.date.get('title', '')
            category = request.date.get('category', '')
            content = request.date.get('content', '')
            new_aricle = Article.objects.create(title=title, category=category, content=content, writer=user)
            return Response(new_aricle)
        # Given
        title = "test_title"

        # When
        article = create_an_article(title)

        # Then
        self.assertEqual(article.title, title)