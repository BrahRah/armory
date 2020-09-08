from arm.logicnode.arm_nodes import *

class ScreenToWorldSpaceNode(ArmLogicTreeNode):
    """Screen to world space node"""
    bl_idname = 'LNScreenToWorldSpaceNode'
    bl_label = 'Screen To World Space'

    def init(self, context):
        self.add_input('NodeSocketVector', 'Vector')
        self.add_output('NodeSocketVector', 'Vector')

add_node(ScreenToWorldSpaceNode, category=MODULE_AS_CATEGORY, section='matrix')
