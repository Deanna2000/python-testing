## Instructions

Write test cases to verify the I/O of the following methods of `Animal` and `Dog`.

1. In the test class' `setUpClass()` method, create an instance of `Animal` and `Dog`.
1. Animal object has the correct `name` property.
1. Set a species and verify that the object property of `species` has the correct value.
1. Invoking the `walk()` method set the correct speed on the both objects.
1. The animal object is an instance of `Animal`.
1. The dog object is an instance of `Dog`.

## Test Discovery

Read the [Test Discovery section](https://docs.python.org/3.3/library/unittest.html#unittest-test-discovery) of the Python docs. It explains how you can run all tests inside a directory. This allows you to split your unit test suite into many, smaller, more maintainable modules, and the use a pattern matcher to find tests in all matching files.

```
python -m unittest discover -s . -p "Test*.py" -v