#!/bin/bash
# run_all.sh — Complete test suite for Sentinel Risk
set -e

DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "${DIR}/.."

echo "Starting Sentinel Risk Test Suite..."
echo ""

bash tests/test_validation.sh
echo ""
bash tests/test_skills.sh
echo ""
bash tests/test_exports.sh

echo ""
echo "============================================================"
echo " ★ ALL VERIFICATION GATES PASSED: READY FOR PASSPORT ★"
echo "============================================================"
