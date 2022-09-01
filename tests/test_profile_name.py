from profile import Profile
from user import User


def test_object_name_setter_correct():
    user = User("Ali1", "Ali@12345")
    profile = Profile("ali", "ahmadi", 1999)
    assert profile.name == "ali"