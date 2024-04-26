#!/bin/bash
# OPTIONS
curl -sI ALLOW $1 -L | grep "allow" | cut -d " " -f2-

