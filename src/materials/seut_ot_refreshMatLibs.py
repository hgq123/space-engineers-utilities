import bpy
import os
import re

from bpy.types  import Operator

from ..seut_errors  import report_error

class SEUT_OT_RefreshMatLibs(Operator):
    """Refresh available MatLibs"""
    bl_idname = "scene.refresh_matlibs"
    bl_label = "Refresh MatLibs"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):

        SEUT_OT_RefreshMatLibs.refreshMatLibs(self, context)

        return {'FINISHED'}
    
    def refreshMatLibs(self, context):
        """Refresh available MatLibs"""

        wm = context.window_manager

        addon = __package__[:__package__.find(".")]
        preferences = bpy.context.preferences.addons.get(addon).preferences
        materialsPath = os.path.abspath(bpy.path.abspath(preferences.materialsPath))

        if preferences.materialsPath == "" or preferences.materialsPath == "." or os.path.isdir(materialsPath) == False:
            report_error(self, context, True, 'E012', "Materials Folder", materialsPath)
            return {'CANCELLED'}

        # Find all MatLibs in directory, save to set, then add to matlibs list
        path = bpy.path.abspath(preferences.materialsPath)
        newSet = set()

        for file in os.listdir(path):
            if file is not None and file.endswith(".blend") and file.find("MatLib_") != -1:
                newSet.add(file)

        # Add everything in the directory that is not already in the set to the set
        for libNew in newSet:
            if libNew in wm.seut.matlibs:
                continue
            else:
                item = wm.seut.matlibs.add()
                item.name = libNew

        # If the set has entries that don't exist in the directory, remove them
        for libOld in wm.seut.matlibs:
            if libOld.name in newSet:
                for mat in bpy.data.materials:
                    if mat.library is not None and mat.library.name == libOld.name:
                        wm.seut.matlibs[wm.seut.matlibs.find(libOld.name)].enabled = True
                        break
                continue
            else:
                for idx in range(0, len(wm.seut.matlibs)):
                    if wm.seut.matlibs[idx].name == libOld.name:
                        wm.seut.matlibs.remove(idx)
        
        # Finally, attempt to re-link any MatLibs with broken paths
        try:
            currentArea = context.area.type
            context.area.type = 'OUTLINER'
        except AttributeError:
            try:
                context.area.type = 'OUTLINER'
                currentArea = context.area.type
            # If it fails here it generally means that this is on startup before context.area is even set.
            except AttributeError:
                pass

        for lib in bpy.data.libraries:
            if os.path.exists(lib.filepath) == False:
                
                if re.search("\.[0-9]{3}", lib.name[-4:]) != None:
                    lib.name = lib.name[:-4]

                try:
                    bpy.ops.wm.lib_relocate(
                        library=lib.name,
                        directory=path,
                        filename=lib.name
                    )
                except:
                    print("SEUT Warning: Library '" + lib.name + "' could not be relocated in '" + path + "'.")

        try:
            context.area.type = currentArea
        except UnboundLocalError:
            pass

        return {'FINISHED'}