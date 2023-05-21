from apps.blogs.models import Rating
from numpy import dot
from numpy.linalg import norm

def compute_user_similarity(user, other_users):
    """
    A function that calculates the similarity between users.

    It takes a user object and a list of other user objects as an argument.
    Returns a sorted list in descending similarity list of tuples.
    Tuples consist of a number denoting similarity and user id.
    """

    ratings_user = Rating.objects.filter(user=user)
    ratings_dict_user = {rating.article.id: rating.rating for rating in ratings_user}

    similarities = []

    for other_user in other_users:
        ratings_other_user = Rating.objects.filter(user=other_user)
        ratings_dict_other_user = {rating.article.id: rating.rating for rating in ratings_other_user}

        user_rating = []
        other_user_rating = []
        common_articles = set(ratings_dict_user.keys()) & set(ratings_dict_other_user.keys())

        for article_id in common_articles:
            user_rating.append(ratings_dict_user[article_id])
            other_user_rating.append(ratings_dict_other_user[article_id])

            similarity = dot(user_rating, other_user_rating) / (norm(user_rating) * norm(other_user_rating))

        similarities.append((similarity, other_user.id))
    
    similarities = sorted(similarities, key=lambda x: x[0], reverse=True)

    return similarities
