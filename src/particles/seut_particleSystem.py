import bpy

from bpy.types  import PropertyGroup
from bpy.props  import (EnumProperty,
                        FloatProperty,
                        FloatVectorProperty,
                        IntProperty,
                        StringProperty,
                        BoolProperty,
                        PointerProperty,
                        CollectionProperty
                        )


class SEUT_ParticlePropertyKeys(PropertyGroup):
    """Holder for the various Particle Generation Property Keys"""

    time: FloatProperty(
        name="Time"
    )
    value_bool: BoolProperty(
        name="ValueBool"
    )
    value_int: IntProperty(
        name="ValueInt"
    )
    value_float: FloatProperty(
        name="ValueFloat"
    )
    value_vector_3: FloatVectorProperty(
        name="ValueVector3",
        description="TBD",
        subtype='XYZ'
    )
    value_vector_4: FloatVectorProperty(
        name="ValueVector4",
        description="TBD",
        subtype='COLOR_GAMMA'
    )


class SEUT_ParticlePropertyValue2D(PropertyGroup):
    """Holder for the various Particle Generation Property Keys"""

    time: FloatProperty(
        name="Time"
    )
    value_bool: BoolProperty(
        name="ValueBool"
    )
    value_int: IntProperty(
        name="ValueInt"
    )
    value_float: FloatProperty(
        name="ValueFloat"
    )
    value_vector_3: FloatVectorProperty(
        name="ValueVector3",
        description="TBD",
        subtype='XYZ'
    )
    value_vector_4: FloatVectorProperty(
        name="ValueVector4",
        description="TBD",
        subtype='COLOR_GAMMA'
    )
    value_2d: CollectionProperty(
        type=SEUT_ParticlePropertyKeys
    )


class SEUT_ParticleProperty(PropertyGroup):
    """Holder for the various Particle Generation properties"""

    name: StringProperty(
        name="Name of Property"
    )
    prop_animation_type: EnumProperty(
        name="AnimationType",
        description="TBD",
        items=(
            ('Const', 'Constant', 'TBD'),
            ('Animated', 'Animated', 'TBD'),
            ('Animated2D', 'Animated2D', 'TBD')
            ),
        default='Const'
    )
    prop_type: EnumProperty(
        name="Type",
        description="TBD",
        items=(
            ('Bool', 'Bool', 'TBD'),
            ('Int', 'Int', 'TBD'),
            ('Float', 'Float', 'TBD'),
            ('Vector3', 'Vector3', 'TBD'),
            ('Vector4', 'Vector4', 'TBD')
            ),
        default='Bool'
    )

    value_bool: BoolProperty(
        name="ValueBool"
    )
    value_int: IntProperty(
        name="ValueInt"
    )
    value_float: FloatProperty(
        name="ValueFloat"
    )
    value_vector_3: FloatVectorProperty(
        name="ValueVector3",
        description="TBD",
        subtype='XYZ'
    )
    value_vector_4: FloatVectorProperty(
        name="ValueVector4",
        description="TBD",
        subtype='COLOR_GAMMA'
    )

    keys: CollectionProperty(
        type=SEUT_ParticlePropertyValue2D
    )


class SEUT_ParticleSystem(PropertyGroup):
    """Holder for the various particle generation properties"""
    
    properties: CollectionProperty(
        type=SEUT_ParticleProperty
    )