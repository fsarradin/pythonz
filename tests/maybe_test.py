from maybe import Nothing, Maybe, Just

from unittest import TestCase


class MaybeTest(TestCase):
    def test_Maybe_of_None_is_Nothing(self):
        self.assertEqual(Nothing, Maybe.pure(None))

    def test_Maybe_of_not_None_is_Just(self):
        self.assertEqual(Just(5), Maybe.pure(5))

    def test_Just_is_equal_to_Just_with_same_value(self):
        self.assertEqual(Just(5), Just(5))

    def test_Just_is_not_equal_to_Just_with_different_value(self):
        self.assertNotEqual(Just(5), Just(10))

    def test_Just_is_equal_not_to_Nothing(self):
        self.assertNotEqual(Just(5), Nothing)

    def test_Nothing_is_equal_to_Nothing(self):
        self.assertEqual(Nothing, Nothing)

    def test_iter_on_Just(self):
        result = 0
        for value in Just(10):
            result = value

        self.assertEqual(10, result)

    def test_iter_on_Nothing(self):
        result = 0
        for value in Nothing:
            result = value

        self.assertEqual(0, result)


class MaybeDefinedTest(TestCase):
    def test_Just_is_defined(self):
        self.assertTrue(Just(5).is_defined())

    def test_Nothing_is_not_defined(self):
        self.assertFalse(Nothing.is_defined())


class MaybeMapTest(TestCase):
    def test_map_of_Just_is_another_Just(self):
        self.assertEqual(Just(15), Just(10).map(lambda x: x + 5))

    def test_map_of_Nothing_is_Nothing(self):
        self.assertEqual(Nothing, Nothing.map(lambda x: x + 5))

    def test_flatmap_of_Just_is_another_Just(self):
        self.assertEqual(Just(15), Just(10).flatmap(lambda x: Just(x + 5)))

    def test_flatmap_of_Nothing_is_Nothing(self):
        self.assertEqual(Nothing, Nothing.flatmap(lambda x: Just(x + 5)))

    def test_map_flatmap_on_Just(self):
        result = Just(10).flatmap(lambda x: Just(5).map(lambda y: x + y))
        self.assertEqual(Just(15), result)

    def test_map_flatmap_on_Nothing(self):
        result = Just(10).flatmap(lambda x: Nothing.map(lambda y: x + y))
        self.assertEqual(Nothing, result)


class MaybeFoldTest(TestCase):
    def test_fold_of_Just_gives_result(self):
        result = Just(10).fold(5, lambda x, y: x + y)
        self.assertEqual(15, result)

    def test_fold_of_Nothing_shold_be_initial_value(self):
        result = Nothing.fold(5, lambda x, y: x + y)
        self.assertEqual(5, result)


class MaybeInDataStructureTest(TestCase):
    def test_Just_in_a_list(self):
        self.assertIn(Just(5), [Just(5)])

    def test_Nothing_in_a_list(self):
        self.assertIn(Nothing, [Nothing])

    def test_Just_in_a_set(self):
        numbers = {Just(5), Just(5)}
        self.assertEqual(1, len(numbers))

    def test_Nothing_in_a_set(self):
        numbers = {Nothing, Nothing}
        self.assertEqual(1, len(numbers))

    def test_Just_as_key_in_a_dict(self):
        numbers = {Just(5): "five"}
        self.assertEqual("five", numbers.get(Just(5)))

    def test_Nothing_as_key_in_a_dict(self):
        numbers = {Nothing: "five"}
        self.assertEqual("five", numbers.get(Nothing))

