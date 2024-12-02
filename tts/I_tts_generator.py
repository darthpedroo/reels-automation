from abc import ABC

class ITtsGenerator(ABC):
    """
    Interface for the TTS strategy pattern generator
    """

    def generate_tts(self, parsed_json_data:dict ):
        """Generates a tts given a json
        """
        pass
