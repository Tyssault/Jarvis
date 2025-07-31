"""Main entry point for Renan Agent.
Provides a simple command-line chat interface for executing tasks.
"""

from __future__ import annotations

import sys
from pathlib import Path
from typing import Callable, Dict

from .chat import ChatHistory
from .modules import image, video, transcription, voice, automation

# Mapping of keywords to module handlers
COMMAND_HANDLERS: Dict[str, Callable[[str], str]] = {
    "imagem": image.generate_image,
    "video": video.create_video,
    "transcrever": transcription.transcribe_audio,
    "voz": voice.synthesize_voice,
    "automacao": automation.run_flow,
}

def parse_command(command: str) -> Callable[[str], str] | None:
    """Return the handler for a given command text."""
    for key, handler in COMMAND_HANDLERS.items():
        if key in command.lower():
            return handler
    return None

def main() -> None:
    """Run a simple REPL chat for the agent."""
    chat = ChatHistory()
    print("Renan Agent iniciado. Digite 'sair' para encerrar.")
    while True:
        try:
            user_input = input("Você: ")
        except EOFError:
            break
        if user_input.strip().lower() == "sair":
            break
        chat.add_user_message(user_input)
        handler = parse_command(user_input)
        if handler:
            response = handler(user_input)
        else:
            response = "Comando não reconhecido."
        chat.add_agent_message(response)
        print(f"Renan: {response}")
    # Optionally save conversation history
    history_path = Path("chat_history.txt")
    history_path.write_text("\n".join(chat.history))

if __name__ == "__main__":
    main()
