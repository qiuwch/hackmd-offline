# TODO: How to paint vertex and find coorespondence between views

[Prereq: make vertex uniform](https://blenderartists.org/forum/showthread.php?152289-Uniform-vertex-spacing). This is [another discussion](http://blender.stackexchange.com/questions/14860/how-can-i-obtain-an-even-vertex-density-base-mesh). Search term `blender uniform vertex`.

The [remesh modifier](https://www.blender.org/manual/modeling/modifiers/generate/remesh.html) is documented here. Use `block` mode to produce uniform grid. To do it in batch mode, need to [apply modifier in python](http://blender.stackexchange.com/questions/15584/applying-modifiers-in-a-script). Remember to apply modifier. 

![](https://i.imgur.com/A4ioSWW.png)

A rough setting can be, `octree depth = 7`, `scale = 0.9`, `mode = smooth`.

Another idea is [reducing the number of vertexs](http://blender.stackexchange.com/questions/31467/how-to-reduce-vertex-count-on-a-mesh)

There is [where the code from](http://blender.stackexchange.com/questions/8560/apply-vertex-paint-to-a-vertex)
```python
import bpy

def color_obj(obj, color):
    mesh = obj.data 
    scn = bpy.context.scene
    #check if our mesh already has Vertex Colors, and if not add some... (first we need to make sure it's the active object)
    scn.objects.active = obj
    obj.select = True
    if mesh.vertex_colors:
        vcol_layer = mesh.vertex_colors.active
    else:
        vcol_layer = mesh.vertex_colors.new()
    for poly in mesh.polygons:
        for loop_index in poly.loop_indices:
            loop_vert_index = mesh.loops[loop_index].vertex_index
            vcol_layer.data[loop_index].color = color


def random_color(obj):
    import random
    r = random.random
    mesh = obj.data 
    scn = bpy.context.scene
    #check if our mesh already has Vertex Colors, and if not add some... (first we need to make sure it's the active object)
    scn.objects.active = obj
    obj.select = True
    if mesh.vertex_colors:
        vcol_layer = mesh.vertex_colors.active
    else:
        vcol_layer = mesh.vertex_colors.new()
    for poly in mesh.polygons:
        for loop_index in poly.loop_indices:
            loop_vert_index = mesh.loops[loop_index].vertex_index
            random_color = [r(), r(), r()]
            vcol_layer.data[loop_index].color = random_color
            

def color_vertex(obj, vert, color):
    """Paints a single vertex where vert is the index of the vertex
    and color is a tuple with the RGB values."""
    mesh = obj.data 
    scn = bpy.context.scene
    #check if our mesh already has Vertex Colors, and if not add some... (first we need to make sure it's the active object)
    scn.objects.active = obj
    obj.select = True
    if mesh.vertex_colors:
        vcol_layer = mesh.vertex_colors.active
    else:
        vcol_layer = mesh.vertex_colors.new()
    for poly in mesh.polygons:
        for loop_index in poly.loop_indices:
            loop_vert_index = mesh.loops[loop_index].vertex_index
            if vert == loop_vert_index:
                vcol_layer.data[loop_index].color = color

#example usage
def paint():
    color = (1.0, 0.0, 1.0)  # pink
    color_vertex(bpy.context.scene.objects['Cube'], 1, color)
```

Switch to paint mode can be done with [this](https://github.com/qiuwch/tenon/blob/master/tenon/render.py)

![](https://i.imgur.com/9sDdpzc.png)

## The rendering procedure

1. Import models

import object and scale it 10x larger.

2. Change camera postions and render original images

``` python
bpy.data.scenes['Scene'].render.filepath = 'D:/original.png' 
bpy.ops.render.render( write_still=True )
```

![](https://i.imgur.com/GD34llH.png)
This is a buggy model, so the rendering is weird.

3. Iterate through objects and apply remesh modifer

``` python
# modified from http://blender.stackexchange.com/questions/15584/applying-modifiers-in-a-script
def applyRemesh (target):
    # remesh = target.modifiers.new('RemeshToBlocks', 'BOOLEAN')
    scn = bpy.context.scene
    scn.objects.active = target
    # No empty line
    bpy.ops.object.modifier_add(type='REMESH')
    remesh = target.modifiers['Remesh'] # This is the default name, might cause problem if Remesh already exist
    remesh.octree_depth = 7
    remesh.mode = 'BLOCKS'
    bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Remesh")
    
test_obj_name = 'mesh15.002_mesh15-geometry'
test_obj = bpy.context.scene.objects[test_obj_name]
applyRemesh(test_obj)
```

Iterate over all objects in the scene, this loop will take a while
``` python
scn = bpy.context.scene
for obj in scn.objects:
    # do something, do I need to check the object type? 
    # What will happen if I apply modifer to a camera? error happened
    # print(obj)
    if obj.type == 'MESH':
        applyRemesh(obj)
```

4. Apply `vertex paint` to meshes
``` python
# code modified from: http://blender.stackexchange.com/questions/8560/apply-vertex-paint-to-a-vertex
# Do a random paint first
def randomPaint(obj):
    import random
    r = random.random
    mesh = obj.data 
    scn = bpy.context.scene
    #check if our mesh already has Vertex Colors, and if not add some... (first we need to make sure it's the active object)
    scn.objects.active = obj
    obj.select = True
    if mesh.vertex_colors:
        vcol_layer = mesh.vertex_colors.active
    else:
        vcol_layer = mesh.vertex_colors.new()
    for poly in mesh.polygons:
        for loop_index in poly.loop_indices:
            loop_vert_index = mesh.loops[loop_index].vertex_index
            random_color = [r(), r(), r()]
            vcol_layer.data[loop_index].color = random_color
```

Iterate over all objects and apply vertex paint
``` python
scn = bpy.context.scene
for obj in scn.objects:
    if obj.type == 'MESH':
        randomPaint(obj)
```

5. Switch render mode to `vertex paint` and render vertex images
  
This code can [switch to paint mode](https://github.com/qiuwch/tenon/blob/master/tenon/render.py)

```python
def setObjectPaintMode(obj):
    def setMaterialPaintMode(material):
        if material:
            material.use_shadeless = True
            material.use_vertex_color_paint = True
            material.use_transparency = False
            for i in range(len(material.use_textures)):
                material.use_textures[i] = False
        else:
            print('Material not available')
    #----
    if obj:
        if len(obj.material_slots.items()) == 0:
            print('No material is defined for object: %s' % obj.name)
        for slot in obj.material_slots:
            setMaterialPaintMode(slot.material)
    else:
        print('Enable paint mode: Object not exist')
```

Revert the vertex paint material operation
```python
def unsetMaterialPaintMode(material):
    if material:
        material.use_shadeless = False
        material.use_vertex_color_paint = False

        material.use_transparency = True
        for i in range(len(material.use_textures)):
            material.use_textures[i] = True
```


Iterate over all objects and set paint mode
``` python
scn = bpy.context.scene
for obj in scn.objects:
    if obj.type == 'MESH':
        setObjectPaintMode(obj)
```

Render to image
```python
bpy.data.scenes['Scene'].render.filepath = 'D:/vertex.png' 
bpy.ops.render.render( write_still=True )
```
![](https://i.imgur.com/hJhNlqH.png)
