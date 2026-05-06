import maya.cmds as cmds
import random

def simple_scatter():
    selection = cmds.ls(sl=True)
    if not selection:
        cmds.warning("Please select your object first.")
        return
    
    source_obj = selection[0]