#!/usr/bin/env bash

set -Eeuo pipefail

PROJECT="VPNPanel v2"

echo "======================================"
echo "        $PROJECT Installer"
echo "======================================"

# Проверка запуска от root
if [[ $EUID -ne 0 ]]; then
    echo "Ошибка: запустите install.sh от root."
    exit 1
fi

echo "✓ Запуск от root"

# Проверка операционной системы
if [[ -f /etc/os-release ]]; then
    source /etc/os-release
    echo "✓ Система: $PRETTY_NAME"
else
    echo "Не удалось определить операционную систему."
    exit 1
fi

echo
echo "Первичная проверка завершена успешно."

echo
echo "Обновление списка пакетов..."
apt update

echo
echo "Установка необходимых компонентов..."

apt install -y \
    git \
    curl \
    wget \
    unzip \
    python3 \
    python3-pip \
    python3-venv \
    sqlite3 \
    wireguard-tools

echo
echo "✓ Основные пакеты установлены."

echo
echo "Установка VPNPanel v2 может быть продолжена."