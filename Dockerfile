FROM ubuntu:20.04

# Avoid interactive prompts
ENV DEBIAN_FRONTEND=noninteractive
ENV PATH="/usr/games:${PATH}"

# Install dependencies
RUN apt-get update && apt-get install -y \
    fortune-mod \
    cowsay \
    lolcat \
    netcat \
 && rm -rf /var/lib/apt/lists/*

# Copy script
COPY wisecow.sh /usr/local/bin/wisecow.sh
RUN chmod +x /usr/local/bin/wisecow.sh

# Expose port
EXPOSE 4499

# Run script
CMD ["/usr/local/bin/wisecow.sh"]
