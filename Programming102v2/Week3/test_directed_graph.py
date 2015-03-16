from directed_graph import DirectedGraph
import unittest


class TestDirectedGraph(unittest.TestCase):

    def setUp(self):
        self.graph = DirectedGraph()
        self.graph.add_edge("Pesho", "Tisho")
        self.graph.add_edge("Pesho", "Gosho")
        self.graph.add_edge("Tisho", "Grisho")
        self.graph.add_edge("Rafa", "Grisho")
        self.graph.add_edge("Grisho", "Tisho")
        self.graph.add_edge("Grisho", "Rafa")
        self.graph.get_neighbors_for("Grisho")
        self.graph.path_between("Pesho", "Rafa")

    def test_path_between(self):
        self.assertFalse(self.graph.path_between("Pesho", "Rafa"))
        self.graph.add_edge("Pesho", "Grisho")
        self.assertTrue(self.graph.path_between("Pesho", "Rafa"))

if __name__ == '__main__':
    unittest.main()
