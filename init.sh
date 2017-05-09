#!/bin/bash

args=("$@")

name=Problem
name=Problem${args[0]}
echo ${name} directory made.
echo File main.py inside directory is ready.

mkdir ${name}
touch ${name}/main.py
