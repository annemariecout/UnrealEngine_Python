import unreal

levelSubSys = unreal.get_editor_subsystem(unreal.LevelEditorSubsystem)

#init new level
newLevel = "myNewLevel"

#create new level
myNewLevel = levelSubSys.new_level("/Game/Levels/newLevel")

#set level as current level
levelSubSys.set_current_level_by_name(newLevel)

#save level
levelSubSys.save_current_level()
