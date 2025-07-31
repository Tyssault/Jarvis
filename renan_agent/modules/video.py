"""Video creation utilities using FFmpeg and Wav2Lip."""

from __future__ import annotations

import subprocess
from pathlib import Path


def create_video(command: str) -> str:
    """Create a video from an image and audio using Wav2Lip."""
    output_dir = Path("outputs")
    output_dir.mkdir(exist_ok=True)
    output_path = output_dir / "video.mp4"
    image_path = output_dir / "image.png"
    audio_path = output_dir / "audio.wav"
    try:
        subprocess.run(["wav2lip", "--face", str(image_path), "--audio", str(audio_path), "--outfile", str(output_path)], check=True)
        return f"Vídeo criado em {output_path}"
    except Exception as exc:  # pylint: disable=broad-except
        return f"Falha ao criar vídeo: {exc}"
