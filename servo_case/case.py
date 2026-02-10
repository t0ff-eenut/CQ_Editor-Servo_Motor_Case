import project_top as ptop

body = None
back_block_1st = None
joint_a = None
back_block_2nd = None
joint_b = None
joint_c = None

class CaseConfig:
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

    joint_a_x = 7
    joint_a_y = 6
    joint_a_z = 7.2
    joint_a_pos_x = back_block_1st_pos_x + (back_block_1st_x / 2) - (joint_a_x / 2)
    joint_a_pos_y = back_block_1st_pos_y + (back_block_1st_y / 2) + (joint_a_y / 2)
    joint_a_pos_z = back_block_1st_pos_z + back_block_1st_z - 7.5 - joint_a_z

    joint_hole_body_size = 4.5
    joint_hole_body_dep = 5
    joint_hole_head_size = 2.7
    joint_hole_head_dep = joint_a_z - joint_hole_body_dep

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
    joint_b_pos_y = back_block_2nd_pos_y + (back_block_2nd_y / 2) + (joint_b_y / 2)
    joint_b_pos_z = joint_a_pos_z

    joint_c_x = 6
    joint_c_y = 9
    joint_c_z = 8.7
    joint_c_pos_x = -(body_x / 2) - (joint_c_x / 2)
    joint_c_pos_y = back_block_2nd_pos_y - (18.5 - (back_block_2nd_y / 2)) - (joint_c_y / 2)
    # joint_c_pos_z = joint_b_pos_z - ((joint_b_z - joint_c_z) / 2)
    joint_c_pos_z = joint_a_pos_z - (joint_c_z - joint_b_z)


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

def add_joint_holes(joint, cfg):
    joint_get_pos = ptop.get_obj_pos(joint)

    hole_pos = [
        (joint_get_pos.min.x + cfg.wing_hole_x_offset_minY_view + (cfg.wing_hole_size / 2), joint_get_pos.min.z + cfg.wing_hole_z_offset_minY_view + (cfg.wing_hole_size / 2))
    ]

    return (
        joint_get_pos
        .faces("<Y").workplane()
        .pushPoints(hole_pos)
        .hole(cfg.wing_hole_size)
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

def make_joint_c(cfg):
    return (
        ptop.cq.Workplane("XY")
        .rect(cfg.joint_c_x, cfg.joint_c_y)
        .extrude(cfg.joint_c_z)
        .translate((cfg.joint_c_pos_x, cfg.joint_c_pos_y, cfg.joint_c_pos_z))
    )

def case():
    global body, back_block_1st, joint_a, back_block_2nd, joint_b, joint_c
    cfg = CaseConfig()
    body = make_body(cfg)
    back_block_1st = make_back_block_1st(cfg)
    joint_a = make_joint_a(cfg)

    back_block_2nd = make_back_block_2nd(cfg)
    joint_b = make_joint_b(cfg)
    joint_c = make_joint_c(cfg)
    return cfg

