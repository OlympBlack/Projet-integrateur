from commondatab.models import ZzDiscussions, ZzFriendship, ZzMessages, ZzUsersDiscussions, ZzMedias, ZzUsers, ZzUsersManager
from django.db import models

class Messages(ZzMessages):
    def __str__(self) -> str:
        return f'{self.user.username}-{self.discussion}' if self.user else f'{self.content}-{self.discussion}'