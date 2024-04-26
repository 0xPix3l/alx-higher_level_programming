#!/bin/bash
# POST data
curl -sX POST -d $1 "email=test@gmail.com&subject=I will always be here for PLD" -L
