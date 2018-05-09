import FreeCAD as App
import FreeCADGui as Gui

box = App.ActiveDocument.addObject("Part::Box", "CUBO")
box.Placement = App.Placement(App.Vector(1, 1, 1), App.Rotation(0, 0, 0, 1))
box.Height = 7.00
box.Length = 4.00
box.Width = 3.00
App.ActiveDocument.recompute()
Gui.SendMsgToActiveView("ViewFit")