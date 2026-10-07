class Environment:
    def __init__(self, rain='No', windows_open='Open'):
        self.rain = rain
        self.windows_open = windows_open

    def get_percept(self):
        return {
            'rain': self.rain,
            'windows_open': self.windows_open
        }

    def close_windows(self):
        if self.windows_open == 'Open':
            self.windows_open = 'Closed'


class ModelBasedAgent:
    def __init__(self):
        self.model = {
            'rain': 'No',
            'windows_open': 'Open'
        }

    def act(self, percept):
        self.model.update(percept)

        if (
            self.model['rain'] == 'Yes'
            and self.model['windows_open'] == 'Open'
        ):
            return 'Close the windows'
        else:
            return 'No action needed'


def run_agent(agent, environment, steps):
    for step in range(steps):
        percept = environment.get_percept()
        action = agent.act(percept)

        print(
            f"Step {step + 1}: Percept - {percept}, "
            f"Action - {action}"
        )

        if action == 'Close the windows':
            environment.close_windows()


agent = ModelBasedAgent()
environment = Environment(rain='Yes', windows_open='Open')
run_agent(agent, environment, 5)
