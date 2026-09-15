#!/bin/bash
# test_validation.sh — Validates OpenGAP specification compliance and regulatory audit
set -e

echo "============================================================"
echo " RUNNING OPENGAP SPEC & COMPLIANCE VALIDATION"
echo "============================================================"

bunx @open-gitagent/opengap validate --dir .
bunx @open-gitagent/opengap validate --compliance --dir .

echo ""
echo "============================================================"
echo " RUNNING COMPLIANCE AUDIT"
echo "============================================================"

bunx @open-gitagent/opengap audit --dir .

echo "✓ OpenGAP spec validation & audit complete."
