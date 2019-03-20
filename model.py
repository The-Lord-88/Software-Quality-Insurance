"""/*
 * @Author: Pierre Loneux 
 * @Date: 2019-03-19 19:41:11 
 * @Last Modified by:   Pierre Loneux 
 * @Last Modified time: 2019-03-19 19:41:11 
 */"""

# Here we just initiate our model, it is used to display text in our window
class Model:
    def __init__(self):
        self.display = ""

    def set_display(self, display):
        self.display = display
