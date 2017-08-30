import c4d

from ..Const import Const
from .InteractionFunction import InteractionFunction

const = Const()
ifc = InteractionFunction()

class InteractionC4D(InteractionFunction):

    def c4d_interaction(self, dialog, doc, clicked_id, msg, c4d_lights, layers):
        #Order
        self.order_interaction_up(dialog, doc, const.LIGHT_LISTER_C4D_ORDER_UP, clicked_id, c4d_lights)
        self.order_interaction_down(dialog, doc, const.LIGHT_LISTER_C4D_ORDER_DOWN, clicked_id, c4d_lights)

        #Select
        self.selection_interaction(doc, const.LIGHT_LISTER_SELECT, clicked_id, msg, c4d_lights)

        #Name
        self.name_interaction(dialog, doc, const.LIGHT_LISTER_NAME, clicked_id, c4d_lights)

        #enable
        self.enable_interaction(dialog, doc, const.LIGHT_LISTER_C4D_ENABLE, clicked_id, c4d_lights)

        #Viewport Change
        self.long_interaction(dialog, doc, const.LIGHT_LISTER_ENABLE_VIEWPORT,
                              clicked_id, c4d_lights, c4d.ID_BASEOBJECT_VISIBILITY_EDITOR)

        #Render Change
        self.long_interaction(dialog, doc, const.LIGHT_LISTER_ENABLE_RENDER,
                              clicked_id, c4d_lights, c4d.ID_BASEOBJECT_VISIBILITY_RENDER)

        #No illum
        self.bool_interaction(dialog, doc, const.LIGHT_LISTER_NO_ILLUMINATION,
                              clicked_id, c4d_lights, c4d.LIGHT_NOLIGHTRADIATION)

        #Ambiant
        self.bool_interaction(dialog, doc, const.LIGHT_LISTER_AMBIANT_ILLUMINATION,
                              clicked_id, c4d_lights, c4d.LIGHT_DETAILS_AMBIENT)

        #Diffuse
        self.bool_interaction(dialog, doc, const.LIGHT_LISTER_DIFFUSE,
                              clicked_id, c4d_lights, c4d.LIGHT_DETAILS_DIFFUSE)

        #Specular
        self.bool_interaction(dialog, doc, const.LIGHT_LISTER_SPECULAR,
                              clicked_id, c4d_lights, c4d.LIGHT_DETAILS_SPECULAR)

        #Gi Illum
        self.bool_interaction(dialog, doc, const.LIGHT_LISTER_GI_ILLUM,
                              clicked_id, c4d_lights, c4d.LIGHT_DETAILS_GI)

        #Light Type
        self.long_interaction(dialog, doc, const.LIGHT_LISTER_LIGHT_TYPE,
                              clicked_id, c4d_lights, c4d.LIGHT_TYPE)

        #Light Color
        self.color_interaction(dialog, doc, const.LIGHT_LISTER_LIGHT_COLOR,
                               clicked_id, c4d_lights, c4d.LIGHT_COLOR)

        #Light Intensity
        self.float_interaction(dialog, doc, const.LIGHT_LISTER_LIGHT_INTENSITY,
                               clicked_id, c4d_lights, c4d.LIGHT_BRIGHTNESS)

        #Use decay
        self.long_interaction(dialog, doc, const.LIGHT_LISTER_LIGHT_USE_DECAY,
                              clicked_id, c4d_lights, c4d.LIGHT_DETAILS_FALLOFF)

        #Decay Radius
        self.float_interaction(dialog, doc, const.LIGHT_LISTER_LIGHT_DECAY_RADIUS,
                               clicked_id, c4d_lights, c4d.LIGHT_DETAILS_OUTERDISTANCE)

        #Use visibility
        self.long_interaction(dialog, doc, const.LIGHT_LISTER_LIGHT_USE_VISIBILITY,
                              clicked_id, c4d_lights, c4d.LIGHT_VLTYPE)

        #Visibility percent
        self.float_interaction(dialog, doc, const.LIGHT_LISTER_LIGHT_VISIBILITY_PERCENT,
                               clicked_id, c4d_lights, c4d.LIGHT_VISIBILITY_BRIGHTNESS)

        #visibilit radius
        self.float_interaction(dialog, doc, const.LIGHT_LISTER_LIGHT_VISIBILITY_RADIUS,
                               clicked_id, c4d_lights, c4d.LIGHT_VISIBILITY_OUTERDISTANCE)

        #Use Shadow
        self.long_interaction(dialog, doc, const.LIGHT_LISTER_SHADOW_USE,
                              clicked_id, c4d_lights, c4d.LIGHT_SHADOWTYPE_VIRTUAL)

        #visibilit radius
        self.float_interaction(dialog, doc, const.LIGHT_LISTER_SHADOW_DENSITY,
                               clicked_id, c4d_lights, c4d.LIGHT_SHADOW_DENSITY)

        #Shadow Color
        self.color_interaction(dialog, doc, const.LIGHT_LISTER_SHADOW_COLOR,
                               clicked_id, c4d_lights, c4d.LIGHT_SHADOW_COLOR)

        #Use Shadow
        self.long_interaction(dialog, doc, const.LIGHT_LISTER_SHADOW_RESOLUTION,
                              clicked_id, c4d_lights, c4d.LIGHT_SHADOW_MAPSIZE)

        #Shadow bias
        self.float_interaction(dialog, doc, const.LIGHT_LISTER_SHADOW_BIAS,
                               clicked_id, c4d_lights, c4d.LIGHT_SHADOW_ABSOLUTEBIAS)

        #Shadow accuracy
        self.float_interaction(dialog, doc, const.LIGHT_LISTER_SHADOW_ACCURACY,
                               clicked_id, c4d_lights, c4d.LIGHT_SHADOW_ACCURACY)

        #Min sample
        self.long_interaction(dialog, doc, const.LIGHT_LISTER_SHADOW_MIN_SAMPLE,
                              clicked_id, c4d_lights, c4d.LIGHT_SHADOW_MINSAMPLES)

        #Max sample
        self.long_interaction(dialog, doc, const.LIGHT_LISTER_SHADOW_MAX_SAMPLE,
                              clicked_id, c4d_lights, c4d.LIGHT_SHADOW_MAXSAMPLES)

        #layer
        self.layer_interaction(dialog, doc, const.LIGHT_LISTER_C4D_LAYER,
                               clicked_id, c4d_lights, layers)

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