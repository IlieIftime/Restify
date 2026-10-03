# Restify

Desktop application for configuring and controlling a Restify smart pillow.

The project was developed as a software and hardware integration prototype. It combines a Python graphical interface, local configuration storage, audio playback, and TCP communication with a Raspberry Pi.

## Overview

Restify allows users to interact with several smart-pillow features through a graphical interface:

- Basic user authentication and account management;
- Pillow measurements and parameter configuration;
- Alarm and smart-alarm configuration;
- Audio upload and playback;
- Pillow movement and actuator control;
- Raspberry Pi communication;
- Sensor data reception and visualization;
- Hardware tests for components such as motors, microphones, speakers, and pressure sensors;
- Local storage of preferences in JSON files.

> **Current status:** Restify is a prototype under development. Some features require external hardware, network configuration, or files that are still being implemented.

## Main Features

### Graphical interface

The interface is mainly developed with Tkinter and includes screens for:

- Welcome and login;
- User registration;
- Main menu;
- Settings;
- Pillow configuration;
- Measurement input;
- Account management;
- Alarms;
- Smart alarm clock;
- Audio playback;
- Hardware connection;
- Data visualization;
- Sleep monitoring.

### Raspberry Pi communication

The project includes TCP client-server components for communication with a Raspberry Pi.

Communication can be used to:

- Send commands to the hardware;
- Receive sensor data;
- Test motors and actuators;
- Validate the connection between the application and the pillow.

The IP address and port must be configured according to the network and device being used.

### Audio management

The application uses `pygame` to play audio files. Users can:

- Select `.mp3` or `.wav` files;
- Store files in the `audio_records` directory;
- View available audio files;
- Play and stop audio.

### Local storage

Application settings are stored locally in JSON files inside the `config` directory.

Stored information may include:

- User account data;
- Current session data;
- Pillow measurements;
- Smart-alarm settings;
- General application settings;
- Device-related configuration.

## Project Structure

```text
Restify/
└── RestifyV2/
    ├── GUI/                    # Tkinter interfaces and application screens
    ├── communication/          # TCP clients, servers, and communication scripts
    ├── config/                 # Local JSON configuration files
    ├── storage/                # Local persistence utilities
    ├── tests/                  # Sensor and actuator tests
    ├── audio_records/          # User audio files
    ├── data_recebida/          # Data received from the hardware
    ├── img/                    # Interface images
    ├── ml/                     # Reserved area for machine-learning features
    ├── audio.py                # Audio playback management
    ├── communication.py        # Basic TCP communication class
    ├── config.py               # Configuration constants and paths
    ├── main.py                 # Alternative application entry point
    ├── run.py                  # Main interface launcher
    ├── RUNneste.py             # Development launch script
    ├── storage.py              # JSON-based local persistence
    └── tester.py               # Experimental Kivy visual test
```

## Requirements

- Python 3.8 or newer;
- Tkinter;
- Pillow;
- pygame;
- matplotlib, when required by visualization modules;
- Kivy, only for the visual test in `tester.py`;
- Raspberry Pi access when running hardware tests;
- A network connection between the computer and the Raspberry Pi.

## Installation

Clone the repository:

```bash
git clone https://github.com/IlieIftime/Restify.git
cd Restify
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate the virtual environment.

### Windows

```powershell
.venv\Scripts\activate
```

### Linux/macOS

```bash
source .venv/bin/activate
```

Install the available dependencies:

```bash
pip install -r RestifyV2/requirements.txt
```

If the dependency file does not yet exist or is incomplete, install the main packages manually:

```bash
pip install pillow pygame matplotlib kivy
```

## Running the Application

From the `RestifyV2` directory, run the entry point selected for the version being tested:

```bash
cd RestifyV2
python RUNneste.py
```

Other experimental entry points may also be available:

```bash
python run.py
python main.py
```

Because the project currently contains multiple launch scripts, it is recommended to select one official entry point and archive the experimental alternatives.

## Raspberry Pi Configuration

Before starting hardware communication, confirm that:

1. The Raspberry Pi is connected to the same network;
2. The Raspberry Pi server is running;
3. The IP address is correct;
4. The configured port is available;
5. The firewall allows TCP communication;
6. The sensors and actuators are correctly connected.

Communication settings should be centralized in one configuration file. Avoid keeping fixed IP addresses directly in the source code.

## Hardware Tests

The `tests` directory includes scripts for components such as:

- Alarms;
- Microphone;
- Pressure and proximity sensors;
- Data reception;
- Servo motors;
- Speakers;
- Vibration motors;
- Raspberry Pi communication.

These tests may require a Raspberry Pi, physical sensors, motors, GPIO access, a local network, and operating-system-specific permissions.

Hardware tests are not expected to run on a computer without the corresponding physical components.

## Known Limitations

The project is still under development and currently has several limitations:

- Multiple entry points exist;
- Some features have duplicate implementations;
- Some paths depend on the original development environment;
- Network addresses may be defined directly in the source code;
- The dependency file requires updating;
- Some machine-learning modules are empty or incomplete;
- Local authentication should not yet be considered secure;
- JSON files are not a replacement for a database;
- Hardware tests depend on external equipment;
- TCP communication still needs a more robust protocol.

## Recommended Future Improvements

Recommended next steps include:

1. Define a single official entry point;
2. Correct and complete `requirements.txt`;
3. Replace absolute paths with `pathlib`;
4. Centralize network configuration;
5. Remove duplicate and experimental files;
6. Add automated tests for the main modules;
7. Implement secure password hashing;
8. Improve the Raspberry Pi communication protocol;
9. Add automatic reconnection and timeout handling;
10. Clearly separate production code, tests, and prototypes;
11. Document the JSON data formats;
12. Remove `__pycache__`, logs, and temporary data from version control;
13. Complete or remove the machine-learning modules.

## Project Description

Restify is a desktop prototype for controlling a smart pillow through a graphical interface. It supports alarm, measurement, audio, and movement configuration, stores user preferences locally, and communicates with a Raspberry Pi to receive sensor data and control hardware actuators.

## License

This repository uses the Apache License 2.0. See the `LICENSE` file for the complete license terms.
