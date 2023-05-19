import unreal

AssetTools = unreal.AssetToolsHelpers.get_asset_tools()
MaterialEditLibrary = unreal.MaterialEditingLibrary
EditorAssetLibrary = unreal.EditorAssetLibrary

Materials = AssetTools.create_asset("M_Master_Stacked", "/Game/Materials", unreal.Material, unreal.MaterialFactoryNew())

#Create 2D Texture Param and Connect to Base Color
BaseColorTextureParam = MaterialEditLibrary.create_material_expression(Materials, unreal.MaterialExpressionTextureSampleParameter, -384, -200)
BaseColorTextureParam.set_editor_property("ParameterName", "BaseColor")
MaterialEditLibrary.connect_material_property(BaseColorTextureParam, "RGB", unreal.MaterialProperty.MP_BASE_COLOR)

#Create Constant Value and Connect to Specular
SpecularParam = MaterialEditLibrary.create_material_expression(Materials, unreal.MaterialExpressionConstant, -384, 100)
SpecularParam.set_editor_property("R", 0.3)
MaterialEditLibrary.connect_material_property(SpecularParam, "", unreal.MaterialProperty.MP_SPECULAR)

#Create 2D Texture Param and Connect to Normal
NormalTextureParam = MaterialEditLibrary.create_material_expression(Materials, unreal.MaterialExpressionTextureSampleParameter, -384, 200)
NormalTextureParam.set_editor_property("ParameterName", "Normal")
MaterialEditLibrary.connect_material_property(NormalTextureParam, "RGB", unreal.MaterialProperty.MP_NORMAL)

#Create 2D Texture Param and Connect to ORM
ORMTextureParam = MaterialEditLibrary.create_material_expression(Materials, unreal.MaterialExpressionTextureSampleParameter, -384, 500)
ORMTextureParam.set_editor_property("ParameterName", "ORM")
MaterialEditLibrary.connect_material_property(ORMTextureParam, "R", unreal.MaterialProperty.MP_AMBIENT_OCCLUSION)
MaterialEditLibrary.connect_material_property(ORMTextureParam, "G", unreal.MaterialProperty.MP_ROUGHNESS)
MaterialEditLibrary.connect_material_property(ORMTextureParam, "B", unreal.MaterialProperty.MP_METALLIC)

#Create Material Instance
MaterialInstanceStacked = AssetTools.create_asset("MI_Stacked", "/Game/Materials", unreal.MaterialInstanceConstant, unreal.MaterialInstanceConstantFactoryNew())
MaterialEditLibrary.set_material_instance_parent(MaterialInstanceStacked, Materials)
MaterialInstanceStacked.set_editor_property("Parent", Materials)
MaterialEditLibrary.update_material_instance(MaterialInstanceStacked)

#Save Materials and Instances
EditorAssetLibrary.save_asset("/Game/Materials/M_Master_Stacked", True)
EditorAssetLibrary.save_asset("/Game/Materials/MI_Stacked", True)

