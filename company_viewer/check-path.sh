#!/bin/bash
# Path check script for Vite project
# Checks if the project path contains illegal characters

CURRENT_PATH=$(pwd)
PROJECT_ROOT=$(dirname "$(realpath "$0")")

echo "=== Path Check for Vite Project ==="
echo "Current directory: $CURRENT_PATH"
echo "Project root: $PROJECT_ROOT"
echo ""

# Check for # character in path
if echo "$PROJECT_ROOT" | grep -q '#'; then
    echo "❌ ERROR: Path contains '#' character:"
    echo "$PROJECT_ROOT"
    echo ""
    echo "This may cause issues with Vite development server."
    echo "Please rename the directory to remove '#' characters."
    exit 1
else
    echo "✅ Path does not contain '#' character"
fi

# Check for other problematic characters
if echo "$PROJECT_ROOT" | grep -qE '[%&]'; then
    echo "⚠️  WARNING: Path contains potentially problematic characters (%, &)"
    echo "$PROJECT_ROOT"
fi

echo ""
echo "Path is safe for Vite development server."
exit 0

