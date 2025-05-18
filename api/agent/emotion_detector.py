import json

from api.agent.cupcakeagent import CupCakeAgent


class EmotionDetector(CupCakeAgent):
    def __init__(self):
        super().__init__("./prompt/ask_emotion.txt")

    def extract_emotion(self, response):
        json_data = response[8:-3]
        data = json.loads(json_data)
        return data['emotions']

    def answer(self, text):
        response = self.invoke(text)
        print("hehe")
        print(response)
        _emotions = self.extract_emotion(response)
        return _emotions