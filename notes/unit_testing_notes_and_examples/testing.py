# So first off we have assert statements, these allow us to check if a condition
# is met and if not print a currom message, looks like:

result = 300
assert result == 200, 'Expected return 200, instead got ' + str(result)

# Normally you would have result as = to the result of a function.
# You then put these assert statements into functions to make a single 
# unit test.

# Python being its super helpful self has a way of making this easier, you can
# import unittest. This allows us to make sure all tests are run as with the 
# previous method if an error was hit it would stop running. This looks like:

import unittest 
 
class TestTimesTen(unittest.TestCase):
    
    def test1(self):
        self.assertEqual(function_we_want_to_test(), """what the return value 
        should be""", "Message if it doesnt hit what we want")

# You then call it with:

unittest.main()

# As you can see above rather then assert we now use assertEquals, this is 
# a shorthand of what we typed above. Its worth noting that there are abunch of
# shorthands like this, a full list can be found here:
# https://docs.python.org/3/library/unittest.html#unittest.TestCase.output
# It inculdes methods like: (self.assertIn, self.assertTrue, self.assertTrue, 
# assertAlmostEqual(This will check if they're the same after being rounded 
# down 7 places.), self.assertRaises (This takes in an exception and will 
# pass the test if the exception is hit, fail it if it doesnt hit it and 
# error if a different exception was hit.), self.assertWarns (Same as the last
# one but with warns))

# We can also take the above code abit further using subTest() this allows us to
# run mulitply tests are once. You would write it like: 

class TestTimesTen(unittest.TestCase):
 
    def test_times_ten(self):
        for num in [0, 1000000, -10]:
            with self.subTest():
                expected_result = num * 10
                message = str(num) + "gave an incorrect answer"
                self.assertEqual(times_ten(num), expected_result, message)


# This code would run through each number in num and test it and if it didn't
# get the expected result it would print the message. Its worth noting while you
# could do this without subTest() it would stop at the first failure were as with
# subTest() it will run through all of them and then report any mistakes once its
# done.

# Next up we have text fixtures, this is broken down into setUp() and tearDown().
# This allows us to ensure the tests are run properly and prevent invalid results.
# You would write them like:

def setUp(self):
    placeholder()

def tearDown(self):
    placeholder()

# Writing it like this will cause them to run before and after each test. You
# can also write it so it only does it at the start of testing and at the end.
# This looks like:

@classmethod
def setUpClass(cls):
    placeholder()

@classmethod
def tearDownClass(cls):
    placeholder()

# Next up we have skipping tests this can be done one of two ways, with the 
# unitest skip decorator or with self.skip test. These looks like: 

@unittest.skipUnless(sys.platform.startswith("linux"), 
"This test only runs on Linux")
def test_linux_feature(self):
    print("This test should only run on Linux")

@unittest.skipIf(not sys.platform.startswith("linux"), 
"This test only runs on Linux")
def test_other_linux_feature(self):
    print("This test should only run on Linux")

def test_linux_feature(self):
    if not sys.platform.startswith("linux"):
        self.skipTest("Test only runs on Linux")

# As you can see the decorator has 2 different forms, skipUnless and skipIf, 
# skipUnless skips if the condition is false and skipIf skips if the condition
# is true.

# Finally we can plan for failures with the expectedFailure decorator, this is 
# useful is we know there is a known bug and dont want it to cloud the test 
# results, to do this you write:

@unittest.expectedFailure
def test_broken_feature(self):
    raise Exception("This test is going to fail")