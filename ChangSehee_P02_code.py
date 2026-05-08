import maya.cmds as cmds
import random

def simple_scatter():
    selection = cmds.ls(sl=True)
    if not selection:
        cmds.warning("Please select your object first.")
        return
    
    source_obj = selection[0]

    for i in range(5):
        new_obj = cmds.duplicate(source_obj)[0]
        x = random.uniform(-7,7)
        z = random.uniform(-7,7)
        cmds.xform(new_obj, translation=[x, 0, z])
    
def apply_variation(obj):  
    
    rot_y = random.uniform(0, 360)
    cmds.setAttr(f"{obj}.rotateY", rot_y)    

    s = random.uniform(0.5, 1.5)
    cmds.setAttr(f"{obj}.scale", s, s, s)

def scatter_on_surface(target_mesh, count):
    selection = cmds.ls(sl=True)
    if not selection:
        cmds.warning("Please select the object you want to duplicate.")
        return
        
    source_obj = selection[0]

    for i in range(count):
        new_obj = cmds.duplicate(source_obj)[0]
        
        rx = random.uniform(-15, 15)
        rz = random.uniform(-15, 15)
        
        target_height = cmds.getAttr(f"{target_mesh}.translateY")
        
        cmds.xform(new_obj, t=[rx, target_height, rz])

    print(f"Success: {count} objects scattered on {target_mesh}!")
