class Environment:
    def __init__(self, heat_level='High'):
        self.heat_level = heat_level

    def get_percept(self):
        return 'Hot' if self.heat_level == 'High' else 'Cool'


class SimpleReflexAgent:
    def __init__(self):
        pass

    def act(self, percept):
        if percept == 'Hot':
            return 'Pull hand away, you touched the hot object'
        else:
            return 'You have not touched any hot object, No need to pull away'


def run_agent(agent, environment):
    percept = environment.get_percept()
    action = agent.act(percept)
    print(f"Percept: {percept}, Action: {action}")


agent = SimpleReflexAgent()
environment = Environment(heat_level='Low')
run_agent(agent, environment)
