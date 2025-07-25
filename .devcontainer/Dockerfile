FROM mcr.microsoft.com/devcontainers/python:1-3.12-bullseye

ARG USERNAME=vscode

# Used to persist bash history as per https://code.visualstudio.com/remote/advancedcontainers/persist-bash-history
RUN SNIPPET="export PROMPT_COMMAND='history -a' && export HISTFILE=/commandhistory/.bash_history" \
    && mkdir /commandhistory \
    && touch /commandhistory/.bash_history \
    && chown -R $USERNAME /commandhistory \
    && echo "$SNIPPET" >> "/home/$USERNAME/.bashrc"

# Create claude config directories and set permissions
RUN mkdir -p /home/$USERNAME/.claude && \
  chown -R $USERNAME /home/$USERNAME/.claude
