# SeheeChang_P02
# Maya Surface Scatter and Variation Tool 
  Creator : Sehee Chang

# GitHub URL
 https://github.com/SeheeChang97/SeheeChang_P02.git

## Overview
  A Python and PySide6 utility for Maya that scatters objects onto a selected target mesh with controlled density and transformation variation. 

## Key Features
  1. Surface Scattering : Place objects on a selected mesh.
  2. Random Variation : Jitter for position,   rotation, and scale.
  3. User-Defined Range Control: Features QDoubleSpinBox inputs for precise min/max range settings, addressing specific layout needs

## Challenges I anticipated
  - PySide6 Version Revision: The most important challenge was adapting the tool for Maya 2027, which required changing from PySide2 to PySide6.
  - UI-to-Script Data Handling: Ensuring that user-defined numerical inputs from the GUI were correctly passed to the core scattering functions was a complex logic step.   
  
## Future Goal 
  While I aimed for surface normal alignment first, I concentrated on building a stable and user-driven range control system.