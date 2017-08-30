class Const(object):
    PLUGIN_ID           = 1039150
    PLUGIN_ID_TAG       = 1039151
    VERSION             = 1.4

    #===========================================================================================================#
    #                                                                                                           #
    #                                            LIGHT TAG ID                                                   #
    #                                                                                                           #
    #===========================================================================================================#
    TAG_ID_OCTANE = 1029526
    TAG_ID_ARNOLD = 1029989
    TAG_ID_VRAY = 1020441
    LIGHT_C4D_ID = 5102
    LIGHT_ID_REDSHIFT = 1036751
    LIGHT_ID_ARNOLD = 1030424
    LIGHT_ID_CORONA = 1032104

    STEP                = 202
    RENDER_STEP         = 10000

    C4D_RENDER          = 1

    INT_MODE            = 0
    PERCENT_MODE        = 1
    METER_MODE          = 2
    FLOAT_MODE          = 3
    DEGREE_MODE         = 4

    TAG = 0
    OBJ = 1

    #===========================================================================================================#
    #                                                                                                           #
    #                                                   UI ID                                                   #
    #                                                                                                           #
    #===========================================================================================================#
    UI_BTN_OPTION = 100001
    UI_OPTION_END_OK = 100002
    UI_OPTION_END_CANCEL = 100003
    UI_OPTION_END = 100004

    UI_BTN_LICENSE = 100005
    UI_BTN_LICENSE_MAIN_GRP = 100005
    UI_BTN_LICENSE_REDSHIFT = 100007

    UI_BTN_LICENSE_REGISTER_GRP = 100010
    UI_BTN_LICENSE_INPUT = 100011
    UI_BTN_LICENSE_TYPE = 100012
    UI_BTN_LICENSE_START = 100013
    UI_BTN_LICENSE_VALID = 100014
    UI_BTN_LICENSE_CANCEL = 100015
    UI_BTN_LICENSE_OFFLINE = 100016

    GRP_MAIN = 100018
    GRP_TAB = 100019

    GRP_TAB_C4D = 100040
    GRP_TAB_C4D_SCROLL_NAME = 100041
    GRP_TAB_C4D_SCROLL_LIGHT = 100042
    GRP_TAB_C4D_SCROLL_OPT = 100043
    GRP_TAB_C4D_GRP = 100044

    GRP_OPT_TAB_C4D = 100083

    #C4D LightLister ID
    if bool(1):
         LIGHT_LISTER_C4D_START                  = C4D_RENDER * RENDER_STEP + STEP * 0
         LIGHT_LISTER_SELECT                     = C4D_RENDER * RENDER_STEP + STEP * 1
         LIGHT_LISTER_ENABLE_VIEWPORT            = C4D_RENDER * RENDER_STEP + STEP * 2
         LIGHT_LISTER_ENABLE_RENDER              = C4D_RENDER * RENDER_STEP + STEP * 3
         LIGHT_LISTER_NAME                       = C4D_RENDER * RENDER_STEP + STEP * 4
         LIGHT_LISTER_NO_ILLUMINATION            = C4D_RENDER * RENDER_STEP + STEP * 5
         LIGHT_LISTER_AMBIANT_ILLUMINATION       = C4D_RENDER * RENDER_STEP + STEP * 6
         LIGHT_LISTER_DIFFUSE                    = C4D_RENDER * RENDER_STEP + STEP * 7
         LIGHT_LISTER_SPECULAR                   = C4D_RENDER * RENDER_STEP + STEP * 8
         LIGHT_LISTER_GI_ILLUM                   = C4D_RENDER * RENDER_STEP + STEP * 9
         LIGHT_LISTER_LIGHT_TYPE                 = C4D_RENDER * RENDER_STEP + STEP * 10
         LIGHT_LISTER_LIGHT_COLOR                = C4D_RENDER * RENDER_STEP + STEP * 11
         LIGHT_LISTER_LIGHT_INTENSITY            = C4D_RENDER * RENDER_STEP + STEP * 12
         LIGHT_LISTER_LIGHT_USE_DECAY            = C4D_RENDER * RENDER_STEP + STEP * 13
         LIGHT_LISTER_LIGHT_DECAY_RADIUS         = C4D_RENDER * RENDER_STEP + STEP * 14
         LIGHT_LISTER_LIGHT_USE_VISIBILITY       = C4D_RENDER * RENDER_STEP + STEP * 15
         LIGHT_LISTER_LIGHT_VISIBILITY_PERCENT   = C4D_RENDER * RENDER_STEP + STEP * 16
         LIGHT_LISTER_LIGHT_VISIBILITY_RADIUS    = C4D_RENDER * RENDER_STEP + STEP * 17
         LIGHT_LISTER_SHADOW_USE                 = C4D_RENDER * RENDER_STEP + STEP * 18
         LIGHT_LISTER_SHADOW_DENSITY             = C4D_RENDER * RENDER_STEP + STEP * 19
         LIGHT_LISTER_SHADOW_COLOR               = C4D_RENDER * RENDER_STEP + STEP * 20
         LIGHT_LISTER_SHADOW_RESOLUTION          = C4D_RENDER * RENDER_STEP + STEP * 21
         LIGHT_LISTER_SHADOW_BIAS                = C4D_RENDER * RENDER_STEP + STEP * 22
         LIGHT_LISTER_SHADOW_ACCURACY            = C4D_RENDER * RENDER_STEP + STEP * 23
         LIGHT_LISTER_SHADOW_MIN_SAMPLE          = C4D_RENDER * RENDER_STEP + STEP * 24
         LIGHT_LISTER_SHADOW_MAX_SAMPLE          = C4D_RENDER * RENDER_STEP + STEP * 25
         LIGHT_LISTER_C4D_LAYER                  = C4D_RENDER * RENDER_STEP + STEP * 26
         LIGHT_LISTER_C4D_ENABLE                 = C4D_RENDER * RENDER_STEP + STEP * 27
         LIGHT_LISTER_C4D_ORDER_GRP              = C4D_RENDER * RENDER_STEP + STEP * 28
         LIGHT_LISTER_C4D_ORDER_UP               = C4D_RENDER * RENDER_STEP + STEP * 29
         LIGHT_LISTER_C4D_ORDER_DOWN             = C4D_RENDER * RENDER_STEP + STEP * 30
         LIGHT_LISTER_C4D_END                    = C4D_RENDER * RENDER_STEP + STEP * 31

    #C4D Option ID
    if bool(1):
         OPTION_C4D_START                        =  LIGHT_LISTER_C4D_END + 1
         OPTION_C4D_SELECT                       =  LIGHT_LISTER_C4D_END + 2
         OPTION_C4D_ENABLE_VIEWPORT              =  LIGHT_LISTER_C4D_END + 3
         OPTION_C4D_ENABLE_RENDER                =  LIGHT_LISTER_C4D_END + 4
         OPTION_C4D_NAME                         =  LIGHT_LISTER_C4D_END + 5
         OPTION_C4D_NO_ILLUMINATION              =  LIGHT_LISTER_C4D_END + 6
         OPTION_C4D_AMBIANT_ILLUMINATION         =  LIGHT_LISTER_C4D_END + 7
         OPTION_C4D_DIFFUSE                      =  LIGHT_LISTER_C4D_END + 8
         OPTION_C4D_SPECULAR                     =  LIGHT_LISTER_C4D_END + 9
         OPTION_C4D_GI_ILLUMINATION              =  LIGHT_LISTER_C4D_END + 10
         OPTION_C4D_LIGHT_TYPE                   =  LIGHT_LISTER_C4D_END + 11
         OPTION_C4D_LIGHT_COLOR                  =  LIGHT_LISTER_C4D_END + 12
         OPTION_C4D_LIGHT_INTENSITY              =  LIGHT_LISTER_C4D_END + 13
         OPTION_C4D_LIGHT_USE_DECAY              =  LIGHT_LISTER_C4D_END + 14
         OPTION_C4D_LIGHT_DECAY_RADIUS           =  LIGHT_LISTER_C4D_END + 15
         OPTION_C4D_LIGHT_USE_VISIBILITY         =  LIGHT_LISTER_C4D_END + 16
         OPTION_C4D_LIGHT_VISIBILITY_PERCENT     =  LIGHT_LISTER_C4D_END + 17
         OPTION_C4D_LIGHT_VISIBILITY_RADIUS      =  LIGHT_LISTER_C4D_END + 18
         OPTION_C4D_SHADOW_USE                   =  LIGHT_LISTER_C4D_END + 19
         OPTION_C4D_SHADOW_DENSITY               =  LIGHT_LISTER_C4D_END + 20
         OPTION_C4D_SHADOW_COLOR                 =  LIGHT_LISTER_C4D_END + 21
         OPTION_C4D_SHADOW_RESOLUTION            =  LIGHT_LISTER_C4D_END + 22
         OPTION_C4D_SHADOW_BIAS                  =  LIGHT_LISTER_C4D_END + 23
         OPTION_C4D_SHADOW_ACCURACY              =  LIGHT_LISTER_C4D_END + 24
         OPTION_C4D_SHADOW_MIN_SAMPLE            =  LIGHT_LISTER_C4D_END + 25
         OPTION_C4D_SHADOW_MAX_SAMPLE            =  LIGHT_LISTER_C4D_END + 26
         OPTION_C4D_LAYER                        =  LIGHT_LISTER_C4D_END + 27
         OPTION_C4D_END_GRP                      =  LIGHT_LISTER_C4D_END + 28