from unittest import TestCase

from src.array_list import ArrayList


class TestArrayList(TestCase):

    def test_append(self):
        array_list = ArrayList[int](
            size=10,
            realloc_coeff=2,
            potential_formula=lambda num_of_occupied_cells, num_of_cells: 2 * num_of_occupied_cells - num_of_cells
        )
        self.assertEqual(3, array_list.append(1))
        self.assertEqual(10, len(array_list))
        for i in range(9):
            array_list.append(1)
        self.assertEqual(3, array_list.append(1))
        self.assertEqual(20, len(array_list))

    def test_potential(self):
        array_list = ArrayList[int](
            size=10,
            realloc_coeff=2,
            potential_formula=lambda num_of_occupied_cells, num_of_cells: 2 * num_of_occupied_cells - num_of_cells
        )
        self.assertEqual(-10, array_list.potential())
        array_list.append(1)
        self.assertEqual(-8, array_list.potential())

    def test_complexity(self):
        k = 100
        n = 5000
        array_list = ArrayList[int](
            size=10,
            realloc_coeff=2,
            potential_formula=lambda num_of_occupied_cells, num_of_cells: 2 * num_of_occupied_cells - num_of_cells
        )
        potential_0 = array_list.potential()
        amortized_costs = [array_list.append(1) for _ in range(k)]
        potential_k = array_list.potential()
        self.assertEqual(250, sum(amortized_costs) + (potential_0 - potential_k))
        amortized_costs = amortized_costs + [array_list.append(1) for _ in range(n - k)]
        potential_n = array_list.potential()
        self.assertEqual(10110, sum(amortized_costs) + (potential_0 - potential_n))
