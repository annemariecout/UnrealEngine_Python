import unreal

AssetTools = unreal.AssetToolsHelpers.get_asset_tools()
MaterialEditLibrary = unreal.MaterialEditingLibrary
EditorAssetLibrary = unreal.EditorAssetLibrary

#Create new material
MeshPaintMaterial = AssetTools.create_asset("M_MeshPaint", "/Game/Materials", unreal.Material, unreal.MaterialFactoryNew())

#Add texture params for each surface
BaseColors = []
Normals = []
ORM = []

#Create vertex color nodes
NodePositionX = -500
NodePositionY = -300

VertexColorNode_Color = MaterialEditLibrary.create_material_expression(MeshPaintMaterial, unreal.MaterialExpressionVertexColor.static_class(), NodePositionX, NodePositionY * 10)
VertexColorNode_Color.set_editor_property('Desc', 'BaseColor')

VertexColorNode_Normal = MaterialEditLibrary.create_material_expression(MeshPaintMaterial, unreal.MaterialExpressionVertexColor.static_class(), NodePositionX, NodePositionY * 8)
VertexColorNode_Normal.set_editor_property('Desc', 'Normal')

VertexColorNode_R = MaterialEditLibrary.create_material_expression(MeshPaintMaterial, unreal.MaterialExpressionVertexColor.static_class(), NodePositionX, NodePositionY * 6)
VertexColorNode_R.set_editor_property('Desc', 'R_Occlusion')

VertexColorNode_G = MaterialEditLibrary.create_material_expression(MeshPaintMaterial, unreal.MaterialExpressionVertexColor.static_class(), NodePositionX, NodePositionY * 4)
VertexColorNode_G.set_editor_property('Desc', 'G_Roughness')

VertexColorNode_B = MaterialEditLibrary.create_material_expression(MeshPaintMaterial, unreal.MaterialExpressionVertexColor.static_class(), NodePositionX, NodePositionY * 2)
VertexColorNode_B.set_editor_property('Desc', 'B_Metallic')

#Create one minus nodes
OneMinusNodeColor = MaterialEditLibrary.create_material_expression(MeshPaintMaterial, unreal.MaterialExpressionOneMinus.static_class(), NodePositionX * 2, NodePositionY * 10)
OneMinusNodeNormal = MaterialEditLibrary.create_material_expression(MeshPaintMaterial, unreal.MaterialExpressionOneMinus.static_class(), NodePositionX * 2, NodePositionY * 8)
OneMinusNode_R = MaterialEditLibrary.create_material_expression(MeshPaintMaterial, unreal.MaterialExpressionOneMinus.static_class(), NodePositionX * 2, NodePositionY * 6)
OneMinusNode_G = MaterialEditLibrary.create_material_expression(MeshPaintMaterial, unreal.MaterialExpressionOneMinus.static_class(), NodePositionX * 2, NodePositionY * 4)
OneMinusNode_B = MaterialEditLibrary.create_material_expression(MeshPaintMaterial, unreal.MaterialExpressionOneMinus.static_class(), NodePositionX * 2, NodePositionY * 2)

#Create base color, normal and ORM texture params

for i in range(5):
    #Create texture params
    BaseColorParam = MaterialEditLibrary.create_material_expression(MeshPaintMaterial, unreal.MaterialExpressionTextureSampleParameter2D.static_class(), NodePositionX, NodePositionY + i * 150)
    NormalParam = MaterialEditLibrary.create_material_expression(MeshPaintMaterial, unreal.MaterialExpressionTextureSampleParameter2D.static_class(), NodePositionX, NodePositionY + i * 150)
    ORMParam = MaterialEditLibrary.create_material_expression(MeshPaintMaterial, unreal.MaterialExpressionTextureSampleParameter2D.static_class(), NodePositionX, NodePositionY + i * 150)

    #Set names and sampler types
    BaseColorParam.set_editor_property("ParameterName", unreal.Name("BaseColor_{}".format(i)))
    BaseColorParam.set_editor_property('SamplerSource', unreal.SamplerSourceMode.SSM_WRAP_WORLD_GROUP_SETTINGS)

    NormalParam.set_editor_property("ParameterName", unreal.Name("Normal_{}".format(i)))
    NormalParam.set_editor_property('SamplerSource', unreal.SamplerSourceMode.SSM_WRAP_WORLD_GROUP_SETTINGS)
    NormalParam.set_editor_property('SamplerType', unreal.MaterialSamplerType.SAMPLERTYPE_NORMAL)

    ORMParam.set_editor_property("ParameterName", unreal.Name("ORM_{}".format(i)))
    ORMParam.set_editor_property('SamplerSource', unreal.SamplerSourceMode.SSM_WRAP_WORLD_GROUP_SETTINGS)
    ORMParam.set_editor_property('SamplerType', unreal.MaterialSamplerType.SAMPLERTYPE_LINEAR_COLOR)

    #Append parameters to their arrays
    BaseColors.append(BaseColorParam)
    Normals.append(NormalParam)
    ORM.append(ORMParam)

#Define lerp arrays
BaseColorLerps = []
NormalLerps = []
ORM_R_Lerps = []
ORM_G_Lerps = []
ORM_B_Lerps = []

for i in range(5):
    BaseColorLerp = MaterialEditLibrary.create_material_expression(MeshPaintMaterial, unreal.MaterialExpressionLinearInterpolate.static_class(), NodePositionX, NodePositionY + i * 200)
    NormalLerp = MaterialEditLibrary.create_material_expression(MeshPaintMaterial, unreal.MaterialExpressionLinearInterpolate.static_class(), NodePositionX, NodePositionY + i * 200)
    ORM_R_Lerp = MaterialEditLibrary.create_material_expression(MeshPaintMaterial, unreal.MaterialExpressionLinearInterpolate.static_class(), NodePositionX, NodePositionY + i * 200)
    ORM_G_Lerp = MaterialEditLibrary.create_material_expression(MeshPaintMaterial, unreal.MaterialExpressionLinearInterpolate.static_class(), NodePositionX, NodePositionY + i * 200)
    ORM_B_Lerp = MaterialEditLibrary.create_material_expression(MeshPaintMaterial, unreal.MaterialExpressionLinearInterpolate.static_class(), NodePositionX, NodePositionY + i * 200)

    BaseColorLerps.append(BaseColorLerp)
    NormalLerps.append(NormalLerp)
    ORM_R_Lerps.append(ORM_R_Lerp)
    ORM_G_Lerps.append(ORM_G_Lerp)
    ORM_B_Lerps.append(ORM_B_Lerp)


#Base color connections

#Connect base color params to lerps
MaterialEditLibrary.connect_material_expressions(BaseColors[0], '', BaseColorLerps[0], 'B')
MaterialEditLibrary.connect_material_expressions(BaseColors[1], '', BaseColorLerps[1], 'B')
MaterialEditLibrary.connect_material_expressions(BaseColors[2], '', BaseColorLerps[2], 'B')
MaterialEditLibrary.connect_material_expressions(BaseColors[3], '', BaseColorLerps[3], 'B')
MaterialEditLibrary.connect_material_expressions(BaseColors[4], '', BaseColorLerps[4], 'B')
MaterialEditLibrary.connect_material_expressions(BaseColors[4], '', BaseColorLerps[0], 'A')
MaterialEditLibrary.connect_material_expressions(OneMinusNodeColor, '', BaseColorLerps[0], 'Alpha')

#Connect vertex color node to base color lerps
MaterialEditLibrary.connect_material_expressions(VertexColorNode_Color, 'A', OneMinusNodeColor, '')
MaterialEditLibrary.connect_material_expressions(VertexColorNode_Color, 'R', BaseColorLerps[1], 'Alpha')
MaterialEditLibrary.connect_material_expressions(VertexColorNode_Color, 'G', BaseColorLerps[2], 'Alpha')
MaterialEditLibrary.connect_material_expressions(VertexColorNode_Color, 'B', BaseColorLerps[3], 'Alpha')
MaterialEditLibrary.connect_material_expressions(VertexColorNode_Color, 'A', BaseColorLerps[4], 'Alpha')

#Make lerp connections
MaterialEditLibrary.connect_material_expressions(BaseColorLerps[0], '', BaseColorLerps[1], 'A')
MaterialEditLibrary.connect_material_expressions(BaseColorLerps[1], '', BaseColorLerps[2], 'A')
MaterialEditLibrary.connect_material_expressions(BaseColorLerps[2], '', BaseColorLerps[3], 'A')
MaterialEditLibrary.connect_material_expressions(BaseColorLerps[3], '', BaseColorLerps[4], 'A')

#Connect last lerp to base color
MaterialEditLibrary.connect_material_property(BaseColorLerps[4], '', unreal.MaterialProperty.MP_BASE_COLOR)



#Normal connections

#Connect normal params to lerps
MaterialEditLibrary.connect_material_expressions(Normals[0], '', NormalLerps[0], 'B')
MaterialEditLibrary.connect_material_expressions(Normals[1], '', NormalLerps[1], 'B')
MaterialEditLibrary.connect_material_expressions(Normals[2], '', NormalLerps[2], 'B')
MaterialEditLibrary.connect_material_expressions(Normals[3], '', NormalLerps[3], 'B')
MaterialEditLibrary.connect_material_expressions(Normals[4], '', NormalLerps[4], 'B')
MaterialEditLibrary.connect_material_expressions(Normals[4], '', NormalLerps[0], 'A')
MaterialEditLibrary.connect_material_expressions(OneMinusNodeNormal, '', NormalLerps[0], 'Alpha')

#Connect vertex color node to normal lerps
MaterialEditLibrary.connect_material_expressions(VertexColorNode_Normal, 'A', OneMinusNodeNormal, '')
MaterialEditLibrary.connect_material_expressions(VertexColorNode_Normal, 'R', NormalLerps[1], 'Alpha')
MaterialEditLibrary.connect_material_expressions(VertexColorNode_Normal, 'G', NormalLerps[2], 'Alpha')
MaterialEditLibrary.connect_material_expressions(VertexColorNode_Normal, 'B', NormalLerps[3], 'Alpha')
MaterialEditLibrary.connect_material_expressions(VertexColorNode_Normal, 'A', NormalLerps[4], 'Alpha')

#Make lerp connections
MaterialEditLibrary.connect_material_expressions(NormalLerps[0], '', NormalLerps[1], 'A')
MaterialEditLibrary.connect_material_expressions(NormalLerps[1], '', NormalLerps[2], 'A')
MaterialEditLibrary.connect_material_expressions(NormalLerps[2], '', NormalLerps[3], 'A')
MaterialEditLibrary.connect_material_expressions(NormalLerps[3], '', NormalLerps[4], 'A')

#Connect last lerp to normal
MaterialEditLibrary.connect_material_property(NormalLerps[4], '', unreal.MaterialProperty.MP_NORMAL)



#Ambient occlusion connections

#Connect ORM red channel to lerps
MaterialEditLibrary.connect_material_expressions(ORM[0], 'R', ORM_R_Lerps[0], 'B')
MaterialEditLibrary.connect_material_expressions(ORM[1], 'R', ORM_R_Lerps[1], 'B')
MaterialEditLibrary.connect_material_expressions(ORM[2], 'R', ORM_R_Lerps[2], 'B')
MaterialEditLibrary.connect_material_expressions(ORM[3], 'R', ORM_R_Lerps[3], 'B')
MaterialEditLibrary.connect_material_expressions(ORM[4], 'R', ORM_R_Lerps[4], 'B')
MaterialEditLibrary.connect_material_expressions(ORM[4], 'R', ORM_R_Lerps[0], 'A')
MaterialEditLibrary.connect_material_expressions(OneMinusNode_R, '', ORM_R_Lerps[0], 'Alpha')

#Connect vertex color node to ORM_R lerps
MaterialEditLibrary.connect_material_expressions(VertexColorNode_R, 'A', OneMinusNode_R, '')
MaterialEditLibrary.connect_material_expressions(VertexColorNode_R, 'R', ORM_R_Lerps[1], 'Alpha')
MaterialEditLibrary.connect_material_expressions(VertexColorNode_R, 'G', ORM_R_Lerps[2], 'Alpha')
MaterialEditLibrary.connect_material_expressions(VertexColorNode_R, 'B', ORM_R_Lerps[3], 'Alpha')
MaterialEditLibrary.connect_material_expressions(VertexColorNode_R, 'A', ORM_R_Lerps[4], 'Alpha')

#Make lerp connections
MaterialEditLibrary.connect_material_expressions(ORM_R_Lerps[0], '', ORM_R_Lerps[1], 'A')
MaterialEditLibrary.connect_material_expressions(ORM_R_Lerps[1], '', ORM_R_Lerps[2], 'A')
MaterialEditLibrary.connect_material_expressions(ORM_R_Lerps[2], '', ORM_R_Lerps[3], 'A')
MaterialEditLibrary.connect_material_expressions(ORM_R_Lerps[3], '', ORM_R_Lerps[4], 'A')

#Connect last lerp to ambient occlusion
MaterialEditLibrary.connect_material_property(ORM_R_Lerps[4], '', unreal.MaterialProperty.MP_AMBIENT_OCCLUSION)



#Roughness connections

#Connect ORM green channel to lerps
MaterialEditLibrary.connect_material_expressions(ORM[0], 'G', ORM_G_Lerps[0], 'B')
MaterialEditLibrary.connect_material_expressions(ORM[1], 'G', ORM_G_Lerps[1], 'B')
MaterialEditLibrary.connect_material_expressions(ORM[2], 'G', ORM_G_Lerps[2], 'B')
MaterialEditLibrary.connect_material_expressions(ORM[3], 'G', ORM_G_Lerps[3], 'B')
MaterialEditLibrary.connect_material_expressions(ORM[4], 'G', ORM_G_Lerps[4], 'B')
MaterialEditLibrary.connect_material_expressions(ORM[4], 'G', ORM_G_Lerps[0], 'A')
MaterialEditLibrary.connect_material_expressions(OneMinusNode_G, '', ORM_G_Lerps[0], 'Alpha')

#Connect vertex color node to ORM_G lerps
MaterialEditLibrary.connect_material_expressions(VertexColorNode_G, 'A', OneMinusNode_G, '')
MaterialEditLibrary.connect_material_expressions(VertexColorNode_G, 'R', ORM_G_Lerps[1], 'Alpha')
MaterialEditLibrary.connect_material_expressions(VertexColorNode_G, 'G', ORM_G_Lerps[2], 'Alpha')
MaterialEditLibrary.connect_material_expressions(VertexColorNode_G, 'B', ORM_G_Lerps[3], 'Alpha')
MaterialEditLibrary.connect_material_expressions(VertexColorNode_G, 'A', ORM_G_Lerps[4], 'Alpha')

#Make lerp connections
MaterialEditLibrary.connect_material_expressions(ORM_G_Lerps[0], '', ORM_G_Lerps[1], 'A')
MaterialEditLibrary.connect_material_expressions(ORM_G_Lerps[1], '', ORM_G_Lerps[2], 'A')
MaterialEditLibrary.connect_material_expressions(ORM_G_Lerps[2], '', ORM_G_Lerps[3], 'A')
MaterialEditLibrary.connect_material_expressions(ORM_G_Lerps[3], '', ORM_G_Lerps[4], 'A')

#Connect last lerp to roughness
MaterialEditLibrary.connect_material_property(ORM_G_Lerps[4], '', unreal.MaterialProperty.MP_ROUGHNESS)



#Metallic connections

#Connect ORM blue channel to lerps
MaterialEditLibrary.connect_material_expressions(ORM[0], 'B', ORM_B_Lerps[0], 'B')
MaterialEditLibrary.connect_material_expressions(ORM[1], 'B', ORM_B_Lerps[1], 'B')
MaterialEditLibrary.connect_material_expressions(ORM[2], 'B', ORM_B_Lerps[2], 'B')
MaterialEditLibrary.connect_material_expressions(ORM[3], 'B', ORM_B_Lerps[3], 'B')
MaterialEditLibrary.connect_material_expressions(ORM[4], 'B', ORM_B_Lerps[4], 'B')
MaterialEditLibrary.connect_material_expressions(ORM[4], 'B', ORM_B_Lerps[0], 'A')
MaterialEditLibrary.connect_material_expressions(OneMinusNode_B, '', ORM_B_Lerps[0], 'Alpha')

#Connect vertex color node to ORM_B lerps
MaterialEditLibrary.connect_material_expressions(VertexColorNode_B, 'A', OneMinusNode_B, '')
MaterialEditLibrary.connect_material_expressions(VertexColorNode_B, 'R', ORM_B_Lerps[1], 'Alpha')
MaterialEditLibrary.connect_material_expressions(VertexColorNode_B, 'G', ORM_B_Lerps[2], 'Alpha')
MaterialEditLibrary.connect_material_expressions(VertexColorNode_B, 'B', ORM_B_Lerps[3], 'Alpha')
MaterialEditLibrary.connect_material_expressions(VertexColorNode_B, 'A', ORM_B_Lerps[4], 'Alpha')

#Make lerp connections
MaterialEditLibrary.connect_material_expressions(ORM_B_Lerps[0], '', ORM_B_Lerps[1], 'A')
MaterialEditLibrary.connect_material_expressions(ORM_B_Lerps[1], '', ORM_B_Lerps[2], 'A')
MaterialEditLibrary.connect_material_expressions(ORM_B_Lerps[2], '', ORM_B_Lerps[3], 'A')
MaterialEditLibrary.connect_material_expressions(ORM_B_Lerps[3], '', ORM_B_Lerps[4], 'A')

#Connect last lerp to metallic
MaterialEditLibrary.connect_material_property(ORM_B_Lerps[4], '', unreal.MaterialProperty.MP_METALLIC)


#Create material instance
MeshPaintInstance = AssetTools.create_asset("MI_MeshPaint", "/Game/Materials", unreal.MaterialInstanceConstant, unreal.MaterialInstanceConstantFactoryNew())
MaterialEditLibrary.set_material_instance_parent(MeshPaintInstance, MeshPaintMaterial)
MeshPaintInstance.set_editor_property("Parent", MeshPaintMaterial)
MaterialEditLibrary.update_material_instance(MeshPaintInstance)

#Save material and instance
EditorAssetLibrary.save_asset("/Game/Materials/M_MeshPaint", True)
EditorAssetLibrary.save_asset("/Game/Materials/MI_MeshPaint", True)
