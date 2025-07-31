"""Voice synthesis using Coqui TTS."""

from __future__ import annotations

import subprocess
from pathlib import Path


def synthesize_voice(command: str) -> str:
    """Generate synthetic speech using Coqui TTS."""
    text = command.replace("crie uma voz", "").strip()
    output_dir = Path("outputs")
    output_dir.mkdir(exist_ok=True)
    audio_path = output_dir / "audio.wav"
    try:
        subprocess.run(["tts", "--text", text, "--out_path", str(audio_path)], check=True)
        return f"Áudio gerado em {audio_path}"
    except Exception as exc:  # pylint: disable=broad-except
        return f"Falha na geração de voz: {exc}"
