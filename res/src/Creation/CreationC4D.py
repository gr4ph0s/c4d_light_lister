import c4d

from ..Const import Const
from CreationFunction import CreationFunction

const = Const()

class CreationC4D(CreationFunction):
    def refresh_c4d_light(self, dialog, list_lights):
        try:
            save_light = dialog.GetVisibleArea(const.GRP_TAB_C4D_SCROLL_LIGHT)

            #Name
            self.create_edit_string(dialog, const.LIGHT_LISTER_NAME,
                                    "Name", const.OBJ, list_lights, True)

            current_light = dialog.GetVisibleArea(const.GRP_TAB_C4D_SCROLL_LIGHT)

            decalage = save_light["x2"] - current_light["x2"]
            size_x = current_light["x2"] - current_light["x1"]
            if decalage > 0 and current_light["x1"] < size_x :
                decalage = 0 - decalage
            dialog.SetVisibleArea(const.GRP_TAB_C4D_SCROLL_LIGHT,
                                  current_light["x1"] + decalage,
                                  current_light["y1"],
                                  current_light["x2"] + decalage,
                                  current_light["y2"]
                                  )
        except:
            pass


    def create_c4d_light(self, dialog, config, c4d_lights, layers):
        if not len(c4d_lights):
            return

        dialog.ScrollGroupBegin(const.GRP_TAB_C4D_SCROLL_NAME, c4d.BFH_LEFT | c4d.BFV_SCALEFIT, c4d.SCROLLGROUP_VERT | c4d.SCROLLGROUP_LEFT | c4d.SCROLLGROUP_AUTOVERT, 0, 0)
        if dialog.GroupBegin(const.GRP_TAB_C4D_GRP, c4d.BFH_LEFT | c4d.BFV_SCALEFIT, 300, 200, "C4D"):
            dialog.GroupBorderSpace(0, 0, 10, 15)

            self.create_min_max_button(dialog, const.LIGHT_LISTER_C4D_ORDER_GRP, const.LIGHT_LISTER_C4D_ORDER_UP, const.LIGHT_LISTER_C4D_ORDER_DOWN, c4d_lights)

            #select
            self.create_button(dialog, const.LIGHT_LISTER_SELECT,
                             "Select", "S", c4d_lights)

            #Name
            self.create_edit_string(dialog, const.LIGHT_LISTER_NAME,
                                  "Name", const.OBJ, c4d_lights)

            self.create_enable(dialog, const.LIGHT_LISTER_C4D_ENABLE, c4d_lights)

        dialog.GroupEnd()
        dialog.GroupEnd()


        dialog.ScrollGroupBegin(const.GRP_TAB_C4D_SCROLL_LIGHT, c4d.BFH_SCALEFIT | c4d.BFV_SCALEFIT, c4d.SCROLLGROUP_HORIZ | c4d.SCROLLGROUP_VERT | c4d.SCROLLGROUP_AUTOVERT , 0, 0)
        if dialog.GroupBegin(const.GRP_TAB_C4D_GRP, c4d.BFH_SCALEFIT | c4d.BFV_SCALEFIT, 300, 200, "C4D"):

            #visibility viewport
            if config["enableViewport"]:
                buffer = [{"id": 2, "text": "Default"},
                          {"id": 0, "text": "On"},
                          {"id": 1, "text": "Off"}]
                self.create_cycle_button(dialog, const.LIGHT_LISTER_ENABLE_VIEWPORT,
                                       "Viewport", buffer, const.OBJ, c4d_lights, c4d.ID_BASEOBJECT_VISIBILITY_EDITOR)

            #Visibility render
            if config["enableRender"]:
                buffer = [{"id": 2, "text": "Default"},
                          {"id": 0, "text": "On"},
                          {"id": 1, "text": "Off"}]
                self.create_cycle_button(dialog, const.LIGHT_LISTER_ENABLE_RENDER,
                                       "Render", buffer, const.OBJ, c4d_lights, c4d.ID_BASEOBJECT_VISIBILITY_RENDER)

            #No illum
            if config["noIllumination"]:
                self.create_checkbox(dialog, const.LIGHT_LISTER_NO_ILLUMINATION,
                                   "No illum", const.OBJ, c4d_lights, c4d.LIGHT_NOLIGHTRADIATION)

            #Ambiant illum
            if config["ambiantIllumination"]:
                self.create_checkbox(dialog, const.LIGHT_LISTER_AMBIANT_ILLUMINATION,
                                   "Amb illum", const.OBJ, c4d_lights, c4d.LIGHT_DETAILS_AMBIENT)

            #Diffuse
            if config["diffuse"]:
                self.create_checkbox(dialog, const.LIGHT_LISTER_DIFFUSE,
                                   "Diff", const.OBJ, c4d_lights, c4d.LIGHT_DETAILS_DIFFUSE)

            #Specular
            if config["specular"]:
                self.create_checkbox(dialog, const.LIGHT_LISTER_SPECULAR,
                                   "Spec", const.OBJ, c4d_lights, c4d.LIGHT_DETAILS_SPECULAR)

            #Gi illum
            if config["giIllumination"]:
                self.create_checkbox(dialog, const.LIGHT_LISTER_GI_ILLUM,
                                   "GI", const.OBJ, c4d_lights, c4d.LIGHT_DETAILS_GI)

            #Light type
            if config["lightType"]:
                buffer = [{"id": 0, "text": "Omni"},
                          {"id": 1, "text": "Spot"},
                          {"id": 3, "text": "Infinite"},
                          {"id": 8, "text": "Area"},
                          {"id": 2, "text": "Square Spot"},
                          {"id": 4, "text": "Parallel"},
                          {"id": 5, "text": "Parallel Spot"},
                          {"id": 6, "text": "Square Parallel Spot"},
                          {"id": 9, "text": "IES"}]
                self.create_cycle_button(dialog, const.LIGHT_LISTER_LIGHT_TYPE,
                                       "Light Type", buffer, const.OBJ, c4d_lights, c4d.LIGHT_TYPE)

            #Light color
            if config["lightColor"]:
                self.create_color_field(dialog, const.LIGHT_LISTER_LIGHT_COLOR,
                                      "Color", const.OBJ, c4d_lights, c4d.LIGHT_COLOR)

            #Light intensity
            if config["lightIntensity"]:
                self.create_number_edit(dialog, const.LIGHT_LISTER_LIGHT_INTENSITY,
                                      "Intensity", const.PERCENT_MODE, const.OBJ, c4d_lights, c4d.LIGHT_BRIGHTNESS, -100000.0, 100000.0)

            #Use decay
            if config["useDecay"]:
                buffer = [{"id": 0, "text": "None"},
                          {"id": 10, "text": "Inverse Square Physically"},
                          {"id": 8, "text": "Linear"},
                          {"id": 5, "text": "Step"},
                          {"id": 7, "text": "Inverse Square Clamped"}]
                self.create_cycle_button(dialog, const.LIGHT_LISTER_LIGHT_USE_DECAY,
                                       "Use Decay", buffer, const.OBJ, c4d_lights, c4d.LIGHT_DETAILS_FALLOFF)

            #Decay radius
            if config["decayRadius"]:
                self.create_number_edit(dialog, const.LIGHT_LISTER_LIGHT_DECAY_RADIUS,
                                      "Decay", const.METER_MODE, const.OBJ, c4d_lights, c4d.LIGHT_DETAILS_OUTERDISTANCE, 0, 2147483647.0)

            #Use visibility
            if config["useVisibility"]:
                buffer = [{"id": 0, "text": "None"},
                          {"id": 1, "text": "Visible"},
                          {"id": 2, "text": "Volumetric"},
                          {"id": 3, "text": "Inverse Volumetric"}]
                self.create_cycle_button(dialog, const.LIGHT_LISTER_LIGHT_USE_VISIBILITY,
                                       "Visibility", buffer, const.OBJ, c4d_lights, c4d.LIGHT_VLTYPE)

            #Visibility percent
            if config["visibilityPercent"]:
                self.create_number_edit(dialog, const.LIGHT_LISTER_LIGHT_VISIBILITY_PERCENT,
                                      "Visibility", const.PERCENT_MODE, const.OBJ, c4d_lights, c4d.LIGHT_VISIBILITY_BRIGHTNESS, 0.0, 100.0)

            #Visibility percent
            if config["visibilityRadius"]:
                self.create_number_edit(dialog, const.LIGHT_LISTER_LIGHT_VISIBILITY_RADIUS,
                                      "Visibility", const.METER_MODE, const.OBJ, c4d_lights, c4d.LIGHT_VISIBILITY_OUTERDISTANCE, 0.0, 2147483647.0)

            #Shadow use
            if config["shadowUse"]:
                buffer = [{"id": 0, "text": "None"},
                          {"id": 1, "text": "Shadow Map"},
                          {"id": 2, "text": "Raytraced"},
                          {"id": 3, "text": "Area"}]
                self.create_cycle_button(dialog, const.LIGHT_LISTER_SHADOW_USE,
                                       "Shadow", buffer,const.OBJ, c4d_lights, c4d.LIGHT_SHADOWTYPE_VIRTUAL)

            #Shadow density
            if config["shadowDensity"]:
                self.create_number_edit(dialog, const.LIGHT_LISTER_SHADOW_DENSITY,
                                      "Shadow", const.PERCENT_MODE, const.OBJ, c4d_lights, c4d.LIGHT_SHADOW_DENSITY, 0, 100.0)

            #Light color
            if config["shadowColor"]:
                self.create_color_field(dialog, const.LIGHT_LISTER_SHADOW_COLOR,
                                      "Shadow",const.OBJ, c4d_lights, c4d.LIGHT_SHADOW_COLOR)

            #Use decay
            if config["shadowResolution"]:
                buffer = [{"id": 0, "text": "250x250"},
                          {"id": 1, "text": "500x500"},
                          {"id": 2, "text": "750x750"},
                          {"id": 3, "text": "1000x1000"},
                          {"id": 4, "text": "1250x1250"},
                          {"id": 5, "text": "1500x1500"},
                          {"id": 6, "text": "1750x1750"},
                          {"id": 7, "text": "2000x2000"}]
                self.create_cycle_button(dialog, const.LIGHT_LISTER_SHADOW_RESOLUTION,
                                       "Resolution", buffer, const.OBJ, c4d_lights, c4d.LIGHT_SHADOW_MAPSIZE)

            #shadow bias
            if config["shadowBias"]:
                self.create_number_edit(dialog, const.LIGHT_LISTER_SHADOW_BIAS,
                                      "Bias", const.METER_MODE, const.OBJ, c4d_lights, c4d.LIGHT_SHADOW_ABSOLUTEBIAS, 0.0, 2147483647.0)

            #Shadow accuracy
            if config["shadowAccuracy"]:
                self.create_number_edit(dialog, const.LIGHT_LISTER_SHADOW_ACCURACY,
                                      "Shadow Accuracy", const.PERCENT_MODE, const.OBJ, c4d_lights, c4d.LIGHT_SHADOW_DENSITY, 0, 100)

            #shadow min sample
            if config["shadowMinSample"]:
                self.create_number_edit(dialog, const.LIGHT_LISTER_SHADOW_MIN_SAMPLE,
                                      "Min Sample", const.INT_MODE, const.OBJ, c4d_lights, c4d.LIGHT_SHADOW_MINSAMPLES, 2, 10000)

            #shadow max sample
            if config["shadowMaxSample"]:
                self.create_number_edit(dialog, const.LIGHT_LISTER_SHADOW_MAX_SAMPLE,
                                      "Max Sample", const.INT_MODE, const.OBJ, c4d_lights, c4d.LIGHT_SHADOW_MAXSAMPLES, 2, 10000)

            #Layers
            if config["layer"]:
                buffer = list()
                buffer.append({"id": 0, "text": "None"})
                for i in xrange(len(layers)):
                    buffer.append({"id": i+1, "text": layers[i].GetName()})

                self.create_cycle_button(dialog, const.LIGHT_LISTER_C4D_LAYER,
                                       "Layer", buffer, const.OBJ, c4d_lights, layers=layers)

        dialog.GroupEnd()
        dialog.GroupEnd()

        self.disable_data(dialog, c4d_lights, layers)

    def disable_data(self, dialog, c4d_lights, layers):
        for i in xrange(len(c4d_lights)):
            #use decay
            if not dialog.GetLong(const.LIGHT_LISTER_LIGHT_USE_DECAY + i + 2):
                dialog.Enable(const.LIGHT_LISTER_LIGHT_DECAY_RADIUS + i + 2, False)
            else:
                dialog.Enable(const.LIGHT_LISTER_LIGHT_DECAY_RADIUS + i + 2, True)

            if not dialog.GetLong(const.LIGHT_LISTER_LIGHT_USE_VISIBILITY + i + 2):
                dialog.Enable(const.LIGHT_LISTER_LIGHT_VISIBILITY_PERCENT + i + 2, False)
                dialog.Enable(const.LIGHT_LISTER_LIGHT_VISIBILITY_RADIUS + i + 2, False)
            else:
                dialog.Enable(const.LIGHT_LISTER_LIGHT_VISIBILITY_PERCENT + i + 2, True)
                dialog.Enable(const.LIGHT_LISTER_LIGHT_VISIBILITY_RADIUS + i + 2, True)

            #Not shadow
            if not dialog.GetLong(const.LIGHT_LISTER_SHADOW_USE + i + 2):
                dialog.Enable(const.LIGHT_LISTER_SHADOW_DENSITY + i + 2, False)
                dialog.Enable(const.LIGHT_LISTER_SHADOW_COLOR + i + 2, False)
                dialog.Enable(const.LIGHT_LISTER_SHADOW_RESOLUTION + i + 2, False)
                dialog.Enable(const.LIGHT_LISTER_SHADOW_BIAS + i + 2, False)
                dialog.Enable(const.LIGHT_LISTER_SHADOW_ACCURACY + i + 2, False)
                dialog.Enable(const.LIGHT_LISTER_SHADOW_MIN_SAMPLE + i + 2, False)
                dialog.Enable(const.LIGHT_LISTER_SHADOW_MAX_SAMPLE + i + 2, False)

            #Soft shadows
            elif dialog.GetLong(const.LIGHT_LISTER_SHADOW_USE + i + 2) == 1:
                dialog.Enable(const.LIGHT_LISTER_SHADOW_DENSITY + i + 2, True)
                dialog.Enable(const.LIGHT_LISTER_SHADOW_COLOR + i + 2, True)
                dialog.Enable(const.LIGHT_LISTER_SHADOW_RESOLUTION + i + 2, True)
                dialog.Enable(const.LIGHT_LISTER_SHADOW_BIAS + i + 2, True)
                dialog.Enable(const.LIGHT_LISTER_SHADOW_ACCURACY + i + 2, False)
                dialog.Enable(const.LIGHT_LISTER_SHADOW_MIN_SAMPLE + i + 2, False)
                dialog.Enable(const.LIGHT_LISTER_SHADOW_MAX_SAMPLE + i + 2, False)

            #Raytraced
            elif dialog.GetLong(const.LIGHT_LISTER_SHADOW_USE + i + 2) == 3:
                dialog.Enable(const.LIGHT_LISTER_SHADOW_DENSITY + i + 2, True)
                dialog.Enable(const.LIGHT_LISTER_SHADOW_COLOR + i + 2, True)
                dialog.Enable(const.LIGHT_LISTER_SHADOW_RESOLUTION + i + 2, False)
                dialog.Enable(const.LIGHT_LISTER_SHADOW_BIAS + i + 2, False)
                dialog.Enable(const.LIGHT_LISTER_SHADOW_ACCURACY + i + 2, False)
                dialog.Enable(const.LIGHT_LISTER_SHADOW_MIN_SAMPLE + i + 2, False)
                dialog.Enable(const.LIGHT_LISTER_SHADOW_MAX_SAMPLE + i + 2, False)

            #Area
            elif dialog.GetLong(const.LIGHT_LISTER_SHADOW_USE + i + 2) == 2:
                dialog.Enable(const.LIGHT_LISTER_SHADOW_DENSITY + i + 2, True)
                dialog.Enable(const.LIGHT_LISTER_SHADOW_COLOR + i + 2, True)
                dialog.Enable(const.LIGHT_LISTER_SHADOW_RESOLUTION + i + 2, False)
                dialog.Enable(const.LIGHT_LISTER_SHADOW_BIAS + i + 2, False)
                dialog.Enable(const.LIGHT_LISTER_SHADOW_ACCURACY + i + 2, True)
                dialog.Enable(const.LIGHT_LISTER_SHADOW_MIN_SAMPLE + i + 2, True)
                dialog.Enable(const.LIGHT_LISTER_SHADOW_MAX_SAMPLE + i + 2, True)

            #should never happend
            else:
                dialog.Enable(const.LIGHT_LISTER_SHADOW_DENSITY + i + 2, True)
                dialog.Enable(const.LIGHT_LISTER_SHADOW_COLOR + i + 2, True)
                dialog.Enable(const.LIGHT_LISTER_SHADOW_RESOLUTION + i + 2, True)
                dialog.Enable(const.LIGHT_LISTER_SHADOW_BIAS + i + 2, True)
                dialog.Enable(const.LIGHT_LISTER_SHADOW_ACCURACY + i + 2, True)
                dialog.Enable(const.LIGHT_LISTER_SHADOW_MIN_SAMPLE + i + 2, True)
                dialog.Enable(const.LIGHT_LISTER_SHADOW_MAX_SAMPLE + i + 2, True)

            if not len(layers):
                dialog.Enable(const.LIGHT_LISTER_C4D_LAYER + i + 2, False)
            else:
                dialog.Enable(const.LIGHT_LISTER_C4D_LAYER + i + 2, True)
