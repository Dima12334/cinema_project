from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType
from django.shortcuts import redirect

from .models import Review

User = get_user_model()


class LeaveEmotion:
    def update_like(self, request, review):
        """Лайкает.
        """
        is_dislike = False

        for dislike in review.dislikes.all():
            if dislike == request.user:
                is_dislike = True
                break

        if is_dislike:
            review.dislikes.remove(request.user)

        is_like = False

        for like in review.likes.all():
            if like == request.user:
                is_like = True
                break

        if not is_like:
            review.likes.add(request.user)

        if is_like:
            review.likes.remove(request.user)

    def update_dislike(self, request, review):
        """Дизлайкает.
        """
        is_like = False

        for like in review.likes.all():
            if like == request.user:
                is_like = True
                break

        if is_like:
            review.likes.remove(request.user)

        is_dislike = False

        for dislike in review.dislikes.all():
            if dislike == request.user:
                is_dislike = True
                break

        if not is_dislike:
            review.dislikes.add(request.user)

        if is_dislike:
            review.dislikes.remove(request.user)
