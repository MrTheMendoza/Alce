# -*- coding: utf-8 -*-

class alceapp (Workbench):
    def __init__(self):
        import alceD
        self.__class__.Icon = alceD.ICON_PATH + '/AddFrame.svg'
        #self.__class__.Icon = FreeCAD.getResourceDir() + 'Mod/alce/resources/icons/AddFrame.svg'
        self.__class__.MenuText = "Alce Consorcio"
        self.__class__.ToolTip = "Alce workbench"

    def Initialize(self):
        "This function is executed when FreeCAD starts"
        import Command_init
        self.list = ["One_crearAlce"]
        self.appendToolbar("Pieza", self.list) 


    def Activated(self):
        if not(FreeCAD.ActiveDocument):
            FreeCAD.newDocument("Figura")

        FreeCAD.Console.PrintMessage('Modulo de Alce Cargado\n')
        return

    def GetClassName(self):
        return "Gui::PythonWorkbench"

Gui.addWorkbench(alceapp())
