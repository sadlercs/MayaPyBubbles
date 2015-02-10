# Christopher S Sadler
# Bubbles

import nimble
from nimble import cmds
from random import randint
from random import uniform
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
        self.exampleBtn.clicked.connect(self._handleExampleButton)
        self.homeBtn.clicked.connect(self._handleReturnHome)



#===================================================================================================
#                                                                                 H A N D L E R S

#___________________________________________________________________________________________________ _handleReturnHome
    def _handleExampleButton(self):
        """
        This callback creates a polygonal container and fills it with bubbles.
        """

        sx = 0.1 # original scale size x
        sy = 0.1 # original scale size y
        sz = 0.1 # original scale size z
        so = 0.1 # scale original for exp growth form

        maxY = 10 # highest bound
        maxX = 5 # max horizon bound
        maxZ = 5 # max horzon bound

        # Create container material
        containerShader =  mayaShader('container_mat', (0.6,0.6,0.6), (0.9,0.9,0.9), (0.8,0.8,0.8), 'blinn')
        containerShader.create()

        # Create Container
        cHeight = 12
        c = cmds.polyCylinder( r = 11, h = cHeight, sx = 40, sy = 10, sz = 0, ax = (0,1,0), rcp = 0, cuv = 3, ch=1, n='container1')[0]
        cmds.select(c)
        cmds.setAttr("container1.translateY", cHeight/2 - 0.5)

        # create another mesh smaller
        cHeight = 12
        c = cmds.polyCylinder( r = 10.5, h = cHeight, sx = 40, sy = 10, sz = 0, ax = (0,1,0), rcp = 0, cuv = 3, ch=1, n='container2')[0]
        cmds.select(c)
        cmds.setAttr("container2.translateY", cHeight/2)

        # Boolean difference for making container
        cmds.polyCBoolOp( 'container1', 'container2', op=2, n='container' )

        # Assign container_mat
        cmds.hyperShade( a = "container_mat")



        keyStep = 3 #  3 * 10 = 30 fps
        totalTime = 10 # number of seconds of animation

        maxKey = totalTime * keyStep * 10 # max num of keys for the time
        minHdev = -2.0 # max movement between horizon space
        maxHdev = 2.0 # max movement beteen horiz space

        numBubbles = 50 # make 20 bubbles

        scaleRate = 0.2 # for growth of bubble exponentially as a decimal

        bubbleToTop = 1 # seconds for life of bubble

        # Create Material
        # Start bubble_mat
        bubbleShader =  mayaShader('bubble_mat', (0.0,0.8,1.0), (0.9,0.9,0.9), (0.8,0.8,0.8), 'blinn')
        bubbleShader.create()
        #end bubble_mat


        for i in xrange(0, numBubbles):
            x = 0
            y = 0
            z = 0

            time = 0 # amount of time since bubble creation

            # Create Spehere nurb, the [0] selects first node of object
            randX = uniform(-maxX, maxX)
            randZ = uniform(-maxZ, maxZ)
            r = 1
            yUp = (0, 1, 0)	 	# start creation at y-up
            p = (randX,0,randZ) 		# object pivot point
            d = 3 				# degree
            bNum = 1			# bNum is the bubble number


            c = cmds.sphere( p=p, ax=yUp, ssw=0, esw=360, r=r, d=d, ut=0, tol=0.01, s=8, nsp=4, ch=1, n='bubble' + str(bNum))[0]
            cmds.select(c)

            # Assign bubble_mat
            cmds.hyperShade( a = "bubble_mat")

            randFrameStart = randint(1,maxKey) # Start randomly in time

            for j in xrange(randFrameStart, maxKey, keyStep):
                cmds.currentTime( j )
                cmds.setKeyframe( v = y, at='translateY' )
                cmds.setKeyframe( v = x, at='translateX' )
                cmds.setKeyframe( v = z, at='translateZ' )


                x = x + uniform(minHdev, maxHdev)
                z = z + uniform(minHdev, maxHdev)
                y = y + (keyStep / bubbleToTop)
                print(y)
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




class mayaShader:
    """A simple shader class"""
    def __init__(self, name, color, trans, specClr, type,):
        self.name = name
        self.color = color
        self.type = type
        self.trans = trans
        self.specClr = specClr

    def create(self):
        #checking if shader exists
        shadExist = 0
        allShaders = cmds.ls(mat=1)
        for shadeCheck in allShaders:
            if(shadeCheck == self.name):
                shadExist = 1

        if (shadExist == 0):
            cmds.sets(renderable=True, noSurfaceShader=True, empty=True, name=self.name+"SG")
            cmds.shadingNode(self.type, asShader=True, name=self.name)
            # 0.0, 0.8, 1.0 color
            cmds.setAttr( self.name+".color", self.color[0], self.color[1], self.color[2], type='double3')
            #transparency between 0.8 - 0.9 is good
            cmds.setAttr(self.name+".transparency", self.trans[0], self.trans[1], self.trans[2], type="double3")
            cmds.setAttr( self.name+".specularColor", self.specClr[0], self.specClr[1], self.specClr[2], type='double3')
            cmds.connectAttr(self.name+".outColor", self.name+"SG.surfaceShader", f=True)
