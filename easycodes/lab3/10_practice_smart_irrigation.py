import random


class Environment:
    def __init__(self):
        self.state = random.choice(['Dry', 'Wet'])

    def get_percept(self):
        return self.state

    def change_state(self):
        self.state = random.choice(['Dry', 'Wet'])

    def turn_pump_on(self):
        print("Water pump: ON")


class SimpleReflexAgent:
    def act(self, percept):
        if percept == 'Dry':
            return 'Turn water pump ON'
        else:
            return 'No action needed - Soil is Wet'


def run_agent(agent, environment, steps):
    for step in range(steps):
        percept = environment.get_percept()
        action = agent.act(percept)

        print(
            f"Step {step + 1}: Percept - {percept}, "
            f"Action - {action}"
        )

        if percept == 'Dry':
            environment.turn_pump_on()

        environment.change_state()


agent = SimpleReflexAgent()
environment = Environment()

run_agent(agent, environment, 5)
