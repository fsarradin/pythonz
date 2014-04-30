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

    def test_ap(self):
        result = Success(10).ap(Success(lambda x: Success(x + 5)))
        self.assertEqual(Success(15), result)
