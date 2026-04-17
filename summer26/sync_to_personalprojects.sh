#!/bin/zsh
set -euo pipefail

SOURCE_DIR="/Users/lukasz/Documents/Summer26"
REPO_DIR="/Users/lukasz/Documents/personalprojects"
TARGET_DIR="${REPO_DIR}/summer26"

mkdir -p "${TARGET_DIR}"

rsync -a --delete \
  --exclude '.git/' \
  --exclude '__pycache__/' \
  --exclude '*.pyc' \
  "${SOURCE_DIR}/" "${TARGET_DIR}/"

git -C "${REPO_DIR}" status --short

if [[ $# -gt 0 ]]; then
  git -C "${REPO_DIR}" add summer26 README.md .gitignore
  git -C "${REPO_DIR}" commit -m "$*"
fi

echo
echo "Synced ${SOURCE_DIR} -> ${TARGET_DIR}"
echo "Next steps:"
echo "  git -C ${REPO_DIR} add summer26 README.md .gitignore"
echo "  git -C ${REPO_DIR} commit -m \"update summer26\""
echo "  git -C ${REPO_DIR} push -u origin main"
