
from flask import Blueprint, request
 
bg7_40323216 = Blueprint('bg7_40323216', __name__, url_prefix='/bg7_40323216', template_folder='templates')
 

@bg7_40323216.route('/hw_w16')
def hw_w16():
    outstring = '''
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>網際 2D 繪圖</title>
    <!-- IE 9: display inline SVG -->
    <meta http-equiv="X-UA-Compatible" content="IE=9">
<script type="text/javascript" src="http://brython.info/src/brython_dist.js"></script>
<script type="text/javascript" src="http://cptocadp-2015fallhw.rhcloud.com/static/Cango-8v03.js"></script>
<script type="text/javascript" src="http://cptocadp-2015fallhw.rhcloud.com/static/Cango2D-6v13.js"></script>
<script type="text/javascript" src="http://cptocadp-2015fallhw.rhcloud.com/static/CangoAxes-1v33.js"></script>
</head>
<body>
<script>
window.onload=function(){
brython(1);
}
</script>
<canvas id="plotarea" width="800" height="800"></canvas>
<script type="text/python">
from javascript import JSConstructor
from browser import window
import math
cango = JSConstructor(window.Cango)
cobj = JSConstructor(window.Cobj)
shapedefs = window.shapeDefs
obj2d = JSConstructor(window.Obj2D)
cgo = cango("plotarea")
cgo.setWorldCoords(-250, -250, 500, 500) 

        
#cgo.drawText("使用 Cango 繪圖程式庫!", 0, 0, {"fontSize":60, "fontWeight": 1200, "lorg":5 })
deg = math.pi/180  
def O(x, y, rx, ry, rot, color, border, linewidth):
    # 旋轉必須要針對相對中心 rot not working yet
    chamber = "M10.728 19.400 A7.500,7.500 0 0,0 6.568,26.403 A7.500,7.500 0 0,0 11.247,33.070 A24.908,24.908 0 0,0 10.839,42.493 A7.500,7.500 0 0,0 5.602,48.731 A7.500,7.500 0 0,0 9.141,56.066 A7.500,7.500 0 0,0 17.283,55.849 A24.908,24.908 0 0,0 28.063,62.617 A7.500,7.500 0 0,0 31.405,70.045 A7.500,7.500 0 0,0 39.550,70.045 A7.500,7.500 0 0,0 42.892,62.617 A24.908,24.908 0 0,0 55.466,53.700 A7.500,7.500 0 0,0 63.580,53.002 A7.500,7.500 0 0,0 66.274,45.316 A7.500,7.500 0 0,0 60.370,39.705 A24.908,24.908 0 0,0 59.852,33.712 A7.500,7.500 0 0,0 64.705,27.171 A7.500,7.500 0 0,0 60.732,20.061 A7.500,7.500 0 0,0 52.618,20.767 A24.908,24.908 0 0,0 42.892,15.060 A7.500,7.500 0 0,0 39.550,7.633 A7.500,7.500 0 0,0 31.405,7.633 A7.500,7.500 0 0,0 28.063,15.060 A24.908,24.908 0 0,0 18.820,20.320 A7.500,7.500 0 0,0 10.728,19.400"
    cgoChamber = window.svgToCgoSVG(chamber)
    cmbr = cobj(cgoChamber, "SHAPE", {
            "fillColor": color,
            "border": border,
            "strokeColor": "tan",
            "lineWidth": linewidth })
            
            
            
    cmbr.translate(0, 20)    
            
 
   
    
    
    # hole 為原點位置
    #hole = cobj(shapedefs.circle(4), "PATH") 
    #cmbr.appendPath(hole) 

  
    # 放大 1 倍
    cgo.render(cmbr, x, y, 3, rot)
    
O(0, 0, 0, 0, 0, "red", True, 4)
</script>


'''
    return outstring
