# coding: utf8
import c4d
import operator

from Const import Const

const = Const()

class LightManager(object):

    def get_bc_from_tag(self, light):
        tag = light.GetTag(const.PLUGIN_ID_TAG)
        if not tag:
            return False

        bc_tag = tag.GetData().GetContainer(const.PLUGIN_ID_TAG)
        if not bc_tag:
            return False

        if not bc_tag[0]:
            return False

        return bc_tag[1]

    def set_bc_tag(self, light, new_id):
        buffer_tag = light.GetTag(const.PLUGIN_ID_TAG)
        if not buffer_tag:
            buffer_tag = c4d.BaseTag(const.PLUGIN_ID_TAG)
            light.InsertTag(buffer_tag)

        bc_tag = buffer_tag.GetDataInstance().GetContainerInstance(const.PLUGIN_ID_TAG)
        bc_tag[0] = True
        bc_tag[1] = new_id

        c4d.EventAdd()

    def get_c4d_light(self):
        list_light = self.get_all_light()
        buffer_c4d_light = list()
        new_c4d_light = list()

        #pour chaque light
        for light in list_light:
            #on recup les tags
            tags = light.GetTags()
            have_tag = False
            for tag in tags:
                if tag.CheckType(const.TAG_ID_OCTANE) or tag.CheckType(const.TAG_ID_VRAY) or tag.CheckType(const.TAG_ID_ARNOLD):
                    have_tag = True
                    break

            if have_tag:
                continue

            if light.GetType() != const.LIGHT_C4D_ID:
                continue

            buffer = dict()
            buffer["light"] = light

            old_id = self.get_bc_from_tag(light)
            if old_id is False:
                buffer["id"] = 0
                new_c4d_light.append(buffer)
            else:
                buffer["id"] = old_id
                buffer_c4d_light.append(buffer)

        for i, light in enumerate(new_c4d_light):
            light["id"] = len(buffer_c4d_light) + i + 1

        buffer_c4d_light += new_c4d_light
        buffer_c4d_light.sort(key=operator.itemgetter('id'))

        for i, light in enumerate(buffer_c4d_light):
            light["id"] = i
            self.set_bc_tag(light["light"], i)

        return buffer_c4d_light

    def get_all_light(self):
        doc = c4d.documents.GetActiveDocument()
        all_lights = self.search_light_in_hierarchy(doc.GetFirstObject())

        return all_lights

    def search_light_in_hierarchy(self, op, light_type=c4d.Olight, buffer_all_lights=None):
        if buffer_all_lights is None:
            buffer_all_lights = list()

        while op:
            if op.CheckType(light_type):
                buffer_all_lights.append(op)
            self.search_light_in_hierarchy(op.GetDown(), light_type,  buffer_all_lights)
            op = op.GetNext()
        return buffer_all_lights

    def get_all_layers(self, layer=None, buffer_all_layers=[], first=True):
        if first:
            buffer_all_layers = list()
            doc = c4d.documents.GetActiveDocument()
            layer = doc.GetLayerObjectRoot().GetDown()

        while layer:
            buffer_all_layers.append(layer)
            self.get_all_layers(layer.GetDown(), buffer_all_layers, first=False)
            layer = layer.GetNext()

        return buffer_all_layers