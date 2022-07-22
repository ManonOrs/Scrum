import src


def test_connexion():
    assert src.connexion(1) is True
    assert src.connexion(2) is True
    assert src.connexion(3) is False
