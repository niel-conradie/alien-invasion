# Alien Invasion

Alien Invasion Game written in Python built using Pygame. 

The goal is to shoot the enemy space ships before they reach earth. The game continuously gets more difficult as the levels progress. You can play yourself or let a computer play for you!

----
## Requirements

- [Python 3.10.5](https://www.python.org/downloads/release/python-3105/)
- [Pygame 2.1.2](https://www.pygame.org/news)
----
## Installation

Alien Invasion can be installed via Pip. To start, clone the repository to your local computer and change into the proper directory.

```bash
Clone Repository

  $ git clone https://github.com/niel-conradie/Alien-Invasion.git
  $ cd Alien-Invasion
```
### Pip Install

```bash
Create Environment

  $ python -m venv .venv
```
```bash
Activate Environment

  # Bash
  $ source .venv/Scripts/activate

  # Command Prompt
  C:> .venv\Scripts\activate.bat

  # macOS
  $ .venv/bin/activate

  # PowerShell
  PS C:> Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
  PS C:> .venv\Scripts\Activate.ps1
```
```bash
Install Requirements

  (.venv) $ python -m pip install -r requirements.txt
```
----
## Usage

```bash
To start the game run one of these two files.

  # Human Player
  run.py

  # Computer Player
  run_computer.py
```
----