# Christopher S Sadler
# Bubbles

import nimble
from nimble import cmds
from random import randint
from random import uniform
from pyglass.widgets.PyGlassWidget import PyGlassWidget

#___________________________________________________________________________________________________ BubbleWidget
class BubbleWidget(PyGlassWidget):
    """A class for Assignment 1"""

#===================================================================================================
#                                                                                       C L A S S

#___________________________________________________________________________________________________ __init__
    def __init__(self, parent, **kwargs):
        """Creates a new instance of Bubble."""
        super(BubbleWidget, self).__init__(parent, **kwargs)
        self.exampleBtn.clicked.connect(self._handleExampleButton)
        self.homeBtn.clicked.connect(self._handleReturnHome)

#===================================================================================================
#                                                                                 H A N D L E R S

#___________________________________________________________________________________________________ _handleReturnHome
    def _handleExampleButton(self):
        """
        This callback creates a polygonal cylinder in the Maya scene.

        """
        x = 0
        y = 0
        z = 0

        sx = 0.1 # original scale size x
        sy = 0.1 # original scale size y
        sz = 0.1 # original scale size z
        so = 0.1 # scale original for exp growth form

        maxY = 30 # highest bound
        maxX = 5 # max horizon bound
        maxZ = 5 # max horzon bound

        keyStep = 3 #  3 * 10 = 30 fps
        totalTime = 10 # number of seconds of animation

        maxKey = totalTime * keyStep * 10 # max num of keys for the time
        randFrameStart = randint(1,maxKey) # Start randomly in time
        minHdev = -2.0 # max movement between horizon space
        maxHdev = 2.0 # max movement beteen horiz space

        scaleRate = 0.2 # for growth of bubble exponentially as a decimal
        time = 0 # amount of time since bubble creation

        bubbleToTop = 1 # seconds for life of bubble

        # Create Spehere nurb, the [0] selects first node of object
        r = 1
        yUp = (0, 1, 0)	 	# start creation at y-up
        p = (0,0,0) 		# object pivot point
        d = 3 				# degree
        bNum = 1			# bNum is the bubble number

        c = cmds.sphere( p=p, ax=yUp, ssw=0, esw=360, r=r, d=d, ut=0, tol=0.01, s=8, nsp=4, ch=1, n='bubble' + str(bNum))[0]
        cmds.select(c)



        for i in xrange(1, maxKey, keyStep):
        # for later use    for i in xrange(randFrameStart, maxKey, keyStep):
            cmds.currentTime( i )
            cmds.setKeyframe( v = y, at='translateY' )
            cmds.setKeyframe( v = x, at='translateX' )
            cmds.setKeyframe( v = z, at='translateZ' )


            x = x + uniform(minHdev, maxHdev)
            z = z + uniform(minHdev, maxHdev)
            y = y + (keyStep / bubbleToTop)

            if x >= maxX:
                x = maxX

            if z >= maxZ:
                z = maxZ

            sx = so * ((1 + scaleRate)**time)
            sz = so * ((1 + scaleRate)**time)
            sy = so * ((1 + scaleRate)**time)

            cmds.setKeyframe( v = sy, at='scaleY' )
            cmds.setKeyframe( v = sx, at='scaleX' )
            cmds.setKeyframe( v = sz, at='scaleZ' )

            time = time + 1

            if y >maxY:
                break # terminate movement which can explode bubble later


        response = nimble.createRemoteResponse(globals())
        response.put('name', c)
#___________________________________________________________________________________________________ _handleReturnHome
    def _handleReturnHome(self):
        self.mainWindow.setActiveWidget('home')
