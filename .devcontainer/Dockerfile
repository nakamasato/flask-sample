
FROM mcr.microsoft.com/devcontainers/python:1-3.12-bullseye

ARG USERNAME=vscode

# Install tig
RUN apt-get update && apt-get install -y tig && apt-get clean

# Used to persist shell history
RUN mkdir /commandhistory \
    && touch /commandhistory/.bash_history \
    && touch /commandhistory/.zsh_history \
    && chown -R $USERNAME /commandhistory \
    && echo 'export PROMPT_COMMAND="history -a" && export HISTFILE=/commandhistory/.bash_history' >> "/home/$USERNAME/.bashrc" \
    && echo 'export HISTFILE=/commandhistory/.zsh_history' >> "/home/$USERNAME/.zshrc"

# Create claude config directories and set permissions
RUN mkdir -p /home/$USERNAME/.claude && \
  chown -R $USERNAME /home/$USERNAME/.claude
