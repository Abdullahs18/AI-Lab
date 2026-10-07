class Environment:
    def __init__(self, movies=None):
        if movies is None:
            movies = {
                'Movie A': 8,
                'Movie B': 6,
                'Movie C': 9
            }
        self.movies = movies

    def get_percept(self):
        return self.movies


class UtilityBasedAgent:
    def __init__(self, mood_factor=0.7):
        self.mood_factor = mood_factor

    def utility(self, review):
        return review * self.mood_factor

    def act(self, percept):
        best_movie = None
        best_utility = -float('inf')

        for movie, review in percept.items():
            movie_utility = self.utility(review)

            if movie_utility > best_utility:
                best_movie = movie
                best_utility = movie_utility

        return best_movie


def run_agent(agent, environment):
    percept = environment.get_percept()
    best_choice = agent.act(percept)

    print(f"Available Movies: {percept}")
    print(f"Best Movie to Watch: {best_choice}")


agent = UtilityBasedAgent(mood_factor=0.8)
environment = Environment({
    'Movie A': 7,
    'Movie B': 9,
    'Movie C': 5
})

run_agent(agent, environment)
