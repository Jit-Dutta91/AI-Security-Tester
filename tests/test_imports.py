def test_backend_imports():
    import backend.app.main

    assert backend.app.main.app is not None
