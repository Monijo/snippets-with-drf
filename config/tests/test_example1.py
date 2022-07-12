import pytest
from django.contrib.auth.models import User


# @pytest.mark.skip  # ten zostanie przeskoczony
# def test_example():
#     assert 1 == 1
#
#
# @pytest.mark.xfail  # ten napewno obleje ale terminal zielony:)
# def test_example2():
#     assert 1 == 2
#
#
# @pytest.mark.slow
# def test_example3(fixture_1):
#     print("run test example3")
#     sth = fixture_1
#     assert sth == 1
#
#
# @pytest.mark.slow
# def test_example4(fixture_1):
#     print("run test example4")
#     sth = fixture_1
#     assert sth == 1
#
# TEST_DIV_DATA = (
#     (8, 2, 4),
#     (0, 9, 0),
#     (7, 2, 3.5)
# )
#
#
# def div(a, b):
#     return a / b
#
#
# @pytest.mark.parametrize("a,b, result", TEST_DIV_DATA)
# def test_div(a, b, result):
#     assert div(a, b) == result
#
#
# def test_with_yield(yield_fixture):
#     print("test with yield is running...")
#     assert yield_fixture == 6
#
# @pytest.mark.django_db
# def test_user_create(user_1):
#     assert User.objects.count() == 1
#
# @pytest.mark.django_db
# def test_user_create(new_user_from_stuff):
#     assert User.objects.count() == 1
#     assert new_user_from_stuff.is_staff == "True"

# @pytest.mark.django_db
# def test_new_user_with_factory_boy(user_factory):
#     user = user_factory.create()
#     print(user.username)
#     assert User.objects.all().count() == 1

@pytest.mark.django_db
def test_new_user_with_factory_boy(new_user_from_factory_boy):
    print(new_user_from_factory_boy)
    assert User.objects.all().count() == 1
