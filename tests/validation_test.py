from unittest import TestCase

from validation import Success, Failure


class ValidationTest(TestCase):
    def test_Success_should_be_success(self):
        self.assertTrue(Success(10).isSuccess())

    def test_Failure_should_not_be_success(self):
        self.assertFalse(Failure("error").isSuccess())

    def test_Success_should_not_be_failure(self):
        self.assertFalse(Success(10).isFailure())

    def test_Failure_should_be_failure(self):
        self.assertTrue(Failure("error").isFailure())

    def test_swap_should_convert_success_into_failure(self):
        self.assertEqual(Failure(10), Success(10).swap())

    def test_swap_should_convert_failure_into_success(self):
        self.assertEqual(Failure(10), Success(10).swap())


class ValidationMapTest(TestCase):
    def test_map_of_Success_should_be_another_Success(self):
        result = Success(10).map(lambda x: x + 5)
        self.assertEqual(Success(15), result)

    def test_map_of_Failure_should_be_this_Failure(self):
        result = Failure("error").map(lambda x: x + 5)
        self.assertEqual(Failure("error"), result)


class ValidationApplicativeTest(TestCase):
    def test_append_two_Success_then_should_produce_another_Success(self):
        result = Success([10]) + Success([5])
        self.assertEqual(Success([10, 5]), result)

    def test_append_Success_and_Failure_then_should_produce_Failure(self):
        result = Success([10]) + Failure(["Nope"])
        self.assertEqual(Failure(["Nope"]), result)

    def test_ap_on_Success_with_function_returning_Success_is_another_Success(self):
        result = Success(10).ap(Success(lambda x: Success(x + 5)))
        self.assertEqual(Success(15), result)

    def test_ap_on_Failure_is_Failure(self):
        result = Failure("error").ap(Success(lambda x: Success(x + 5)))
        self.assertEqual(Failure("error"), result)


class MaybeInDataStructureTest(TestCase):
    def test_Success_in_a_list(self):
        self.assertIn(Success(5), [Success(5)])

    def test_Failure_in_a_list(self):
        self.assertIn(Failure("error"), [Failure("error")])

    def test_Success_in_a_set(self):
        numbers = {Success(5), Success(5)}
        self.assertEqual(1, len(numbers))

    def test_Failure_in_a_set(self):
        numbers = {Failure("error"), Failure("error")}
        self.assertEqual(1, len(numbers))

    def test_Success_as_key_in_a_dict(self):
        numbers = {Success(5): "five"}
        self.assertEqual("five", numbers.get(Success(5)))

    def test_Failure_as_key_in_a_dict(self):
        numbers = {Failure("error"): "five"}
        self.assertEqual("five", numbers.get(Failure("error")))

