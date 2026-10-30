class TestMathOperations:
    def test_subtraction(self):
        sub_result = 100 - 40
        assert sub_result == 60

    def test_division(self):
        quotient = 50 / 2
        assert quotient == 25.0

suite = TestMathOperations()
suite.test_subtraction()
suite.test_division()
print('Test Math operations All passed')