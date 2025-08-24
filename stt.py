import speech_recognition as sr
from typing import Optional
from . import config

class STT:
    def __init__(self, language: str = None):
        self.r = sr.Recognizer()
        self.language = language or config.LANGUAGE

    def listen_once(self, timeout: float = None, phrase_time_limit: float = None) -> Optional[str]:
        """
        Captura áudio do microfone e retorna o texto reconhecido ou None.
        """
        timeout = timeout if timeout is not None else config.LISTEN_TIMEOUT
        phrase_time_limit = phrase_time_limit if phrase_time_limit is not None else config.PHRASE_TIME_LIMIT

        with sr.Microphone() as source:
            self.r.adjust_for_ambient_noise(source, duration=0.8)
            try:
                audio = self.r.listen(source, timeout=timeout, phrase_time_limit=phrase_time_limit)
            except sr.WaitTimeoutError:
                return None

        try:
            text = self.r.recognize_google(audio, language=self.language)
            return text
        except sr.UnknownValueError:
            return None
        except sr.RequestError:
            # Sem internet/erro no serviço
            return None
