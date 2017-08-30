import c4d

from ..Const import Const
from .JsonFunction import JsonFunction

const = Const()


class ConfigManagerC4D(JsonFunction):
    def createC4DCheckBox(self, dialog):
        dialog.AddCheckbox(const.OPTION_C4D_ENABLE_VIEWPORT,c4d.BFH_LEFT | c4d.BFV_TOP ,0 ,0, "Enable Viewport")
        dialog.AddCheckbox(const.OPTION_C4D_ENABLE_RENDER,c4d.BFH_LEFT | c4d.BFV_TOP ,0 ,0, "Enable Render")
        dialog.AddCheckbox(const.OPTION_C4D_NO_ILLUMINATION,c4d.BFH_LEFT | c4d.BFV_TOP ,0 ,0, "No Illumination")
        dialog.AddCheckbox(const.OPTION_C4D_AMBIANT_ILLUMINATION,c4d.BFH_LEFT | c4d.BFV_TOP ,0 ,0, "Ambiant Illumination")
        dialog.AddCheckbox(const.OPTION_C4D_DIFFUSE,c4d.BFH_LEFT | c4d.BFV_TOP ,0 ,0, "Diffuse")
        dialog.AddCheckbox(const.OPTION_C4D_SPECULAR,c4d.BFH_LEFT | c4d.BFV_TOP ,0 ,0, "Specular")
        dialog.AddCheckbox(const.OPTION_C4D_GI_ILLUMINATION,c4d.BFH_LEFT | c4d.BFV_TOP ,0 ,0, "GI Illumination")
        dialog.AddCheckbox(const.OPTION_C4D_LIGHT_TYPE,c4d.BFH_LEFT | c4d.BFV_TOP ,0 ,0, "Light Type")
        dialog.AddCheckbox(const.OPTION_C4D_LIGHT_COLOR,c4d.BFH_LEFT | c4d.BFV_TOP ,0 ,0, "Light Color")
        dialog.AddCheckbox(const.OPTION_C4D_LIGHT_INTENSITY,c4d.BFH_LEFT | c4d.BFV_TOP ,0 ,0, "Light Intensity")
        dialog.AddCheckbox(const.OPTION_C4D_LIGHT_USE_DECAY,c4d.BFH_LEFT | c4d.BFV_TOP ,0 ,0, "Use Decay")
        dialog.AddCheckbox(const.OPTION_C4D_LIGHT_DECAY_RADIUS,c4d.BFH_LEFT | c4d.BFV_TOP ,0 ,0, "Decay Radius")
        dialog.AddCheckbox(const.OPTION_C4D_LIGHT_USE_VISIBILITY,c4d.BFH_LEFT | c4d.BFV_TOP ,0 ,0, "Use Visibility")
        dialog.AddCheckbox(const.OPTION_C4D_LIGHT_VISIBILITY_PERCENT,c4d.BFH_LEFT | c4d.BFV_TOP ,0 ,0, "Visibility Percent")
        dialog.AddCheckbox(const.OPTION_C4D_LIGHT_VISIBILITY_RADIUS,c4d.BFH_LEFT | c4d.BFV_TOP ,0 ,0, "Visibility Radius")
        dialog.AddCheckbox(const.OPTION_C4D_SHADOW_USE,c4d.BFH_LEFT | c4d.BFV_TOP ,0 ,0, "Shadow Type")
        dialog.AddCheckbox(const.OPTION_C4D_SHADOW_DENSITY,c4d.BFH_LEFT | c4d.BFV_TOP ,0 ,0, "Shadow Density")
        dialog.AddCheckbox(const.OPTION_C4D_SHADOW_COLOR,c4d.BFH_LEFT | c4d.BFV_TOP ,0 ,0, "Shadow Color")
        dialog.AddCheckbox(const.OPTION_C4D_SHADOW_RESOLUTION,c4d.BFH_LEFT | c4d.BFV_TOP ,0 ,0, "Shadow Resolution")
        dialog.AddCheckbox(const.OPTION_C4D_SHADOW_BIAS,c4d.BFH_LEFT | c4d.BFV_TOP ,0 ,0, "Shadow Bias")
        dialog.AddCheckbox(const.OPTION_C4D_SHADOW_ACCURACY,c4d.BFH_LEFT | c4d.BFV_TOP ,0 ,0, "Shadow Accuracy")
        dialog.AddCheckbox(const.OPTION_C4D_SHADOW_MIN_SAMPLE,c4d.BFH_LEFT | c4d.BFV_TOP ,0 ,0, "Shadow Min Sample")
        dialog.AddCheckbox(const.OPTION_C4D_SHADOW_MAX_SAMPLE,c4d.BFH_LEFT | c4d.BFV_TOP ,0 ,0, "Shadow Max Sample")
        dialog.AddCheckbox(const.OPTION_C4D_LAYER,c4d.BFH_LEFT | c4d.BFV_TOP ,0 ,0, "Layer")

        self.fillC4DCheckBox(dialog)

    def fillC4DCheckBox(self, dialog):
        self.jsonContent = self.loadJsonFile()
        self.c4dConfig = self.jsonContent["c4d"]

        dialog.SetBool(const.OPTION_C4D_ENABLE_VIEWPORT, self.c4dConfig["enableViewport"])
        dialog.SetBool(const.OPTION_C4D_ENABLE_RENDER, self.c4dConfig["enableRender"])
        dialog.SetBool(const.OPTION_C4D_NO_ILLUMINATION, self.c4dConfig["noIllumination"])
        dialog.SetBool(const.OPTION_C4D_AMBIANT_ILLUMINATION, self.c4dConfig["ambiantIllumination"])
        dialog.SetBool(const.OPTION_C4D_DIFFUSE, self.c4dConfig["diffuse"])
        dialog.SetBool(const.OPTION_C4D_SPECULAR, self.c4dConfig["specular"])
        dialog.SetBool(const.OPTION_C4D_GI_ILLUMINATION, self.c4dConfig["giIllumination"])
        dialog.SetBool(const.OPTION_C4D_LIGHT_TYPE, self.c4dConfig["lightType"])
        dialog.SetBool(const.OPTION_C4D_LIGHT_COLOR, self.c4dConfig["lightColor"])
        dialog.SetBool(const.OPTION_C4D_LIGHT_INTENSITY, self.c4dConfig["lightIntensity"])
        dialog.SetBool(const.OPTION_C4D_LIGHT_USE_DECAY, self.c4dConfig["useDecay"])
        dialog.SetBool(const.OPTION_C4D_LIGHT_DECAY_RADIUS, self.c4dConfig["decayRadius"])
        dialog.SetBool(const.OPTION_C4D_LIGHT_USE_VISIBILITY, self.c4dConfig["useVisibility"])
        dialog.SetBool(const.OPTION_C4D_LIGHT_VISIBILITY_PERCENT, self.c4dConfig["visibilityPercent"])
        dialog.SetBool(const.OPTION_C4D_LIGHT_VISIBILITY_RADIUS, self.c4dConfig["visibilityRadius"])
        dialog.SetBool(const.OPTION_C4D_SHADOW_USE, self.c4dConfig["shadowUse"])
        dialog.SetBool(const.OPTION_C4D_SHADOW_DENSITY, self.c4dConfig["shadowDensity"])
        dialog.SetBool(const.OPTION_C4D_SHADOW_COLOR, self.c4dConfig["shadowColor"])
        dialog.SetBool(const.OPTION_C4D_SHADOW_RESOLUTION, self.c4dConfig["shadowResolution"])
        dialog.SetBool(const.OPTION_C4D_SHADOW_BIAS, self.c4dConfig["shadowBias"])
        dialog.SetBool(const.OPTION_C4D_SHADOW_ACCURACY, self.c4dConfig["shadowAccuracy"])
        dialog.SetBool(const.OPTION_C4D_SHADOW_MIN_SAMPLE, self.c4dConfig["shadowMinSample"])
        dialog.SetBool(const.OPTION_C4D_SHADOW_MAX_SAMPLE, self.c4dConfig["shadowMaxSample"])
        dialog.SetBool(const.OPTION_C4D_LAYER, self.c4dConfig["layer"])

    def generateC4Djson(self, dialog):
        c4d = {}
        c4d["select"]               = dialog.GetBool(const.OPTION_C4D_SELECT)
        c4d["enableViewport"]       = dialog.GetBool(const.OPTION_C4D_ENABLE_VIEWPORT)
        c4d["enableRender"]         = dialog.GetBool(const.OPTION_C4D_ENABLE_RENDER)
        c4d["name"]                 = dialog.GetBool(const.OPTION_C4D_NAME)
        c4d["noIllumination"]       = dialog.GetBool(const.OPTION_C4D_NO_ILLUMINATION)
        c4d["ambiantIllumination"]  = dialog.GetBool(const.OPTION_C4D_AMBIANT_ILLUMINATION)
        c4d["diffuse"]              = dialog.GetBool(const.OPTION_C4D_DIFFUSE)
        c4d["specular"]             = dialog.GetBool(const.OPTION_C4D_SPECULAR)
        c4d["giIllumination"]       = dialog.GetBool(const.OPTION_C4D_GI_ILLUMINATION)
        c4d["lightType"]            = dialog.GetBool(const.OPTION_C4D_LIGHT_TYPE)
        c4d["lightColor"]           = dialog.GetBool(const.OPTION_C4D_LIGHT_COLOR)
        c4d["lightIntensity"]       = dialog.GetBool(const.OPTION_C4D_LIGHT_INTENSITY)
        c4d["useDecay"]             = dialog.GetBool(const.OPTION_C4D_LIGHT_USE_DECAY)
        c4d["decayRadius"]          = dialog.GetBool(const.OPTION_C4D_LIGHT_DECAY_RADIUS)
        c4d["useVisibility"]        = dialog.GetBool(const.OPTION_C4D_LIGHT_USE_VISIBILITY)
        c4d["visibilityPercent"]    = dialog.GetBool(const.OPTION_C4D_LIGHT_VISIBILITY_PERCENT)
        c4d["visibilityRadius"]     = dialog.GetBool(const.OPTION_C4D_LIGHT_VISIBILITY_RADIUS)
        c4d["shadowUse"]            = dialog.GetBool(const.OPTION_C4D_SHADOW_USE)
        c4d["shadowDensity"]        = dialog.GetBool(const.OPTION_C4D_SHADOW_DENSITY)
        c4d["shadowColor"]          = dialog.GetBool(const.OPTION_C4D_SHADOW_COLOR)
        c4d["shadowResolution"]     = dialog.GetBool(const.OPTION_C4D_SHADOW_RESOLUTION)
        c4d["shadowBias"]           = dialog.GetBool(const.OPTION_C4D_SHADOW_BIAS)
        c4d["shadowAccuracy"]       = dialog.GetBool(const.OPTION_C4D_SHADOW_ACCURACY)
        c4d["shadowMinSample"]      = dialog.GetBool(const.OPTION_C4D_SHADOW_MIN_SAMPLE)
        c4d["shadowMaxSample"]      = dialog.GetBool(const.OPTION_C4D_SHADOW_MAX_SAMPLE)
        c4d["layer"]                = dialog.GetBool(const.OPTION_C4D_LAYER)

        self.jsonContent["c4d"] = c4d