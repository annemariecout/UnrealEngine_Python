import unreal

#define actor location
actorLocation = unreal.Vector(0, 0, 0)
actorRotation = unreal.Rotator(0, 0, 0)
levelSubSys = unreal.get_editor_subsystem(unreal.LevelEditorSubsystem)

#create new atmospheric actors
dirLight = unreal.EditorLevelLibrary.spawn_actor_from_class(unreal.DirectionalLight, actorLocation, actorRotation, False)
skyLight = unreal.EditorLevelLibrary.spawn_actor_from_class(unreal.SkyLight, actorLocation, actorRotation, False)
skyAtm = unreal.EditorLevelLibrary.spawn_actor_from_class(unreal.SkyAtmosphere, actorLocation, actorRotation, False)
fog = unreal.EditorLevelLibrary.spawn_actor_from_class(unreal.ExponentialHeightFog, actorLocation, actorRotation, False)
clouds = unreal.EditorLevelLibrary.spawn_actor_from_class(unreal.VolumetricCloud, actorLocation, actorRotation, False)

#save level with atmospheric actors
levelSubSys.save_current_level()

