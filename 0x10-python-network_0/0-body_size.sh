#!/usr/bin/env bash
# gets content page 
curl -sI HEAD  | grep "content-lengt"h | cut -d " " -f2
