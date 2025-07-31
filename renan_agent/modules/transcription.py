"""Audio transcription using Whisper."""

from __future__ import annotations

import subprocess
from pathlib import Path


def transcribe_audio(command: str) -> str:
    """Transcribe audio using Whisper."""
    output_dir = Path("outputs")
    output_dir.mkdir(exist_ok=True)
    audio_path = output_dir / "audio.wav"
    transcript_path = output_dir / "transcript.txt"
    try:
        subprocess.run(["whisper", str(audio_path), "--output", str(transcript_path)], check=True)
        return transcript_path.read_text()
    except Exception as exc:  # pylint: disable=broad-except
        return f"Falha na transcrição: {exc}"
