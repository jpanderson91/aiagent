#!/bin/bash
MAX_RETRIES=10
ATTEMPT=1

while [ $ATTEMPT -le $MAX_RETRIES ]; do
    echo "=== Attempt $ATTEMPT of $MAX_RETRIES ==="
    OUTPUT=$(bootdev run e457f633-6cbf-44bd-9eec-8a938f8db13a -s 2>&1)
    echo "$OUTPUT"
    
    if echo "$OUTPUT" | grep -q "503 UNAVAILABLE"; then
        echo ">>> 503 error detected, retrying in 30s..."
        sleep 30
        ATTEMPT=$((ATTEMPT + 1))
    elif echo "$OUTPUT" | grep -q "Tests failed"; then
        echo ">>> Tests failed (not 503), stopping."
        exit 1
    else
        echo ">>> Tests passed!"
        exit 0
    fi
done

echo ">>> Max retries reached."
exit 1
