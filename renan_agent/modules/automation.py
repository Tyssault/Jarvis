"""n8n automation integration."""

from __future__ import annotations

import subprocess


def run_flow(command: str) -> str:
    """Run an n8n workflow."""
    flow_name = command.replace("executar automacao", "").strip()
    try:
        subprocess.run(["n8n", "run", flow_name], check=True)
        return f"Fluxo {flow_name} executado"
    except Exception as exc:  # pylint: disable=broad-except
        return f"Falha ao executar automação: {exc}"
