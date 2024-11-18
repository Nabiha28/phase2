import heapq

class RecommendationSystem:
    def __init__(self):
        self.user_product_interactions = {}  # Hash Table: User -> Product interactions
        self.product_graph = {}  # Graph: Product -> List of users

    def add_interaction(self, user_id, product_id, interaction_value):
        # Add or update interaction for a user-product pair
        if user_id not in self.user_product_interactions:
            self.user_product_interactions[user_id] = {}
        self.user_product_interactions[user_id][product_id] = interaction_value

        # Add the interaction to the product graph (user-product bipartite graph)
        if product_id not in self.product_graph:
            self.product_graph[product_id] = []
        self.product_graph[product_id].append(user_id)

    def get_top_n_recommendations(self, user_id, n=5):
        # Generate top-N recommendations for a given user
        product_scores = []
        for product, users in self.product_graph.items():
            score = sum(self.user_product_interactions[u].get(product, 0) for u in users)
            heapq.heappush(product_scores, (score, product))
        return heapq.nlargest(n, product_scores)
