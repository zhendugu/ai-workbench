#!/usr/bin/env bash
set -e

REMOTE_URL="https://github.com/zhendugu/ai-workbench.git"

git init
git add .
git commit -m "chore: initialize ai-workbench skeleton with frozen definitions"
git branch -M main
git remote add origin $REMOTE_URL
git push -u origin main

echo "Git repository initialized and pushed to GitHub."