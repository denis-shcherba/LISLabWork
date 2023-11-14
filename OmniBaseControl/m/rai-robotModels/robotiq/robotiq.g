robotiq_base: { X: [0, 0, 1] }

Include: <robotiq_clean.g>
Edit robotiq_arg2f_base_link (robotiq_base): {}

# add F/T sensor

ftsensor (robotiq_base): { Q: [0, 0, -.035], shape: mesh, color: [0.2, 0.2, 0.2], mesh: <meshes/visual/robotiq_ft300.ply> }
 

# define a gripper, palm and fingers

gripper (robotiq_base): {
 Q: "d(180 0 1 0) d(90 0 0 1) t(0 0 -.14)"
 shape: marker, size: [.03], color: [.9, .9, .9], logical:{gripper: True} }
palm (robotiq_base): {
 Q: "d(90 1 0 0) t(0 .07 .0)",
 shape: capsule, color: [1.,1.,1.,.2], size: [.11, .04], contact: -1 }
finger1 (right_inner_finger_joint): {
 Q: [.0, -.009, .025]
 shape: capsule, size: [.04, .02], color: [1., 1., 1., .2], contact: -2 }
finger2 (left_inner_finger_joint): {
 Q: [.0, -.009, .025]
 shape: capsule, size: [.04, .02], color: [1., 1., 1., .2], contact: -2 }

Edit right_inner_finger_joint: { joint_scale: -1 }
Edit left_inner_finger_joint: { joint_scale: -1 }
 
robotiq_optitrackMarker (robotiq_base): { Q: [0, .049, 0.0033], shape: sphere, size: [.0049] }

Edit finger_joint: { q: .2 }
