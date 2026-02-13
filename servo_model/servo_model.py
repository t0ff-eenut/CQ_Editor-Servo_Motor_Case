import project_top as ptop

body = None
wing = None
wing_L = None
wing_R = None
front_adaptor_hole_block_1st = None
front_adaptor_hole_block_2nd = None
front_adaptor_hole_body = None
front_adaptor_hole_head =None

class ServoConfig:
    body_x = 39.4
    body_y = 38
    body_z = 20
    body_pos_x = 0
    body_pos_y = 0
    body_pos_z = 0

    wing_x = 7
    wing_y = 2.5
    wing_z = 18.5
    wing_pos_x = (body_x / 2) + (wing_x / 2)
    wing_pos_y = (body_y / 2) - 32 + (wing_y / 2)
    wing_pos_z = (body_z - wing_z) / 2

    wing_hole_x_offset_minY_view = wing_hole_z_offset_minY_view = 2
    wing_hole_size = 4.5
    # wing_hole_interval = 5.5
    
    front_adaptor_block_1st_x = body_x
    front_adaptor_block_1st_y = 2.5
    front_adaptor_block_1st_z = 17.8
    front_adaptor_block_1st_pos_x = body_pos_x
    front_adaptor_block_1st_pos_y = -((body_y / 2) + (front_adaptor_block_1st_y / 2))
    front_adaptor_block_1st_pos_z = (body_z - front_adaptor_block_1st_z) / 2

    # 38 + 2.5 = 40.5
    # 1.5 + hole body + hole_head = 
    # full_y = body_y + front_adaptor_block_1st_y + front_adaptor_block_2nd_y + hole body + hole_head = 46

    front_adaptor_block_2nd_x = body_x
    front_adaptor_block_2nd_y = 1.5
    front_adaptor_block_2nd_z = 13
    front_adaptor_block_2nd_pos_x = body_pos_x
    # front_adaptor_block_2nd_pos_y = -((body_y / 2) + front_adaptor_block_1st_y + (front_adaptor_block_2nd_y / 2))
    front_adaptor_block_2nd_pos_y = front_adaptor_block_1st_pos_y - ((front_adaptor_block_1st_y / 2) + (front_adaptor_block_2nd_y / 2))
    front_adaptor_block_2nd_pos_z = (body_z - front_adaptor_block_2nd_z) / 2


    adaptor_body_size = 2.5
    adaptor_body_height = 0.8
    adaptor_head_size = 5.7
    adaptor_head_height = 3.2
    adaptor_x_offset_minY_view = 19 - wing_x - adaptor_head_size
    adaptor_z_offset_minY_view = 12.5 - adaptor_head_size

    adaptor_body_pos_x = -(body_x / 2) + adaptor_x_offset_minY_view + (adaptor_head_size / 2)
    adaptor_body_pos_y = front_adaptor_block_2nd_pos_y - (front_adaptor_block_2nd_y / 2)
    adaptor_body_pos_z = adaptor_z_offset_minY_view + (adaptor_head_size / 2)

    adaptor_head_pos_x = adaptor_body_pos_x
    adaptor_head_pos_y = adaptor_body_pos_y - (front_adaptor_block_2nd_y / 2)
    adaptor_head_pos_z = adaptor_body_pos_z


    # # adaptor_height = 4
    # wing_front_dist = 9.5

def make_body(cfg):
    return (
        ptop.cq.Workplane("XY")
        .rect(cfg.body_x, cfg.body_y)
        .extrude(cfg.body_z)
    )

def make_wing(cfg):
    return (
        ptop.cq.Workplane("XY")
        .rect(cfg.wing_x, cfg.wing_y)
        .extrude(cfg.wing_z)
        .translate((cfg.wing_pos_x, cfg.wing_pos_y, cfg.wing_pos_z))
    )

def add_wing_holes(wing, cfg):
    wing_get_pos = ptop.get_obj_pos(wing)

    hole_pos_line = [
        (wing_get_pos.min.x + cfg.wing_hole_x_offset_minY_view + (cfg.wing_hole_size / 2), wing_get_pos.min.z + cfg.wing_hole_z_offset_minY_view + (cfg.wing_hole_size / 2)),
        (wing_get_pos.min.x + cfg.wing_hole_x_offset_minY_view + (cfg.wing_hole_size / 2), wing_get_pos.max.z - cfg.wing_hole_z_offset_minY_view - (cfg.wing_hole_size / 2))
    ]

    return (
        wing
        .faces("<Y").workplane()
        .pushPoints(hole_pos_line)
        .hole(cfg.wing_hole_size)
    )

def make_front_adaptor_hole_block_1st(cfg):
    return (
        ptop.cq.Workplane("XY")
        .rect(cfg.front_adaptor_block_1st_x, cfg.front_adaptor_block_1st_y)
        .extrude(cfg.front_adaptor_block_1st_z)
        .translate((cfg.front_adaptor_block_1st_pos_x, cfg.front_adaptor_block_1st_pos_y, cfg.front_adaptor_block_1st_pos_z))
    )

def make_front_adaptor_hole_block_2nd(cfg):
    return (
        ptop.cq.Workplane("XY")
        .rect(cfg.front_adaptor_block_2nd_x, cfg.front_adaptor_block_2nd_y)
        .extrude(cfg.front_adaptor_block_2nd_z)
        .translate((cfg.front_adaptor_block_2nd_pos_x, cfg.front_adaptor_block_2nd_pos_y, cfg.front_adaptor_block_2nd_pos_z))
    )

def make_front_adaptor_hole_body(cfg):
    return (
        ptop.cq.Workplane("XZ")
        .circle(cfg.adaptor_body_size / 2)
        .extrude(cfg.adaptor_body_height)
        .translate((cfg.adaptor_body_pos_x, cfg.adaptor_body_pos_y, cfg.adaptor_body_pos_z))
    )

def make_front_adaptor_hole_head(cfg):
    return (
        ptop.cq.Workplane("XZ")
        .circle(cfg.adaptor_head_size / 2)
        .extrude(cfg.adaptor_head_height)
        .translate((cfg.adaptor_head_pos_x, cfg.adaptor_head_pos_y, cfg.adaptor_head_pos_z))
    )

def servo_motor():
    global body, wing, wing_L, wing_R, front_adaptor_hole_block_1st, front_adaptor_hole_block_2nd, front_adaptor_hole_body, front_adaptor_hole_head

    cfg = ServoConfig()
    body = make_body(cfg)
    wing = make_wing(cfg)
    wing = add_wing_holes(wing, cfg)
    wing_R = wing
    wing_L = wing.mirror("YZ")
    front_adaptor_hole_block_1st = make_front_adaptor_hole_block_1st(cfg)
    front_adaptor_hole_block_2nd = make_front_adaptor_hole_block_2nd(cfg)
    front_adaptor_hole_body = make_front_adaptor_hole_body(cfg)
    front_adaptor_hole_head = make_front_adaptor_hole_head(cfg)


    return cfg

