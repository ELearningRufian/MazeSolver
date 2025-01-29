import unittest
from maze import Maze

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )

    def test_maze_create_cells_negative_rows(self):
        num_cols = 12
        num_rows = -10
        with self.assertRaises(ValueError) as context:
            m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        result = str(context.exception)
        expected = "The maze must have at least 1 row"
        self.assertEqual(result, expected)

    def test_maze_create_cells_negative_columns(self):
        num_cols = -12
        num_rows = 10
        with self.assertRaises(ValueError) as context:
            m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        result = str(context.exception)
        expected = "The maze must have at least 1 column"
        self.assertEqual(result, expected)

    # Negative coordinates could go off-canvas but should not raise exceptions
    def test_maze_create_cells_negative_coordinates(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(-100, -100, num_rows, num_cols, -100, -100) 
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )

    def test_maze_greak_entrance_and_exit(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertFalse(m1._cells[0][0].has_top_wall)
        self.assertFalse(m1._cells[-1][-1].has_bottom_wall)

if __name__ == "__main__":
    unittest.main()
