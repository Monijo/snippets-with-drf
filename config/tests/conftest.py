import pytest
from django.test import Client
from pytest_factoryboy import register
from factories import UserFactory


from django.contrib.auth.models import User

# @pytest.fixture
# def snippet():
#     snippet = Snippet.objects.create(title="pytest", code="pt")
#     return snippet

@pytest.fixture
def user_1(db):
    user = User.objects.create_user("test", "test@test.com", "test")
    print("create user")
    return user


@pytest.fixture
def client():
    client = Client()
    return client


@pytest.fixture(scope="session")
def fixture_1():
    print("fixture 1 is runninig")
    return 1


@pytest.fixture
def yield_fixture():
    print("start of the yeld fixture")
    yield 6
    print("After yield...tear down")


# @pytest.fixture
# def new_user_factory(db):
#     def create_app_user(
#         username: str,
#         password: str = None,
#         first_name: str = "firstname",
#         last_name: str = "lastname",
#         email: str = "test@test.com",
#         is_staff: str = False,
#         is_superuser: str = False,
#         is_active: str = True,
#     ):
#         user = User.objects.create_user(
#             username=username,
#             password=password,
#             first_name=first_name,
#             last_name=last_name,
#             email=email,
#             is_staff=is_staff,
#             is_superuser=is_superuser,
#             is_active=is_active,
#         )
#         return user
#     return create_app_user
#
# @pytest.fixture
# def new_user1(db, new_user_factory):
#     return new_user_factory("Test_user","password","MyName")
#
# @pytest.fixture
# def new_user_from_stuff(db, new_user_factory):
#     return new_user_factory("Test_user","password", "MyName", is_staff="True")

register(UserFactory) #user_factory

@pytest.fixture
def new_user_from_factory_boy(db, user_factory):
    user = user_factory.create()
    return user
