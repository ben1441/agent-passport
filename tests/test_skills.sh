#!/bin/bash
# test_skills.sh — Unit test skill execution scripts
set -e

echo "============================================================"
echo " TESTING SKILL: financial-ratio-analysis"
echo "============================================================"

python3 skills/financial-ratio-analysis/scripts/calculate_ratios.py \
  skills/financial-ratio-analysis/examples/input.json > /tmp/ratio_output.json

echo "Output preview:"
cat /tmp/ratio_output.json | grep -E '"dscr"|"fccr"|"risk_grade"|"recommendation"'
echo "✓ financial-ratio-analysis calculation successful."

echo ""
echo "============================================================"
echo " TESTING SKILL: aml-sanctions-screening"
echo "============================================================"

python3 skills/aml-sanctions-screening/scripts/screen_entity.py \
  skills/aml-sanctions-screening/examples/screening_request.json > /tmp/screening_output.json

echo "Output preview:"
cat /tmp/screening_output.json | grep -E '"entity_name"|"screening_status"|"cleared"'
echo "✓ aml-sanctions-screening verification successful."

echo ""
echo "============================================================"
echo " TESTING MCP TOOL: immutable-audit-logger"
echo "============================================================"

python3 tools/immutable-audit-logger.py << 'EOF' > /tmp/audit_tool_output.json
{
  "event_type": "test_verification",
  "agent_role": "auditor",
  "payload": {
    "test_id": "TEST-001",
    "status": "PASS"
  }
}
EOF

cat /tmp/audit_tool_output.json | grep -E '"entry_id"|"status"'
echo "✓ immutable-audit-logger execution successful."
