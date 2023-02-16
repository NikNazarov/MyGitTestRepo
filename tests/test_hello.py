from myapp import say_hallo


def test_hello():
    assert say_hallo() == "Hellow World!"