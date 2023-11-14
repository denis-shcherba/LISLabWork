## create standard base frame before including

omnibase_base: { multibody: true }
omnibase_link0: {  }

omnibase_link0_0(panda_link0): { shape: mesh, mesh: <models/structure0.stl>, visual: True, contact: -2 }

omnibase_hinge1_origin(omnibase_link0): { rel: [0, 0, 0.333, 1, 0, 0, 0] }
omnibase_hinge2_origin(omnibase_link0): { rel: [0, 0, 0.333, 1, 0, 0, 0] }
omnibase_hinge3_origin(omnibase_link0): { rel: [0, 0, 0.333, 1, 0, 0, 0] }

omnibase_hinge1(omnibase_hinge1_origin): { joint: hingeZ }
omnibase_hinge2(omnibase_hinge2_origin): { joint: hingeZ }
omnibase_hinge3(omnibase_hinge3_origin): { joint: hingeZ }

omnibase_wheel1(omnibase_hinge1): {  }
omnibase_wheel2(omnibase_hinge2): {  }
omnibase_wheel3(omnibase_hinge3): {  }

omnibase_wheel1_0(omnibase_wheel1): { shape: capsule, color: [1.,1.,1.,1.], size: [.12, .08], Q: "t(-.04 .0 .03) d(90 0 1 0)", visual: True, contact: -2 }
omnibase_wheel2_0(omnibase_wheel2): { shape: capsule, color: [1.,1.,1.,1.], size: [.12, .08], Q: "t(-.04 .0 .03) d(90 0 1 0)", visual: True, contact: -2 }
omnibase_wheel3_0(omnibase_wheel3): { shape: capsule, color: [1.,1.,1.,1.], size: [.12, .08], Q: "t(-.04 .0 .03) d(90 0 1 0)", visual: True, contact: -2 }

Edit omnibase_link0(omnibase_base): {}

## zero position

Edit omnibase_hinge1: { q: .0 }
Edit omnibase_hinge2: { q: .0 }
Edit omnibase_hinge3: { q: .0 }
