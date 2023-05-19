import unreal

AssetTools = unreal.AssetToolsHelpers.get_asset_tools()
MaterialEditLibrary = unreal.MaterialEditingLibrary
EditorAssetLibrary = unreal.EditorAssetLibrary

Materials = AssetTools.create_asset("M_Master", "/Game/Materials", unreal.Material, unreal.MaterialFactoryNew())

#Create 2D Texture Param and Connect to Base Color
BaseColorTextureParam = MaterialEditLibrary.create_material_expression(Materials, unreal.MaterialExpressionTextureSampleParameter, -384, -300)
BaseColorTextureParam.set_editor_property("ParameterName", "BaseColor")
MaterialEditLibrary.connect_material_property(BaseColorTextureParam, "RGB", unreal.MaterialProperty.MP_BASE_COLOR)

#Create 2D Texture Param and Connect to Roughness
RoughnessTextureParam = MaterialEditLibrary.create_material_expression(Materials, unreal.MaterialExpressionTextureSampleParameter, -384, 400)
RoughnessTextureParam.set_editor_property("ParameterName", "Roughness")
MaterialEditLibrary.connect_material_property(RoughnessTextureParam, "RGB", unreal.MaterialProperty.MP_ROUGHNESS)

#Create Constant Value and Connect to Specular
SpecularParam = MaterialEditLibrary.create_material_expression(Materials, unreal.MaterialExpressionConstant, -384, 300)
SpecularParam.set_editor_property("R", 0.3)
MaterialEditLibrary.connect_material_property(SpecularParam, "", unreal.MaterialProperty.MP_SPECULAR)

#Create 2D Texture Param and Connect to Normal
NormalTextureParam = MaterialEditLibrary.create_material_expression(Materials, unreal.MaterialExpressionTextureSampleParameter, -384, 700)
NormalTextureParam.set_editor_property("ParameterName", "Normal")
NormalTextureParam.set_editor_property("SamplerType", "Normal")
MaterialEditLibrary.connect_material_property(NormalTextureParam, "RGB", unreal.MaterialProperty.MP_NORMAL)

#Create 2D Texture Param and Connect to Metallic
MetallicTextureParam = MaterialEditLibrary.create_material_expression(Materials, unreal.MaterialExpressionTextureSampleParameter, -384, 0)
MetallicTextureParam.set_editor_property("ParameterName", "Metallic")
MaterialEditLibrary.connect_material_property(MetallicTextureParam, "RGB", unreal.MaterialProperty.MP_METALLIC)

#Create 2D Texture Param and Connect to AO
AOTextureParam = MaterialEditLibrary.create_material_expression(Materials, unreal.MaterialExpressionTextureSampleParameter, -384, 1000)
AOTextureParam.set_editor_property("ParameterName", "AO")
MaterialEditLibrary.connect_material_property(AOTextureParam, "RGB", unreal.MaterialProperty.MP_AMBIENT_OCCLUSION)

EditorAssetLibrary.save_asset("/Game/Materials/M_Master", True)
