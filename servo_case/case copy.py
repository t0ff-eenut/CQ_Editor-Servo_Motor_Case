
# body_front_2_cut_obj_bb = body_front_2_cut_obj.val().BoundingBox()
# # print(body_front_2_cut_obj_bb.xmin)      # -28.25
# # print(body_front_2_cut_obj_bb.xmax)      # 28.25
# # print(body_front_2_cut_obj_bb.ymin)      # -17.25
# # print(body_front_2_cut_obj_bb.ymax)      # -9.75
# # print(body_front_2_cut_obj_bb.zmin)      # 0.0
# # print(body_front_2_cut_obj_bb.zmax)      # 22.0
# body_front_2_cut_obj_cx = (body_front_2_cut_obj_bb.xmin + body_front_2_cut_obj_bb.xmax) / 2
# body_front_2_cut_obj_cy = (body_front_2_cut_obj_bb.ymin + body_front_2_cut_obj_bb.ymax) / 2
# body_front_2_cut_obj_cz = (body_front_2_cut_obj_bb.zmin + body_front_2_cut_obj_bb.zmax) / 2
# # print(body_front_2_cut_obj_cx)      # 0.0
# # print(body_front_2_cut_obj_cy)      # -13.5
# # print(body_front_2_cut_obj_cz)      # 11.0

import project_top as ptop

body = None
# wing = None
# wing_cutter = None
front_adaptor_braket_head_cutter = None
front_adaptor_braket_body_cutter = None
a_nut_cutter = None

class CaseConfig:
    body_x = 54.8
    body_y = 45.5
    body_z = 33.5
    body_pos_x = 0
    body_pos_y = 0
    body_pos_z = 0

    # wing_x = 7
    # wing_y = 2.5
    # wing_z = 18.5
    # wing_pos_x = 0
    # wing_pos_y = 0
    # wing_pos_z = 0

    # wing_hole_x_offset_minY_view = wing_hole_z_offset_minY_view = 2
    # wing_hole_size = 4.5
    # # wing_hole_interval = 5.5
    
 
    # # adaptor_depth = 4

    adaptor_braket_head_height = 5.3
    adaptor_braket_head_pos_x = 0
    adaptor_braket_head_pos_y = 0
    adaptor_braket_head_pos_z = 0

    adaptor_braket_body_height = 7.2    # 16 - 12.5(5.3+7.2) = 3.5
    adaptor_braket_body_pos_x = 0
    adaptor_braket_body_pos_y = 0
    adaptor_braket_body_pos_z = 0

    adaptor_head_size = 6
    adaptor_head_height = adaptor_braket_body_height
    adaptor_body_size = 9.5
    adaptor_body_height = 3.5
    adaptor_x_offset_minY_view = adaptor_z_offset_minY_view = 7
    adaptor_pos_x = 0
    adaptor_pos_y = 0
    adaptor_pos_z = 0

    a_nut_hole_x = a_nut_hole_y = 5.5
    a_nut_hole_height = 6
    a_nut_hole_x_offset = 22
    # a_nut_hole_z_offset = 7.5
    a_nut_hole_z_offset = adaptor_z_offset_minY_view
    

    # # adaptor_height = 4
    # wing_front_dist = 9.5

def make_body(cfg):
    return (
        ptop.cq.Workplane("XY")
        .rect(cfg.body_x, cfg.body_y)
        .extrude(cfg.body_z)
    )

# def make_wing(cfg):
#     cfg.wing_pos_x = (cfg.body_x / 2) - (cfg.wing_x / 2)
#     # cfg.wing_pos_y = (body_y / 2) - (wing_y / 2) - 32.5   # -9.75
#     cfg.wing_pos_y = -(cfg.body_y / 2) + 15.5 + (cfg.wing_y / 2)    # -9.75
#     cfg.wing_pos_z = (cfg.body_z / 2) - (cfg.wing_z / 2)

#     return (
#         ptop.cq.Workplane("XY")
#         .rect(cfg.wing_x, cfg.wing_y)
#         .extrude(cfg.wing_z)
#         .translate((cfg.wing_pos_x, cfg.wing_pos_y, cfg.wing_pos_z))
#     )

# def add_wing_holes(wing, cfg):
#     wing_get_pos = ptop.get_obj_pos(wing)

#     hole_pos_line = [
#         (wing_get_pos.x.min + cfg.wing_hole_x_offset_minY_view + (cfg.wing_hole_size / 2), wing_get_pos.z.min + cfg.wing_hole_z_offset_minY_view + (cfg.wing_hole_size / 2)),
#         (wing_get_pos.x.min + cfg.wing_hole_x_offset_minY_view + (cfg.wing_hole_size / 2), wing_get_pos.z.max - cfg.wing_hole_z_offset_minY_view - (cfg.wing_hole_size / 2))
#     ]
#     # print("hole_pos_line[1][1] - hole_pos_line[0][1] : ", (hole_pos_line[1][1] - (cfg.wing_hole_size / 2)) - (hole_pos_line[0][1] + (cfg.wing_hole_size / 2))) == wing_hole_interval
#     return (
#         wing
#         .faces("<Y").workplane()
#         .pushPoints(hole_pos_line)
#         .hole(cfg.wing_hole_size)
#     )

# def make_wing_cutter(cfg):
#     return (
#         ptop.cq.Workplane("XY")
#         .rect(cfg.wing_x, cfg.body_y)
#         .extrude(cfg.body_z)
#         .translate((cfg.wing_pos_x, 0, 0))
#     )

def make_front_adaptor_braket_head_cutter(cfg):

    body_get_pos = ptop.get_obj_pos(body)
    cfg.adaptor_braket_head_pos_x = 0
    # cfg.adaptor_braket_head_pos_y = -(cfg.body_y / 2) + (cfg.adaptor_braket_head_height / 2)
    cfg.adaptor_braket_head_pos_y = body_get_pos.y.min + (cfg.adaptor_braket_head_height / 2)
    cfg.adaptor_braket_head_pos_z = 0

    return (
        ptop.cq.Workplane("XY")
        .rect(cfg.body_x, cfg.adaptor_braket_head_height)
        .extrude(cfg.body_z)
        .translate((cfg.adaptor_braket_head_pos_x, cfg.adaptor_braket_head_pos_y, cfg.adaptor_braket_head_pos_z))
    )

def make_front_adaptor_braket_body_cutter(cfg):

    front_adaptor_braket_head_cutter_get_pos = ptop.get_obj_pos(front_adaptor_braket_head_cutter)
    cfg.adaptor_braket_body_pos_x = 0
    cfg.adaptor_braket_body_pos_y = front_adaptor_braket_head_cutter_get_pos.y.max + ((cfg.adaptor_head_height + cfg.adaptor_body_height) / 2)
    cfg.adaptor_braket_body_pos_z = 0

    return (
        ptop.cq.Workplane("XY")
        # .rect(cfg.body_x, cfg.adaptor_braket_body_height)
        .rect(cfg.body_x, cfg.adaptor_head_height + cfg.adaptor_body_height)
        .extrude(cfg.body_z)
        # .translate((cfg.adaptor_braket_body_pos_x, cfg.adaptor_braket_body_pos_y, cfg.adaptor_braket_body_pos_z))
    )

def add_front_adaptor_holes(cutter, cfg):
    cutter_get_pos = ptop.get_obj_pos(cutter)

    cfg.adaptor_pos_x = cutter_get_pos.x.min + cfg.adaptor_x_offset_minY_view + (cfg.adaptor_body_size / 2)
    cfg.adaptor_pos_y = cutter_get_pos.center.y
    # print("cutter_get_pos.center.z : ", cutter_get_pos.center.z)                                                                                                                            # 11.0
    # # cfg.adaptor_pos_z = cutter_get_pos.center.z
    # print("cutter_get_pos.z.min + cfg.adaptor_x_offset_minY_view + (cfg.adaptor_body_size / 2) : ", cutter_get_pos.z.min + cfg.adaptor_x_offset_minY_view + (cfg.adaptor_body_size / 2))    # 11.75
    cfg.adaptor_pos_z = cutter_get_pos.z.min + cfg.adaptor_z_offset_minY_view + (cfg.adaptor_body_size / 2)

    adaptor_hole_pos_minY_view = [
        # (-(body_front_cut_x / 2) + (12 - (adaptor_hole_head_size / 2)), body_get_pos.center.z)
        (cfg.adaptor_pos_x, cfg.adaptor_pos_z)
    ]

    return (
        cutter
        .faces("<Y").workplane()
        .pushPoints(adaptor_hole_pos_minY_view)
        # .cboreHole(cfg.adaptor_body_size, cfg.adaptor_head_size, cfg.adaptor_head_height - cfg.adaptor_body_height)
        .cboreHole(cfg.adaptor_head_size, cfg.adaptor_body_size, cfg.adaptor_body_height)
        .mirror(mirrorPlane="XZ")
        .translate((cfg.adaptor_braket_body_pos_x, cfg.adaptor_braket_body_pos_y, cfg.adaptor_braket_body_pos_z))
    )

def make_a_nut_cutter(cfg):
    body_get_pos = ptop.get_obj_pos(body)
    front_adaptor_braket_body_cutter_get_pos = ptop.get_obj_pos(front_adaptor_braket_body_cutter)
    # print("body_get_pos.x.min : ", body_get_pos.x.min)
    # print("cfg.adaptor_x_offset_minY_view : ", cfg.adaptor_x_offset_minY_view)
    # print("cfg.adaptor_body_size : ", cfg.adaptor_body_size)
    # print("(cfg.a_nut_hole_x / 2) : ", (cfg.a_nut_hole_x / 2))
    
    # print("body_get_pos.x.min + cfg.adaptor_x_offset_minY_view + cfg.adaptor_body_size + 6 + (cfg.a_nut_hole_x / 2) : ", body_get_pos.x.min + cfg.adaptor_x_offset_minY_view + cfg.adaptor_body_size + 6 + (cfg.a_nut_hole_x / 2))
    # print("body_get_pos.x.min + 28 - (cfg.a_nut_hole_x / 2) : ",  body_get_pos.x.min + 28 - (cfg.a_nut_hole_x / 2))

    cfg.a_nut_hole_pos_x = body_get_pos.x.min + cfg.adaptor_x_offset_minY_view + cfg.adaptor_body_size + 6 + (cfg.a_nut_hole_x / 2)
    # cfg.a_nut_hole_pos_x = body_get_pos.x.min + 28 - (cfg.a_nut_hole_x / 2)
    cfg.a_nut_hole_pos_y = front_adaptor_braket_body_cutter_get_pos.y.max - (cfg.a_nut_hole_y / 2)
    cfg.a_nut_hole_pos_z = body_get_pos.z.min + cfg.a_nut_hole_z_offset + (cfg.a_nut_hole_height / 2)
    return (
        ptop.cq.Workplane("XY")
        .rect(cfg.a_nut_hole_x, cfg.a_nut_hole_y)
        .extrude(cfg.a_nut_hole_height)
        .translate((cfg.a_nut_hole_pos_x, cfg.a_nut_hole_pos_y, cfg.a_nut_hole_pos_z))
    )

def case():
    # global body, wing, wing_cutter, front_adaptor_braket_head_cutter, front_adaptor_braket_body_cutter, a_nut_cutter
    global body, front_adaptor_braket_head_cutter, front_adaptor_braket_body_cutter, a_nut_cutter
    cfg = CaseConfig()
    body = make_body(cfg)

    # wing = make_wing(cfg)
    # wing = add_wing_holes(wing, cfg)
    # wing_cutter = make_wing_cutter(cfg)
    # wing_cutter = wing_cutter.cut(wing)

    # body = body.cut(wing_cutter)
    # body = body.cut(wing_cutter.mirror("YZ"))

    front_adaptor_braket_head_cutter = make_front_adaptor_braket_head_cutter(cfg)
    body = body.cut(front_adaptor_braket_head_cutter)
    front_adaptor_braket_body_cutter = make_front_adaptor_braket_body_cutter(cfg)
    front_adaptor_braket_body_cutter = add_front_adaptor_holes(front_adaptor_braket_body_cutter, cfg)
    body = body.cut(front_adaptor_braket_body_cutter)

    a_nut_cutter = make_a_nut_cutter(cfg)
    # body = body.cut(a_nut_cutter)


    # # body = front_cut(body, cfg)

    return cfg

