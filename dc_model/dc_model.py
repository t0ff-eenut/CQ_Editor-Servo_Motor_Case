import project_top as ptop

body = None
back_block_1st = None
joint_a = None
joint_a_debug = None

back_block_2nd = None
joint_b = None

# joint_c_block = None
joint_c = None
joint_d = None

front_block_1st = None

class DCConfig:
    body_x = 49.1
    body_y = 12.8
    body_z = 22.5
    body_pos_x = 0
    body_pos_y = 0
    body_pos_z = 0

    back_block_1st_x = body_x
    back_block_1st_y = 6.5
    back_block_1st_z = body_z
    back_block_1st_pos_x = body_pos_x
    back_block_1st_pos_y = (body_y / 2) + (back_block_1st_y / 2)
    back_block_1st_pos_z = body_pos_z

    joint_a_x = 7.2
    # joint_a_y = 6
    joint_a_y = 7.2
    joint_a_z = 7.2
    joint_a_pos_x = back_block_1st_pos_x + (back_block_1st_x / 2) - (joint_a_x / 2)
    joint_a_pos_y = back_block_1st_pos_y + (back_block_1st_y / 2) + (joint_a_y / 2)
    joint_a_pos_z = back_block_1st_pos_z + back_block_1st_z - 7.5 - joint_a_z

    joint_hole_body_size = 4.5
    joint_hole_body_dep = 5
    joint_hole_head_size = 2.7
    joint_hole_head_dep = joint_a_z - joint_hole_body_dep
    joint_hole_body_ring = (joint_a_x - joint_hole_body_size) / 2
    joint_a_pos_y = joint_a_pos_y - joint_hole_body_ring
    # joint_a_y = joint_a_x - joint_hole_body_ring
    # 8.6 + 7.2 + 7.5 =  = 22.5

    back_block_2nd_x = back_block_1st_x - joint_a_x
    back_block_2nd_y = 4.5
    back_block_2nd_z = back_block_1st_z
    back_block_2nd_pos_x = back_block_1st_pos_x - (joint_a_x / 2)
    back_block_2nd_pos_y = back_block_1st_pos_y + (back_block_1st_y / 2) + (back_block_2nd_y / 2)
    back_block_2nd_pos_z = back_block_1st_pos_z

    joint_b_x = joint_a_x
    joint_b_y = joint_a_y
    joint_b_z = joint_a_z
    joint_b_pos_x = back_block_2nd_pos_x - (back_block_2nd_x / 2) + 8.5 + (joint_b_x / 2)
    joint_b_pos_y = back_block_2nd_pos_y + (back_block_2nd_y / 2) + (joint_b_y / 2) - joint_hole_body_ring
    joint_b_pos_z = joint_a_pos_z

    # joint_c_block_x = joint_b_x
    # joint_c_block_y = 3.4 - joint_hole_body_ring
    # joint_c_block_z = joint_b_z
    # joint_c_block_pos_x = -(body_x / 2) - (joint_c_block_x / 2)
    # joint_c_block_pos_y = back_block_2nd_pos_y - (18.5 - (back_block_2nd_y / 2)) - (joint_b_y / 2)
    # joint_c_block_pos_z = joint_b_pos_z

    joint_c_x = joint_b_x
    joint_c_y_margin = 3.4 - joint_hole_body_ring
    joint_c_y = joint_b_y + joint_c_y_margin
    joint_c_z = joint_b_zs
    # joint_c_x = 5.8
    # joint_c_y = 9
    # joint_c_z = 8.7
    joint_c_pos_x = -(body_x / 2) - (joint_c_x / 2) + ((joint_c_x - joint_hole_body_size) / 2)
    # joint_c_pos_x = -(body_x / 2) - (joint_c_x / 2) + 0.5
    joint_c_pos_y = back_block_2nd_pos_y - (18.5 - (back_block_2nd_y / 2)) - (joint_c_y / 2)
    # joint_c_pos_z = joint_b_pos_z - ((joint_b_z - joint_c_z) / 2)
    joint_c_pos_z = joint_a_pos_z - (joint_c_z - joint_b_z)

    front_block_1st_x = 20.7
    front_block_1st_y = 14
    front_block_1st_z = body_z
    front_block_1st_pos_x = -(body_x / 2) + (front_block_1st_x / 2)
    front_block_1st_pos_y = -(body_y / 2) - (front_block_1st_y / 2)
    front_block_1st_pos_z = body_pos_z

    joint_d_x = joint_b_x
    joint_d_y = joint_b_y
    joint_d_z = joint_b_z
    joint_d_pos_x = front_block_1st_pos_x + (front_block_1st_x / 2) + (joint_d_x / 2) - joint_hole_body_ring
    joint_d_pos_y = -(body_y / 2) - (joint_d_y / 2) + joint_hole_body_ring
    joint_d_pos_z = joint_b_pos_z


def make_body(cfg):
    return (
        ptop.cq.Workplane("XY")
        .rect(cfg.body_x, cfg.body_y)
        .extrude(cfg.body_z)
    )

def make_back_block_1st(cfg):
    return (
        ptop.cq.Workplane("XY")
        .rect(cfg.back_block_1st_x, cfg.back_block_1st_y)
        .extrude(cfg.back_block_1st_z)
        .translate((cfg.back_block_1st_pos_x, cfg.back_block_1st_pos_y, cfg.back_block_1st_pos_z))
    )

def make_joint_a(cfg):
    return (
        ptop.cq.Workplane("XY")
        .rect(cfg.joint_a_x, cfg.joint_a_y)
        .extrude(cfg.joint_a_z)
        .translate((cfg.joint_a_pos_x, cfg.joint_a_pos_y, cfg.joint_a_pos_z))
    )

def debug(joint, cfg):
    joint_get_pos = ptop.get_obj_pos(joint)

    hole_pos = [
        # (joint_get_pos.min.x + cfg.wing_hole_x_offset_minY_view + (cfg.wing_hole_size / 2), joint_get_pos.min.z + cfg.wing_hole_z_offset_minY_view + (cfg.wing_hole_size / 2))
        (joint_get_pos.center.x, joint_get_pos.center.y)
    ]
    return (
        joint
        .faces(">Z").workplane()
        # .move(joint_get_pos.center.x, joint_get_pos.center.y)
        .move(hole_pos[0][0],hole_pos[0][1])
        # .move(hole_pos[0])
        .sphere(0.5)
        #.line(0, 3, forConstruction=True)
    )

def add_joint_holes_a(joint, cfg):
    joint_get_pos = ptop.get_obj_pos(joint)

    hole_pos = [
        # (joint_get_pos.min.x + cfg.wing_hole_x_offset_minY_view + (cfg.wing_hole_size / 2), joint_get_pos.min.z + cfg.wing_hole_z_offset_minY_view + (cfg.wing_hole_size / 2))
        (joint_get_pos.center.x, joint_get_pos.center.y)
    ]
    return (
        joint
        .faces(">Z").workplane()
        .pushPoints(hole_pos)
        .cboreHole(cfg.joint_hole_head_size, cfg.joint_hole_body_size, cfg.joint_hole_body_dep)
    )

def make_back_block_2nd(cfg):
    return (
        ptop.cq.Workplane("XY")
        .rect(cfg.back_block_2nd_x, cfg.back_block_2nd_y)
        .extrude(cfg.back_block_2nd_z)
        .translate((cfg.back_block_2nd_pos_x, cfg.back_block_2nd_pos_y, cfg.back_block_2nd_pos_z))
    )

def make_joint_b(cfg):
    return (
        ptop.cq.Workplane("XY")
        .rect(cfg.joint_b_x, cfg.joint_b_y)
        .extrude(cfg.joint_b_z)
        .translate((cfg.joint_b_pos_x, cfg.joint_b_pos_y, cfg.joint_b_pos_z))
    )

# def make_joint_c_block(cfg):
#     return (
#         ptop.cq.Workplane("XY")
#         .rect(cfg.joint_c_block_x, cfg.joint_c_block_y)
#         .extrude(cfg.joint_c_block_z)
#         .translate((cfg.joint_c_block_pos_x, cfg.joint_c_block_pos_y, cfg.joint_c_block_pos_z))
#     )

def make_joint_c(cfg):
    return (
        ptop.cq.Workplane("XY")
        .rect(cfg.joint_c_x, cfg.joint_c_y)
        .extrude(cfg.joint_c_z)
        .translate((cfg.joint_c_pos_x, cfg.joint_c_pos_y, cfg.joint_c_pos_z))
    )

def add_joint_holes_b(joint, cfg):
    joint_get_pos = ptop.get_obj_pos(joint)

    hole_pos = [
        # (joint_get_pos.min.x + cfg.wing_hole_x_offset_minY_view + (cfg.wing_hole_size / 2), joint_get_pos.min.z + cfg.wing_hole_z_offset_minY_view + (cfg.wing_hole_size / 2))
        # (joint_get_pos.center.x, joint_get_pos.center.y - 1.5)
        (joint_get_pos.center.x, joint_get_pos.center.y - (cfg.joint_c_y_margin / 2))
    ]
    return (
        joint
        .faces(">Z").workplane()
        .pushPoints(hole_pos)
        .cboreHole(cfg.joint_hole_head_size, cfg.joint_hole_body_size, cfg.joint_hole_body_dep)
    )    

def make_front_block_1st(cfg):
    return (
        ptop.cq.Workplane("XY")
        .rect(cfg.front_block_1st_x, cfg.front_block_1st_y)
        .extrude(cfg.front_block_1st_z)
        .translate((cfg.front_block_1st_pos_x, cfg.front_block_1st_pos_y, cfg.front_block_1st_pos_z))
    )

def make_joint_d(cfg):
    return (
        ptop.cq.Workplane("XY")
        .rect(cfg.joint_d_x, cfg.joint_d_y)
        .extrude(cfg.joint_d_z)
        .translate((cfg.joint_d_pos_x, cfg.joint_d_pos_y, cfg.joint_d_pos_z))
    )

def dc_motor():
    global body, back_block_1st, joint_a, back_block_2nd, joint_b, joint_c, joint_d, front_block_1st
    global joint_a_debug

    cfg = DCConfig()
    body = make_body(cfg)
    back_block_1st = make_back_block_1st(cfg)
    joint_a = make_joint_a(cfg)
    # joint_a_debug = debug(joint_a, cfg)
    joint_a = add_joint_holes_a(joint_a, cfg)
    back_block_2nd = make_back_block_2nd(cfg)
    joint_b = make_joint_b(cfg)
    joint_b = add_joint_holes_a(joint_b, cfg)
    # joint_c_block = make_joint_c_block(cfg)
    joint_c = make_joint_c(cfg)
    joint_c = add_joint_holes_b(joint_c, cfg)
    # joint_c = add_joint_holes_a(joint_c, cfg)
    front_block_1st = make_front_block_1st(cfg)
    joint_d = make_joint_d(cfg)
    joint_d = add_joint_holes_a(joint_d, cfg)

    return cfg

