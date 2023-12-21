import unittest
import another_sol as sut

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

    def test_given_mountains_overlapping_in_same_spot_when_calculating_visible_area_then_return_biggest_area(self):
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
                {'left': 0, 'right':  6, 'height': 3},], 20.75),
            ([
                {'left': 0, 'right': 4, 'height': 2},
                {'left': 1, 'right': 5, 'height': 2},
                {'left': 2, 'right':  6, 'height': 2},], 7.5)
        ]
        
        
        for mountains, expected_area in inputs:
            mountain_area = sut.visible_area(mountains)
            self.assertEqual(mountain_area, expected_area)
    
    def test_given_no_mountains_when_calculating_visible_area_then_return_zero(self):
        expected_area = 0.0
        
        area = sut.visible_area({})
        
        self.assertEqual(area, expected_area)
    

if __name__ == '__main__':
    unittest.main()