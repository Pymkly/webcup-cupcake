from api.agent.cupcakeagent import CupCakeAgent


class Refactor(CupCakeAgent):
    def __init__(self):
        super().__init__("./prompt/reformulation.txt")

    def answer(self, text):
        return self.invoke(text)