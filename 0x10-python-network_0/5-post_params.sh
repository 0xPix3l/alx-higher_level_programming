#!/bin/bash
# POST data
curl -sX POST $1 -d "email=hr@holbertonschool.com&subject=I will always be here for PLD" -L
