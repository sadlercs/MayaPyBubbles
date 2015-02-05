# Assignment2Widget.py
# (C)2013
# Scott Ernst

from pyglass.widgets.PyGlassWidget import PyGlassWidget

#___________________________________________________________________________________________________ BubblesWidget
class BubblesWidget(PyGlassWidget):
    """A class for..."""

#===================================================================================================
#                                                                                       C L A S S

#___________________________________________________________________________________________________ __init__
    def __init__(self, parent, **kwargs):
        """Creates a new instance of BubblesWidget."""
        super(BubblesWidget, self).__init__(parent, **kwargs)

        self.homeBtn.clicked.connect(self._handleReturnHome)

#===================================================================================================
#                                                                                 H A N D L E R S

#___________________________________________________________________________________________________ _handleReturnHome
    def _handleReturnHome(self):
        self.mainWindow.setActiveWidget('home')
