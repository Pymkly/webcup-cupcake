from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI

YOUR_API_KEY = "AIzaSyAK4WYCxcXz-EbEc2RMzHcJyfU8pit9jR8"

class CupCakeAgent:
    def __init__(self, file_path):
        self.llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash", google_api_key=YOUR_API_KEY)
        self.file_path = file_path

    def get_instruction(self):
        try:
            with open(self.file_path, 'r', encoding='utf-8') as fichier:
                contenu = fichier.read()
        except FileNotFoundError:
            print(f"Erreur: Le fichier '{self.file_path}' n'a pas été trouvé.")
        except Exception as e:
            print(f"Une erreur s'est produite lors de la lecture du fichier '{self.file_path}': {e}")
        return contenu

    def invoke(self, user_input):
        _instruction = self.get_instruction()
        _prompt = ChatPromptTemplate.from_messages([
            (
                "system",
                _instruction
            )
            ,
            (
                "human", "{user_input}"
            )
        ])
        chain = _prompt | self.llm
        response = chain.invoke(
            {
                "user_input": user_input
            }
        )
        return response.content