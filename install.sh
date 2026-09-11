#!/usr/bin/env bash
set -e

# Create & activate venv
python3 -m venv venv
# shellcheck disable=SC1091
source venv/bin/activate

# Upgrade pip and install dependencies
python -m pip install --upgrade pip
pip install -r requirements.txt

cat <<'EOF'
echo
echo "Setup complete."
echo "Activate the virtualenv with: source venv/bin/activate"
echo "Run the app with: python project1.py"
EOF
