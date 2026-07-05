#!/bin/bash
set -euo pipefail
echo "Setting up CSPM Agent..."
pip install -e ".[dev]"
echo "Setup complete!"
