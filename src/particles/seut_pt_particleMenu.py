import bpy

from bpy.types  import Panel

class SEUT_PT_ParticleMenu(Panel):
    """Creates the Particle Properties menu"""
    bl_idname = "SEUT_PT_ParticleMenu"
    bl_label = "Space Engineers Utilities"
    bl_category = "SEUT"
    bl_space_type = 'PROPERTIES'
    bl_region_type = 'WINDOW'
    bl_context = 'object'

    @classmethod
    def poll(cls, context):
        return not bpy.context.active_object is None and bpy.context.active_object.type == 'MESH' and bpy.context.scene.seut.sceneType == 'particle_effect'


    def draw(self, context):
        layout = self.layout
        scene = context.scene
        holder = context.active_object

        layout.label(text="Particle Properties:")
        layout.prop(holder.seut, 'particle_id')
        layout.prop(holder.seut, 'particle_length')
        layout.prop(holder.seut, 'particle_preload')
        layout.prop(holder.seut, 'particle_lowres')
        layout.prop(holder.seut, 'particle_loop')
        layout.prop(holder.seut, 'particle_duration_min')
        layout.prop(holder.seut, 'particle_duration_max')
        layout.prop(holder.seut, 'particle_version')
        layout.prop(holder.seut, 'particle_distance_max')
