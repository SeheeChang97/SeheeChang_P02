import maya.cmds as cmds
import random

from PySide6 import QtWidgets, QtCore

class ScatterToolUI(QtWidgets.QDialog):
    def __init__(self):
        super(ScatterToolUI, self).__init__()
        self.setWindowTitle("Scatter Tool")
        self.setFixedSize(300, 300)
        
        self.target_mesh_name = ""         
        self.create_widgets()
        self.create_layout()
        self.connect_signals()

    def create_widgets(self):
        self.target_btn = QtWidgets.QPushButton("Set Target Surface")

        self.min_pos_input = QtWidgets.QDoubleSpinBox()
        self.min_pos_input.setRange(-100, 100)
        self.min_pos_input.setValue(-15.0) 
        
        self.max_pos_input = QtWidgets.QDoubleSpinBox()
        self.max_pos_input.setRange(-100, 100)
        self.max_pos_input.setValue(15.0) 

        self.count_input = QtWidgets.QSpinBox()
        self.count_input.setValue(10)
        self.apply_btn = QtWidgets.QPushButton("Scatter")

    def create_layout(self):
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.target_btn)

        range_layout = QtWidgets.QHBoxLayout()
        range_layout.addWidget(QtWidgets.QLabel("Min Range:"))
        range_layout.addWidget(self.min_pos_input)
        range_layout.addWidget(QtWidgets.QLabel("Max Range:"))
        range_layout.addWidget(self.max_pos_input)
        
        layout.addLayout(range_layout) 
        
        layout.addWidget(QtWidgets.QLabel("Object Count:"))
        layout.addWidget(self.count_input)
        layout.addWidget(self.apply_btn)
        self.setLayout(layout)
       
    def connect_signals(self):

        self.target_btn.clicked.connect(self.set_target)
        self.apply_btn.clicked.connect(self.do_scatter)

    def set_target(self):
       
        sel = cmds.ls(sl=True)
        if sel:
            self.target_mesh_name = sel[0]
            self.target_btn.setText(f"Target: {self.target_mesh_name}")
        else:
            cmds.warning("Please select a surface mesh first!")

    def do_scatter(self):        
        count = self.count_input.value()
        
        min_val = self.min_pos_input.value()
        max_val = self.max_pos_input.value()
        
        if self.target_mesh_name: 
            scatter_on_surface(self.target_mesh_name, count, min_val, max_val)
        else:
            cmds.warning("You must set a Target Surface first!")

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

def scatter_on_surface(target_mesh, count, min_val, max_val):
    selection = cmds.ls(sl=True)
    if not selection:
        cmds.warning("Please select the object you want to duplicate.")
        return
        
    source_obj = selection[0]

    for i in range(count):
        new_obj = cmds.duplicate(source_obj)[0]
        
        rx = random.uniform(min_val, max_val)
        rz = random.uniform(min_val, max_val)
        
        target_height = cmds.getAttr(f"{target_mesh}.translateY")
        cmds.xform(new_obj, t=[rx, target_height, rz])
        
        apply_variation(new_obj)

    print(f"Success: {count} objects scattered within [{min_val}, {max_val}]!")

try:
    my_tool.close() 
except:
    pass

my_tool = ScatterToolUI()
my_tool.show()