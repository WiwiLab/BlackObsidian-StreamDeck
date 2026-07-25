# BlackObsidian Studios - StreamDeck (BETA)

![Status](https://img.shields.io/badge/status-development-orange)

A custom Stream Deck system developed with ESP32 and Python.

The goal of this project is to create a modular and customizable alternative to commercial Stream Deck devices, allowing users to control sounds, OBS Studio, applications, editing tools, and system functions through a custom-built physical interface.

## Current Features

- 🎵 Custom sound playback
- 🎥 OBS Studio control through WebSocket
- 🎙️ Audio management and streaming effects
- 🚀 Application launching
- 🖥️ System tools (screenshots, controls, automations)
- 🎛️ Multiple operating modes:
  - STREAM
  - NORMAL
  - EDITION

## Hardware

- ESP32-WROOM-32
- 4x4 Matrix Keypad
- KY-040 Rotary Encoder
- Custom electronic components

## Software

- Python 3.11+
- OBS WebSocket
- PyAudio / SoundDevice
- PyAutoGUI
- Pycaw

> Note: The software interface and internal documentation currently include content written in Spanish.

## Project Structure

BlackObsidian-StreamDeck/

│

├── core/ # Main system

├── modules/ # Internal modules

├── plugins/ # Additional features

├── sounds/ # Custom sounds

├── profiles/ # Mode configurations

├── config_manager.py # Configuration management

└── main.py # Entry point

## Project Status

🚧 Project under development.

The system currently includes functional:
- action management,
- profiles,
- plugins,
- OBS integration,
- sound playback,
- command-based control.

## Developed by

**Yitzhak**
Founder & Developer — WiwiLab

Part of **WiwiLab**  
└── **BlackObsidian Studios** — A creative technology studio within WiwiLab, focused on developing interactive projects, custom systems and experiences that connect hardware and software to enhance creativity, productivity and digital workflows.
