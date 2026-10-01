class Environment:
    def __init__(self,initial_state):
        self.initial_state=initial_state
    def get_percept(self):
        pass
class SimpleAgent:
    def __init__(self):
        pass
    def act(self,percept):
        pass
def run_agent(agent,environment):
    percept=environment.get_percept()
    action=agent.act(percept)


agent=SimpleAgent()
environment=Environment(initial_state=0)
run_agent(agent,environment)
