#!/bin/bash
# sends a POST request to the passed URL, 
 curl -s "$1" -XPOST -d "email=hr@holbertonschool.com" -d "subject=I will always be here for PLD"
 