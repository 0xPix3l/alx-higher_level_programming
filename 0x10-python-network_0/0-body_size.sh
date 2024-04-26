#!/usr/bin/env bash
# gets content page
curl -sI $1 | grep "Content-Length" | cut -d " " -f2
