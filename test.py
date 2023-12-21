import unittest
import unittest.mock

import solution as sut

class TestMountainsVisibleArea(unittest.TestCase):

    def test_given_non_overlapping_mountains_when_calculating_visible_area_then_return_sum_of_all_areas(self):
        mountains = [
            {'left': 0, 'right': 1000, 'height': 500},
            {'left': 1000, 'right':  2000, 'height': 500},
            {'left': 2000, 'right':  3000, 'height': 500},
            {'left': 4000, 'right':  5000, 'height': 500},
        ]
        
        expected_area = 4 * 250_000
        
        area = sut.visible_area(mountains)
        self.assertEqual(area, expected_area)

    def test_given_nested_mountains_when_calculating_visible_area_then_return_biggest_area(self):
        mountains = [
            {'left': 9, 'right': 15, 'height': 3},
            {'left': 9, 'right': 15, 'height': 3},
            {'left': 9, 'right': 15, 'height': 3},
            {'left': 11, 'right': 15, 'height': 2},
            {'left': 11, 'right': 15, 'height': 2},
            {'left': 11, 'right': 15, 'height': 2},
        ]
        
        expected_area = 9.0
        
        area = sut.visible_area(mountains)
        
        self.assertEqual(area, expected_area)
        
    def test_given_mountains_partially_overlapping_when_calculating_visible_area_then_return_expected_value(self):
        inputs = [
            ([
                {'left': 0, 'right': 6, 'height': 3},
                {'left': 4, 'right': 6, 'height': 1},
                {'left': 4, 'right': 10, 'height': 3},], 17.0),
            ([
                {'left': 9, 'right': 15, 'height': 3},
                {'left': 8, 'right': 14, 'height': 3},
                {'left': 0, 'right': 6, 'height': 3},], 20.75),
            ([
                {'left': 0, 'right': 4, 'height': 2},
                {'left': 1, 'right': 5, 'height': 2},
                {'left': 2, 'right': 6, 'height': 2},], 7.5),
            ([
                {'left': 0, 'right': 4, 'height': 2},
                {'left': 1, 'right': 5, 'height': 2},
                {'left': 2, 'right': 6, 'height': 2},
                {'left': 3, 'right': 7, 'height': 2},], 9.25),
        ]
        
        
        for mountains, expected_area in inputs:
            mountain_area = sut.visible_area(mountains)
            self.assertEqual(mountain_area, expected_area)
    
    def test_given_no_mountains_when_calculating_visible_area_then_return_zero(self):
        expected_area = 0.0
        
        area = sut.visible_area({})
        
        self.assertEqual(area, expected_area)
    
    def test_given_maximum_mountains_when_calculating_visible_area_then_return_expected_value(self):
        MAXIMUM_QUANTITY_OF_MOUNTAINS = 1000
        expected_area = 2756.25 #Area of n identical mountains shifted by one is same as area of 1 mountain + (n-1)(area of 1 mountain  - intersection)
        
        mountains = []
        for i in range(MAXIMUM_QUANTITY_OF_MOUNTAINS):
            temp_mountain = {'left': 0, 'right': 6, 'height': 3}
            temp_mountain['right'] = temp_mountain['right'] + i
            temp_mountain['left'] = temp_mountain['left'] + i
            mountains.append(temp_mountain)
        
        area = sut.visible_area(mountains)
        
        self.assertEqual(area, expected_area)
    
    def test_given_nested_mountains_when_removing_nested_ones_then_return_non_nested_mountains(self):
        expected_mountains = [
            {'left': 0, 'right': 100, 'height': 50},
            {'left': 1, 'right': 101, 'height': 50},
        ]
        
        mountains = [
            {'left': 0, 'right': 100, 'height': 50},
            {'left': 0, 'right': 100, 'height': 50},
            {'left': 0, 'right': 100, 'height': 50},
            {'left': 1, 'right': 101, 'height': 50},
        ]
        
        non_nested_mountains = sut.remove_nested_mountains(mountains)
        
        self.assertListEqual(non_nested_mountains, expected_mountains)
        
        
    @unittest.mock.patch("solution.inclusion_exclusion_principle")
    def test_given_mountains_when_calculating_visible_area_then_expect_sorted_non_nested_mountains(self, mock_method):
        expected_mountains = [
            {'left': 0, 'right': 100, 'height': 50},
            {'left': 1, 'right': 101, 'height': 50},
            {'left': 2, 'right': 102, 'height': 50},
        ]

        mountains = [
            {'left': 1, 'right': 101, 'height': 50},
            {'left': 0, 'right': 100, 'height': 50},
            {'left': 2, 'right': 102, 'height': 50},
            {'left': 2, 'right': 102, 'height': 50}
        ]

        sut.visible_area(mountains)

        mock_method.assert_called_once_with(expected_mountains)
        
if __name__ == '__main__':
    unittest.main()