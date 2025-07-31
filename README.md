# Renan Agent

Renan Agent é um assistente local inspirado no Jarvis capaz de executar tarefas automaticamente utilizando ferramentas instaladas no computador.

## Instalação

1. Clone este repositório e navegue até a pasta do projeto.
2. Execute o script `install.sh` para instalar as dependências Python:

```bash
./install.sh
```

Certifique-se de que ComfyUI, FFmpeg, n8n e Wav2Lip estejam instalados e presentes no `PATH` do sistema.

## Uso

Execute o agente com o comando abaixo:

```bash
python -m renan_agent.main
```

Digite seus comandos em português, por exemplo:

- `gere uma imagem de uma paisagem`
- `crie uma voz dizendo Olá`
- `executar automacao exemplo`

O histórico de conversa será salvo em `chat_history.txt`.
