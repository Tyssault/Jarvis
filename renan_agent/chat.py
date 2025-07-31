"""Simple conversation history management."""

from __future__ import annotations

from typing import List


class ChatHistory:
    """In-memory chat history."""

    def __init__(self) -> None:
        self.history: List[str] = []

    def add_user_message(self, message: str) -> None:
        self.history.append(f"Usuário: {message}")

    def add_agent_message(self, message: str) -> None:
        self.history.append(f"Renan: {message}")

    def get_history(self) -> str:
        return "\n".join(self.history)
