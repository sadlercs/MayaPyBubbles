# MayaPyMainWindow.py
# (C)2013
# Scott Ernst

from PySide import QtGui

from pyglass.windows.PyGlassWindow import PyGlassWindow

from mayapy.views.home.MayaPyHomeWidget import MayaPyHomeWidget
from mayapy.views.bubble.BubbleWidget import BubbleWidget
from mayapy.views.bubbles.BubblesWidget import BubblesWidget

#___________________________________________________________________________________________________ MayaPyMainWindow
class MayaPyMainWindow(PyGlassWindow):
    """A class for..."""

#===================================================================================================
#                                                                                       C L A S S

#___________________________________________________________________________________________________ __init__
    def __init__(self, **kwargs):
        PyGlassWindow.__init__(
            self,
            widgets={
                'home':MayaPyHomeWidget,
                'bubble':BubbleWidget,
                'bubbles':BubblesWidget },
            title='Bubbles - Shawn Sadler',
            **kwargs )

        self.setMinimumSize(1024,480)
        self.setContentsMargins(0, 0, 0, 0)

        widget = self._createCentralWidget()
        layout = QtGui.QVBoxLayout(widget)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        widget.setLayout(layout)

        self.setActiveWidget('home')
