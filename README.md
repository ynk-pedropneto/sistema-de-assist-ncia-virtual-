# Assistente Virtual com PLN (STT + TTS)

Um sistema simples de **assistência virtual por voz** em Python, construído com as bibliotecas apresentadas no curso:
- **SpeechRecognition** (Google Web Speech) para **STT** (fala → texto)
- **pyttsx3** para **TTS** (texto → fala) **offline**
- Regras de **comandos por voz** em português para abrir: **Wikipedia**, **YouTube** (home e busca) e **mapa da farmácia mais próxima** (Google Maps)

> Idioma padrão: **pt-BR**.  


## 📦 Requisitos
- **Python 3.9+**
- Microfone funcional
- Sistema com permissão de acesso ao microfone

### Dependências (arquivo `requirements.txt`)
- `speechrecognition`
- `pyttsx3`
- `wikipedia`
- `python-dotenv`
- `pyaudio` *(no Windows pode exigir instalação via `pipwin`)*

> **Windows (PyAudio):**
> ```bash
> pip install pipwin
> pipwin install pyaudio
> ```

> **macOS:** conceda permissão de microfone em **Preferências do Sistema → Segurança e Privacidade → Microfone**.  
> **Linux (Debian/Ubuntu):** se necessário, instale `portaudio19-dev`/`alsa`:
> ```bash
> sudo apt-get update
> sudo apt-get install -y portaudio19-dev python3-pyaudio alsa-utils
> ```

---

## 🛠️ Instalação
Dentro da pasta do projeto:
```bash
python -m venv .venv

# Windows
.venv\Scripts\pip install --upgrade pip
.venv\Scripts\pip install -r requirements.txt

# macOS/Linux
# source .venv/bin/activate && pip install -r requirements.txt
```

Crie opcionalmente um arquivo `.env` (veja `.env.example`):
```env
LANGUAGE=pt-BR
WAKE_WORD=assistente
LISTEN_TIMEOUT=6.0
PHRASE_TIME_LIMIT=8.0
```

---

## ▶️ Como executar
```bash
# Windows
.venv\Scripts\python main.py

# macOS/Linux
# source .venv/bin/activate && python main.py
```

Ao iniciar, fale naturalmente. Exemplos:

- “**Pesquisar no Wikipedia fisioterapia esportiva**”  
- “**Abrir YouTube**”  
- “**Pesquisar no YouTube reabilitação do joelho**”  
- “**Apresentar a localização da farmácia mais próxima**” ou “**farmácia mais próxima**”  
- “**Sair**” (encerra o assistente)

> Se configurar `WAKE_WORD=assistente`, comece cada comando com a hotword, por exemplo:  
> “**assistente pesquisar no Wikipedia inteligência artificial**”.

---

## 🧠 Comandos por voz suportados
- **Wikipedia (busca):**  
  - `pesquisar no wikipedia <termo>`  
  - `wikipedia <termo>`
- **YouTube:**  
  - `abrir youtube` (home)  
  - `pesquisar no youtube <termo>`
- **Farmácia mais próxima:**  
  - `apresentar a localização da farmácia mais próxima`  
  - `farmácia mais próxima` / `farmácia perto de mim`
- **Sair:**  
  - `sair`, `encerrar`, `parar`, `fechar assistente`

---

## 📁 Estrutura do projeto
```
assistente-virtual-pln/
├─ assistant/
│  ├─ __init__.py
│  ├─ config.py        # carrega .env e define idioma, timeouts e hotword
│  ├─ tts.py           # síntese de fala (pyttsx3)
│  ├─ stt.py           # reconhecimento de fala (SpeechRecognition + Google)
│  ├─ commands.py      # parsing simples de intenções com regex e ações
│  └─ utils.py         # abre URLs (Wikipedia, YouTube, Google Maps)
├─ main.py             # loop principal do assistente
├─ requirements.txt
├─ .gitignore
├─ .env.example
└─ README.md
```

---

## 🧩 Como funciona (resumo técnico)
- `STT`: usa `speech_recognition.Recognizer().recognize_google(audio, language="pt-BR")`.
- `TTS`: usa `pyttsx3`, tentando selecionar uma voz compatível com o idioma desejado.
- `commands.py`: regras com **regex** identificam intenções e executam ações via `webbrowser` (abrir páginas).

> **Privacidade:** o modo padrão de STT envia o áudio para o serviço do Google Web Speech. Para funcionamento 100% offline, você pode adaptar para **Vosk** (não incluso aqui para manter a simplicidade pedida no desafio).

---

## 🧯 Solução de problemas
- **PyAudio falhou no Windows:**  
  Use:
  ```bash
  pip install pipwin
  pipwin install pyaudio
  ```
- **Sem som no TTS (pyttsx3):** verifique o volume do sistema e se há voz em pt-BR instalada.  
- **Não reconhece o microfone:** escolha o dispositivo padrão correto no sistema operacional.  
- **Permissões no macOS:** dê acesso ao terminal/IDE em *Segurança e Privacidade → Microfone*.  
- **Nada acontece ao falar:** ruído ambiente alto pode atrapalhar. Fale próximo ao microfone, em local silencioso.


## 📜 Licença
Este projeto é distribuído sob a licença **MIT**. Sinta-se livre para usar e adaptar.

---

## ✨ Ideias de extensão (opcional)
- Hotword por **detecção contínua** (e.g., Snowboy/Picovoice Porcupine).
- Integração com APIs (previsão do tempo, notícias, etc.).
- NLU aprimorado (spaCy/Rasa) ou prompts com LLM para melhor compreensão.
