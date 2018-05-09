import FreeCAD as App, Part, alceD, PartGui
import FreeCADGui as Gui


class One_crearAlceClass():

    def GetResources(self):
        return {'Pixmap' : alceD.ICON_PATH + '/cubito.png',
                'MenuText' : "Add a pipe",
                'ToolTip' : "Adds a pipe"
        }

    def Activated(self):
        from Scripts import Cubito

    def IsActive(self):
            return True

Gui.addCommand ('One_crearAlce', One_crearAlceClass())
