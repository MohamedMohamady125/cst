# CPU Thermal ODE Solver & Visualizer

Predict and plot CPU core temperature under time-varying power using a first-order thermal model or any user-defined ODE.

## Features
- Reads ODE from user input or uses built-in CPU thermal model  
- Accepts step, pulse, or CSV power profiles  
- Adaptive solver (RK45) with configurable tolerances  
- Reports metrics: peak temperature, settling time, throttle exceedance  
- 2D visualization with units, ambient line, error bands  

## Installation
```bash
python -m venv .venv
source .venv/bin/activate   
pip install -r requirements.txt
