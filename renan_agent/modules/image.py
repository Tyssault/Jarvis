"""Image generation via ComfyUI."""

from __future__ import annotations

import subprocess
from pathlib import Path


def generate_image(command: str) -> str:
    """Generate an image using ComfyUI.

    This function assumes ComfyUI is installed locally and accessible
    via the `comfyui` command. The generated image path is returned.
    """
    prompt = command.replace("gere uma imagem", "").strip()
    output_dir = Path("outputs")
    output_dir.mkdir(exist_ok=True)
    output_path = output_dir / "image.png"
    try:
        subprocess.run(["comfyui", "--prompt", prompt, "--output", str(output_path)], check=True)
        return f"Imagem gerada em {output_path}"
    except Exception as exc:  # pylint: disable=broad-except
        return f"Falha ao gerar imagem: {exc}"
