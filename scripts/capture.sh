#!/bin/bash

echo "Starting capture sequence..."
cd "../cv"
peekingduck run
echo "Capture sequence complete"
# read -p "Press Enter to continue" </dev/tty