#!/usr/bin/env bash
set -e

# ── Colors ──
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
CYAN='\033[0;36m'
NC='\033[0m'

# ── Paths ──
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
BINARY="$SCRIPT_DIR/dist/gorbe"
INSTALL_DIR="/usr/local/bin"
INSTALL_PATH="$INSTALL_DIR/gorbe"

echo -e "${CYAN}🐱 Installing Gorbe${NC}"
echo -e "${CYAN}─────────────────────────────${NC}"

# ── 1. Check binary exists ──
if [ ! -f "$BINARY" ]; then
  echo -e "${RED}✗ Binary not found: $BINARY${NC}"
  echo -e "${YELLOW}  Build it first:${NC}"
  echo -e "${YELLOW}  python -m PyInstaller --clean --noconfirm --onefile --name gorbe --add-data \"templates:templates\" main.py${NC}"
  exit 1
fi

echo -e "${GREEN}✓${NC} Binary found: $BINARY"

# ── 2. Make executable ──
chmod +x "$BINARY"
echo -e "${GREEN}✓${NC} Executable permission set"

# ── 3. Copy to /usr/local/bin ──
echo -e "${YELLOW}→ Installing to $INSTALL_PATH ...${NC}"

if [ -w "$INSTALL_DIR" ]; then
  cp "$BINARY" "$INSTALL_PATH"
else
  sudo cp "$BINARY" "$INSTALL_PATH"
fi

# ── 4. Set executable on target ──
if [ -w "$INSTALL_PATH" ]; then
  chmod +x "$INSTALL_PATH"
else
  sudo chmod +x "$INSTALL_PATH"
fi

echo -e "${GREEN}✓${NC} Installed to $INSTALL_PATH"

# ── 5. Verify installation ──
echo -e "${YELLOW}→ Verifying installation...${NC}"
if command -v gorbe &>/dev/null; then
  echo -e "${GREEN}✓${NC} 'gorbe' command is available in PATH"
else
  echo -e "${RED}✗ 'gorbe' not found in PATH. Is $INSTALL_DIR in your PATH?${NC}"
fi

echo ""
echo -e "${GREEN}✅ Installation complete!${NC}"
echo -e "${CYAN}  Run:${NC}  ${GREEN}gorbe${NC}"
