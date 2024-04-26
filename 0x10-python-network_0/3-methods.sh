#!/bin/bash
# OPTIONS
curl -sI ALLOW $1 | grep "allow" | cut -d " " -f2

