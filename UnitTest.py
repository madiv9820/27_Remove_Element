from Solution import Solution
import unittest
from timeout_decorator import timeout

class UnitTest(unittest.TestCase):
    def setUp(self) -> None:
        self.__testCases = {
            1: {
                'nums': [3,2,2,3], 'val': 3,
                'output_size': 2, 'output_nums': [2, 2]
            },
            2: {
                'nums': [0,1,2,2,3,0,4,2], 'val': 2,
                'output_size': 5, 'output_nums': [0,1,4,0,3]
            }
        }

        self.__obj = Solution()
        return super().setUp()
    
    @timeout(0.5)
    def test_Case1(self):
        case = self.__testCases[1]
        nums, val, output_size, output_nums = case.values()
        res = self.__obj.removeElement(nums, val)
        self.assertIsInstance(res, int)
        self.assertEqual(res, output_size)
        self.assertEqual(sorted(nums[:res]), 
                            sorted(output_nums))

    @timeout(0.5)
    def test_Case2(self):
        case = self.__testCases[2]
        nums, val, output_size, output_nums = case.values()
        res = self.__obj.removeElement(nums, val)
        self.assertIsInstance(res, int)
        self.assertEqual(res, output_size)
        self.assertEqual(sorted(nums[:res]), 
                            sorted(output_nums))

if __name__ == '__main__':
    unittest.main()