import c4d

from ..Const import Const
from .ConfigManagerC4D import ConfigManagerC4D

const = Const()

class ConfigManager(c4d.gui.GeDialog, ConfigManagerC4D):
    def __init__(self):
        self.jsonContent = self.loadJsonFile()
        self.c4dConfig = self.jsonContent["c4d"]
        self.dataChanged = False

    def refresh(self):
        self.jsonContent = self.loadJsonFile()
        self.c4dConfig = self.jsonContent["c4d"]
        self.dataChanged = False

    def Command(self, id, msg):
        if id == const.UI_OPTION_END_OK:
            self.generateC4Djson(self)
            self.jsonContent = self.saveJsonFile(self.jsonContent)
            self.dataChanged = True
            self.Close()

        if id == const.UI_OPTION_END_CANCEL:
            self.Close()

        return True

    def CreateLayout(self):
        self.SetTitle('Config')
        #c4d
        if self.GroupBegin(const.GRP_TAB_C4D_GRP, c4d.BFH_SCALEFIT | c4d.BFV_SCALEFIT, 1, 200, "C4D"):
            if self.ScrollGroupBegin(const.GRP_TAB_C4D_SCROLL_OPT, c4d.BFH_SCALEFIT | c4d.BFV_SCALEFIT, c4d.SCROLLGROUP_VERT, 100, 100):
                if self.GroupBegin(const.GRP_OPT_TAB_C4D, c4d.BFH_SCALEFIT | c4d.BFV_SCALEFIT, 1, 200, "C4D"):
                    self.createC4DCheckBox(self)
                self.GroupEnd()
            self.GroupEnd()
        self.GroupEnd()

        if self.GroupBegin(const.OPTION_C4D_START, c4d.BFH_CENTER | c4d.BFV_CENTER, 100, 100):
            self.GroupBorderSpace(30, 5, 0, 2)

            self.AddButton(const.UI_OPTION_END_OK, c4d.BFH_CENTER | c4d.BFV_TOP, 0, 20, "Ok ")
            self.AddButton(const.UI_OPTION_END_CANCEL, c4d.BFH_CENTER | c4d.BFV_TOP, 0, 20, "Cancel")

        self.GroupEnd()

        return True
