import cadquery as cq
from typing import NamedTuple

# class AxisRange(NamedTuple):
#     min: float
#     max: float

# class Center(NamedTuple):
#     x: float
#     y: float
#     z: float

# class ObjPos(NamedTuple):
#     x: AxisRange
#     y: AxisRange
#     z: AxisRange
#     center: Center

# def get_obj_pos(obj) -> ObjPos:
#     bb = obj.val().BoundingBox()
#     cx = (bb.xmin + bb.xmax) / 2
#     cy = (bb.ymin + bb.ymax) / 2
#     cz = (bb.zmin + bb.zmax) / 2
#     return ObjPos(
#         x=AxisRange(bb.xmin, bb.xmax),
#         y=AxisRange(bb.ymin, bb.ymax),
#         z=AxisRange(bb.zmin, bb.zmax),
#         center=Center(cx, cy, cz)
#     )

# class Min(NamedTuple):
#     x: float
#     y: float
#     z: float

# class Max(NamedTuple):
#     x: float
#     y: float
#     z: float

# class Center(NamedTuple):
#     x: float
#     y: float
#     z: float

# class ObjPos(NamedTuple):
#     min: Min
#     max: Max
#     center: Center

# def get_obj_pos(obj) -> ObjPos:
#     bb = obj.val().BoundingBox()
#     cx = (bb.xmin + bb.xmax) / 2
#     cy = (bb.ymin + bb.ymax) / 2
#     cz = (bb.zmin + bb.zmax) / 2
#     return ObjPos(
#         min=Min(bb.xmin, bb.ymin, bb.zmin),
#         max=Max(bb.xmax, bb.ymax, bb.zmax),
#         center=Center(cx, cy, cz)
#     )


class Point(NamedTuple):
    x: float
    y: float
    z: float

class ObjPos(NamedTuple):
    min: Point
    max: Point
    center: Point

def get_obj_pos(obj) -> ObjPos:
    bb = obj.val().BoundingBox()
    
    # 데이터 생성
    p_min = Point(bb.xmin, bb.ymin, bb.zmin)
    p_max = Point(bb.xmax, bb.ymax, bb.zmax)
    p_center = Point(
        (p_min.x + p_max.x) / 2,
        (p_min.y + p_max.y) / 2,
        (p_min.z + p_max.z) / 2
    )
    
    return ObjPos(min=p_min, max=p_max, center=p_center)