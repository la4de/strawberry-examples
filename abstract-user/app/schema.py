import strawberry
import strawberry_django
from . import models
from django.contrib import auth
from typing import List

types = strawberry_django.TypeRegister()

@types.register
@strawberry_django.type(models.User, fields=['username', 'nickname', 'groups'], types=types)
class User:
    pass

@types.register
@strawberry_django.type(auth.models.Group, fields=['name'], types=types)
class Group:
    pass

@strawberry.type
class Query:
    users = strawberry_django.queries.list(User)
    groups = strawberry_django.queries.list(Group)

schema = strawberry.Schema(query=Query)
