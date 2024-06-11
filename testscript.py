import bpy


PARENT_CATEGORY = "GazeboSim"
# Panels
class ComponentInspector(bpy.types.Panel):
    '''This panel can inspect and edit components of the selected object. Similar to Gazebo Sim's "Component Inspector Editor".'''
    bl_label = "Component Inspector"
    bl_idname = "PT_ComponentInstpector"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = PARENT_CATEGORY
    
    
    def draw(self, context):
        layout = self.layout

        row = layout.row()
        row.label(text="Somefin", icon="COLLECTION_COLOR_03")

class EntityTree(bpy.types.Panel):
    '''This panel stores all the entity hierarchy data. Similar to Gazebo Sim's "Entity Tree".'''
    bl_label = "Entity Tree"
    bl_idname = "PT_EntityTree"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = PARENT_CATEGORY
    bl_options = {'DEFAULT_CLOSED'}
    
    def draw(self, context):
        layout = self.layout

        row = layout.row()
        row.label(text="Dis contains", icon="COLLECTION_COLOR_04")

  
        
        
def register():
    bpy.utils.register_class(ComponentInspector)
    bpy.utils.register_class(EntityTree)
def unregister():
    bpy.utils.unregister_class(ComponentInspector) 
    bpy.utils.unregister_class(EntityTree) 
    
    
if __name__ == '__main__':
    register()