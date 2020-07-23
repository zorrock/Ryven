from custom_src.NodeInstance import NodeInstance
from custom_src.Node import Node
from custom_src.retain import M

import cv2


# USEFUL
# self.input(index)                    <- access to input data
# self.outputs[index].set_val(val)    <- set output data port value
# self.main_widget                    <- access to main widget


class %NODE_TITLE%_NodeInstance(NodeInstance):
    def __init__(self, parent_node: Node, flow, configuration=None):
        super(%NODE_TITLE%_NodeInstance, self).__init__(parent_node, flow, configuration)

        # self.special_actions['action name'] = {'method': M(self.action_method)}
        self.img_unlined = None
        self.img_lined = None
       

        self.initialized()


    def update_event(self, input_called=-1):
        self.img_unlined = self.input(0)
        startpoint = self.input(1)
        endpoint=self.input(2)
        color=self.input(3)
        thickness=self.input(4)
        
        self.img_lined = cv2.line( self.img_unlined,startpoint,endpoint,color,thickness)
        self.main_widget.show_image(self.img_lined)
        self.set_output_val(0, self.img_lined)

    def get_data(self):
        data = {}
        # ...
        return data

    def set_data(self, data):
        pass
        # ...



    # optional - important for threading - stop everything here
    def removing(self):
        pass
