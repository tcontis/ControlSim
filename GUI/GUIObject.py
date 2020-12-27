from abc import ABC

"""
Generic abstract class for a GUIObject
"""
class GUIObject(ABC):

    def update(self, new_state):
        pass

    def get_position(self):
        pass

    def get_rotation(self):
        pass

    def get_artists(self):
        pass