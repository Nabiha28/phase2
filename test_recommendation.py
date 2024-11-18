import unittest
from recommendation_system import RecommendationSystem

class TestRecommendationSystem(unittest.TestCase):
    
    def test_add_interaction(self):
        rec_system = RecommendationSystem()
        rec_system.add_interaction(1, 'p1', 5)
        self.assertEqual(rec_system.user_product_interactions[1], {'p1': 5})

    def test_get_top_n_recommendations(self):
        rec_system = RecommendationSystem()
        rec_system.add_interaction(1, 'p1', 5)
        rec_system.add_interaction(2, 'p1', 4)
        rec_system.add_interaction(1, 'p2', 3)
        rec_system.add_interaction(2, 'p2', 5)
        
        recommendations = rec_system.get_top_n_recommendations(1, n=2)
        self.assertEqual(len(recommendations), 2)

if __name__ == '__main__':
    unittest.main()
