import pytest
from timpy import get_float, get_int

def test_get_float(monkeypatch):
    inputs = ["1", "10", "0", "-1", "1.0", "-1.0", "1.5", "-1.5", "0.5", "-0.5", ".5", "-.5", "000000005", "0.0000005", "0.0000000000000000000000000000000000000000000000000000000000000000000000000001"]
    expect = [1, 10, 0, -1, 1.0, -1.0, 1.5, -1.5, 0.5, -0.5, .5, -.5, 5, 0.0000005, 0]
    for i, test_input in enumerate(inputs):
        monkeypatch.setattr("builtins.input", lambda _: test_input)
        assert get_float(f"Type {test_input}: ") == expect[i]
    
def test_get_float_errors(monkeypatch):
    inputs = iter(["--1", "1--1", "1.2.3", "a", "abc", "DEADBEEF", "True", "1.0"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    # all invalid inputs will be skipped, leaving us with the 1.0
    assert get_float(f"Type {inputs}: ") == 1.0
    
def test_get_int(monkeypatch):
    inputs = ["1", "10", "0", "-1", "000000005"]
    expect = [1, 10, 0, -1, 5]
    for i, test_input in enumerate(inputs):
        monkeypatch.setattr("builtins.input", lambda _: test_input)
        assert get_int(f"Type {test_input}: ") == expect[i]

def test_get_int_errors(monkeypatch):
    inputs = iter(["--1", "1--1", "1.2.3", "a", "abc", "DEADBEEF", "True", "1.0", "-.5", "1"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    # all invalid inputs will be skipped, leaving us with the 1.0
    assert get_int(f"Type {inputs}: ") == 1.0
    

# Run the tests
pytest.main(["-v", "--tb=line", "-rN", __file__])

