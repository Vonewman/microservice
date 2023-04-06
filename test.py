from main import add


def test_add():
    assert add(7, 5) == {'total': 12}
