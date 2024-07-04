# Use an official Ubuntu as a parent image
FROM ubuntu:latest

# Set the working directory in the container
WORKDIR /usr/src/app

# Install necessary packages
RUN apt-get update && apt-get install -y \
    build-essential \
    gcc \
    flex \
    bison \
    byacc \
    git \
    && rm -rf /var/lib/apt/lists/*

# Copy the current directory contents into the container
COPY . .
# Compile Lex and Yacc code
RUN flex simple_language.lex
# This command doesn't work while compiling bc it doesn't generate the y.tab.h file so instead use yacc
# RUN bison -d simple_language.y
RUN yacc -d simple_language.y
RUN gcc lex.yy.c y.tab.c -o compiler

# Run the compiler
CMD ["./compiler"]
