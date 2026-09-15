#!/bin/bash
# test_exports.sh — Verifies cross-framework portability exports (Passport Visas)
set -e

mkdir -p exports

echo "============================================================"
echo " EXPORTING PASSPORT VISAS ACROSS ECOSYSTEM TARGETS"
echo "============================================================"

FORMATS=(
  "system-prompt:exports/system-prompt.txt"
  "claude-code:exports/CLAUDE.md"
  "openai:exports/openai-agent.py"
  "crewai:exports/crewai-agent.py"
  "lyzr:exports/lyzr-agent.json"
  "cursor:exports/.cursorrules"
  "gemini:exports/gemini-config.json"
  "copilot:exports/copilot-instructions.md"
)

for ENTRY in "${FORMATS[@]}"; do
  FORMAT="${ENTRY%%:*}"
  OUTFILE="${ENTRY##*:}"
  echo "Stamping Visa for: [${FORMAT}] -> ${OUTFILE}"
  bunx @open-gitagent/opengap export -f "${FORMAT}" -o "${OUTFILE}"
  if [ ! -s "${OUTFILE}" ]; then
    echo "ERROR: Export ${OUTFILE} is empty!"
    exit 1
  fi
done

cp exports/openai-agent.py exports/openai.py

echo ""
echo "============================================================"
echo " ALL PASSPORT VISAS GENERATED & VERIFIED SUCCESSFULLY"
echo "============================================================"
ls -lh exports/
