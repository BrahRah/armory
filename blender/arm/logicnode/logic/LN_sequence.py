from arm.logicnode.arm_nodes import *

class SequenceNode(ArmLogicTreeNode):
    """Sequence node"""
    bl_idname = 'LNSequenceNode'
    bl_label = 'Sequence'

    def __init__(self):
        array_nodes[str(id(self))] = self

    def init(self, context):
        self.add_input('ArmNodeSocketAction', 'In')

    def draw_buttons(self, context, layout):
        row = layout.row(align=True)

        op = row.operator('arm.node_add_output', text='New', icon='PLUS', emboss=True)
        op.node_index = str(id(self))
        op.socket_type = 'ArmNodeSocketAction'
        op2 = row.operator('arm.node_remove_output', text='', icon='X', emboss=True)
        op2.node_index = str(id(self))

add_node(SequenceNode, category=MODULE_AS_CATEGORY, section='flow')
