#!/usr/bin/env bash

text="# that takes in a URL, sends a request to that URL
echo ""
"

for file in *; do
    if [[ -f $file && $(head -n 2 "$file") != "$text" && $file != "README.md" && $file != "write.sh" ]]; then
        echo "$text" | cat - "$file" > temp && mv temp "$file"
        chmod +x "$file"
        echo "Added '$text' to $file"
    fi
done
