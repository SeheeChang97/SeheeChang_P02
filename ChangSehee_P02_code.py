import maya.cmds as cmds
import random
cmds.poly

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
    
def scatter_on_surface(target_mesh, count):
    selection = cmds.ls(sl=True)
    if not selection:
        cmds.warning("Please select the object you want to duplicate.")
        return
        
    source_obj = selection[0]

    for i in range(count):
        new_obj = cmds.duplicate(source_obj)[0]
          
        rx = random.uniform(-20, 20)
        rz = random.uniform(-20, 20)

        pos = cmds.closestPointOnMesh(target_mesh, ip=[rx, 0, rz], q=True, p=True)
        
        cmds.xform(new_obj, t=pos)

    print(f"Success: {count} objects scattered on {target_mesh}!")