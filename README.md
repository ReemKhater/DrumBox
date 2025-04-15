# DrumBox

DrumBox is a rhythm box project developed to provide a versatile, interactive, and customizable drum-playing experience. This project includes both hardware and software components to play pre-recorded sounds using physical buttons, adjust volume with a potentiometer, and interact with a speaker system.

## Table of Contents
1. [Project Overview](#project-overview)
2. [Features](#features)
3. [Hardware](#hardware)
4. [Software](#software)
5. [Setup and Usage](#setup-and-usage)
6. [Repository Structure](#repository-structure)
7. [Contributors](#contributors)
8. [Acknowledgments](#acknowledgments)

---

## Project Overview
DrumBox is a multidisciplinary project that combines:
- **Software**: Python scripts to manage GPIO, sound playback, and volume control.
- **Hardware**: Custom PCB and 3D-printed case to house the components.

## Features
- **Play Sounds**: Trigger sound effects with physical buttons.
- **Adjustable Volume**: Use a potentiometer to control the volume in real-time.
- **Safe Shutdown**: Power button to safely shut down the Raspberry Pi.
- **Custom Sounds**: Easily replace or expand the sound bank.

---

## Hardware
- **Raspberry Pi**: Used for GPIO handling and sound processing.
- **Custom PCB**: Designed to interface with buttons, potentiometer, and speaker.
- **Speaker**: Outputs the triggered sounds.
- **3D-Printed Case**: Houses the components neatly.

The PCB and 3D design files are included in the repository under the `Hardware` directory.

---

## Software
The software is written in Python and relies on several custom modules:
- `main.py`: Entry point for the program.
- `gpioHandler.py`: Manages button presses and GPIO setup.
- `soundPlayer.py`: Plays pre-recorded sounds or wave files.
- `volumeHandler.py`: Adjusts the volume using an ADC.
- `SpeakerHandler.py`: Configures the speaker system.

---

## Setup and Usage

### Clone the Repository
```bash
git clone https://github.com/yourusername/DrumBox.git
cd DrumBox
```

### Install Required Dependencies
Ensure Python is installed on your Raspberry Pi. Then install the required libraries:
```bash
pip install -r requirements.txt
```

### Download the Sound Bank
Ensure the sound files are located in the DrumBox/data directory. You can replace the default sound files with your own, ensuring they are compatible (.wav format).

### Run the Program
Navigate to the project directory and execute the main script:
```bash
python3 main.py
```

---

## Repository Structure
```bash
DrumBox/
├── Hardware/
│   ├── PCB/                   # KiCad files for the PCB
│   ├── 3D_Print/              # STL files for the 3D case
├── DrumBox/
│   ├── main.py                # Entry point
│   ├── gpioHandler.py         # Handles GPIO inputs
│   ├── soundPlayer.py         # Manages sound playback
│   ├── volumeHandler.py       # Handles volume control
│   ├── SpeakerHandler.py      # Configures the speaker
│   ├── data/                  # Sound bank directory
├── README.md                  # Project documentation
├── requirements.txt           # Required Python dependencies
```

---

## Contributors

- Reem Khater: Software development.

- Mathieu Martinent: Hardware development. 

---

## Acknowledgments

Special thanks to Professor Ayoub Jebri and for  for guidance and support throughout this project. 

An additional acknowledgment to Patricia Kittel for the help in the PCB part. 


