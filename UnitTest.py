import unittest
import main


class Testmain(unittest.TestCase):
    def setUp(self):
        print ('About to test a function')

    def test_do_stuff(self):
        '''
        Hiiiiiiii
        :return:
        '''
        test_param = 10
        result = main.do_stuff(test_param)
        self.assertEqual(result, 15)

    def test_do_stuff2(self):
        test_param = 'hsdihu'
        result = main.do_stuff(test_param)
        # self.assertTrue(isinstance(result, ValueError))
        self.assertIsInstance(result, ValueError)

    def test_do_stuff3(self):
        test_param = None
        result = main.do_stuff(test_param)
        self.assertEqual(result, 'please enter a number')

    def test_do_stuff4(self):
        test_param = ''
        result = main.do_stuff(test_param)
        self.assertEqual(result, 'please enter a number')

    def tearDown(self):
        print('Clean up')
if __name__ == '__main__':
    unittest.main()
