import maya.cmds as cmds
import random

def simple_scatter():
    selection = cmds.ls(sl=True)
    if not selection:
        cmds.warning("Please select your object first.")
        return
    
    source_obj = selection[0]

    for i in range(3):
        new_obj = cmds.duplicate(source_obj)[0]
        x = random.uniform(-7,7)
        y = random.uniform(-7,7)
        cmds.xform(new_obj, translation=[x, 0, z])