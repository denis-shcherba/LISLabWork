world: {}

### floor

floor(world): {
 shape: ssBox, Q: "t(0 0. .1)", size: [10, 10, .1, .02], color: [.3, .3, .3],
 contact: 1, logical: { },
 friction: .1
}

### omnibase

# Prefix: "ob_"
Include: <omnibase.g>

# Prefix: False

# Edit ob_panda_base (floor): { Q: "t(0 0 .05) d(90 0 0 1)" joint:rigid }
Edit omnibase_base (floor): { Q: "t(0 0 .05)" joint:rigid }
