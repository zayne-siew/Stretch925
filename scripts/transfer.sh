#!/bin/bash

echo "Transferring data to front-end..."
cd ".."
python app.py
echo "Transfer complete"
# read -p "Press Enter to continue" </dev/tty