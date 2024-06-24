#!/bin/bash

# 현재 스크립트 파일의 경로
script_path=$(dirname "$0")

# 가상 환경의 경로
venv_path="$script_path/venv/bin/activate"

# 가상 환경 활성화
echo "source $venv_path"