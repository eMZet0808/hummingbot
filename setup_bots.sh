#!/bin/bash
set -euo pipefail

# 🗂 Pfad zur Controller-Basis
BASE_DIR="./controllers"

# 📦 Liste der Bots
BOTS=("hybrid_v2" "spike_sniper" "trend_bias")

# 🧱 Standard-Dateien pro Bot
BASE_FILES=("controller.py" "executor.py" "order_manager.py" "recovery.py" "risk_manager.py")

# 🔧 Hilfsordnerstruktur
UTILS=("utils/logger.py" "utils/__init__.py")

# 📁 Bot-Struktur aufbauen
for BOT in "${BOTS[@]}"; do
    BOT_DIR="${BASE_DIR}/${BOT}"
    echo "🧹 Entferne evtl. vorhandenen Ordner: $BOT_DIR"
    rm -rf "$BOT_DIR"
    echo "🔧 Erstelle neue Bot-Struktur für: $BOT"
    mkdir -p "$BOT_DIR/utils"

    # Basisdateien erzeugen
    for FILE in "${BASE_FILES[@]}"; do
        FILENAME="${FILE/controller/${BOT}_controller}"
        FILENAME="${FILENAME/executor/${BOT}_executor}"
        TARGET="${BOT_DIR}/${FILENAME}"
        echo "# coding: utf-8" > "$TARGET"
        echo "# ${FILENAME} – automatisch erstellt für $BOT" >> "$TARGET"
    done

    # Hilfsdateien erzeugen
    for FILE in "${UTILS[@]}"; do
        TARGET="${BOT_DIR}/${FILE}"
        echo "# coding: utf-8" > "$TARGET"
        echo "# ${FILE} – Hilfsmodul für $BOT" >> "$TARGET"
    done

    # __init__.py für Modulimport
    echo "# coding: utf-8" > "$BOT_DIR/__init__.py"
    echo "# __init__.py für Bot: $BOT" >> "$BOT_DIR/__init__.py"
done

echo "✅ Bot-Ordner wurden neu erstellt unter: $BASE_DIR"
