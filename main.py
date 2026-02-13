import project_top as ptop
import servo_model.servo_model as svm
import dc_model.dc_model as dcm

svm_cfg = svm.servo_motor()
# show_object(svm.body, options={"color": (255, 255, 255), "alpha": 0.2}, name="body")
# show_object(svm.wing_L, options={"color": (255, 255, 255), "alpha": 0.2}, name="wing_L")
# show_object(svm.wing_R, options={"color": (255, 255, 255), "alpha": 0.2}, name="wing_R")
# show_object(svm.front_adaptor_hole_block_1st, options={"color": (255, 255, 255), "alpha": 0.2}, name="front_adaptor_hole_block_1st")
# show_object(svm.front_adaptor_hole_block_2nd, options={"color": (255, 255, 255), "alpha": 0.2}, name="front_adaptor_hole_block_2nd")
# show_object(svm.front_adaptor_hole_body, options={"color": (255, 255, 255), "alpha": 0.2}, name="front_adaptor_hole_body")
# show_object(svm.front_adaptor_hole_head, options={"color": (255, 255, 255), "alpha": 0.2}, name="front_adaptor_hole_head")
svm.body = svm.body.union(svm.wing_L)
svm.body = svm.body.union(svm.wing_R)
svm.body = svm.body.union(svm.front_adaptor_hole_block_1st)
svm.body = svm.body.union(svm.front_adaptor_hole_block_2nd)
svm.body = svm.body.union(svm.front_adaptor_hole_body)
svm.body = svm.body.union(svm.front_adaptor_hole_head)
# show_object(svm.body, options={"color": (255, 255, 255), "alpha": 0.2}, name="body")

dcm_cfg = dcm.dc_motor()
show_object(dcm.body, options={"color": (255, 255, 255), "alpha": 0.2}, name="case_body")
show_object(dcm.back_block_1st, options={"color": (255, 255, 255), "alpha": 0.2}, name="case_back_block_1st")
# show_object(dcm.joint_a, options={"color": (255, 255, 255), "alpha": 0.2}, name="case_joint_a")
# debug(dcm.joint_a_debug.vertices()) 
# show_object(dcm.joint_a_debug, options={"color": (255, 0, 0), "alpha": 0.9}, name="joint_a_debug")
show_object(dcm.joint_a, options={"color": (255, 255, 255), "alpha": 0.2}, name="case_joint_a")
show_object(dcm.back_block_2nd, options={"color": (255, 255, 255), "alpha": 0.2}, name="case_back_block_2nd")
show_object(dcm.joint_b, options={"color": (255, 255, 255), "alpha": 0.2}, name="case_joint_b")
show_object(dcm.joint_c, options={"color": (255, 255, 255), "alpha": 0.2}, name="case_joint_c")










# show_object(dcm.front_adaptor_braket_body_cutter, options={"color": (255, 0, 0), "alpha": 0.1})

# svm_front_adaptor_braket_head_cutter_get_pos = ptop.get_obj_pos(svm.front_adaptor_braket_head_cutter)
# c_front_adaptor_braket_head_cutter_get_pos = ptop.get_obj_pos(dcm.front_adaptor_braket_head_cutter)

# svm.body = svm.body.translate((c_cfg.adaptor_pos_x - svm_cfg.adaptor_pos_x, 
#                                c_front_adaptor_braket_head_cutter_get_pos.y.min - svm_front_adaptor_braket_head_cutter_get_pos.y.min, 
#                                c_cfg.adaptor_pos_z - svm_cfg.adaptor_pos_z))

# show_object(svm.body, options={"color": (255, 255, 255), "alpha": 0.2})

# show_object(dcm.a_nut_cutter, options={"color": (255, 0, 0), "alpha": 0.1})
