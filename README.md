# Keystroke Dynamics Authentication 
This project demonstrates behavioral authentication using inter-key timings. The user enrolls with 5 password attempts; typing rhythms are averaged and compared on login using Euclidean distance.

## Features
- Console-based (Windows, uses `msvcrt`)
- Records and prints the inter-key timing vector
- Access granted or denied based on timing similarity (bio-metrics)

## Usage
1. Install numpy (if you haven’t yet):  pip install numpy
2. Run the script: python keystroke_auth.py
3. Follow the prompts in the terminal.

## Example Screenshot
<img width="291" height="153" alt="image" src="https://github.com/user-attachments/assets/8374c85a-82be-4078-8670-a67371344057" />


## Requirements
- Python 3.x (Windows)
- numpy
- No additional packages needed on Windows

## Code Structure
- `keystroke_auth.py`: Main authentication script

## Author
Tayyaba :P 
