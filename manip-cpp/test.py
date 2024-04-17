import robotic as ry
import manipulation as manip

def main():
    C = ry.Config()

    C.addFile("/home/eckart/rai-robotModels/scenarios/pandaSingle.g");
    C.delFrame("cameraWrist")

    C.addFrame("hinge", "table").setJoint(ry.JT.rigid) .setRelativePosition([.3, .2, .15])
    C.addFrame("door", "hinge").setRelativePosition([.1, .0, .0]) .setShape(ry.ST.ssBox, [.2, .04, .2, .005]). setContact(1)
    C.addFrame("handle", "door").setRelativePosition([.08, -.02, .0]) .setShape(ry.ST.marker, [.1])

    gripper = "l_gripper"
    palm = "l_palm"
    obj = "door"
    table = "table"
    qHome = C.getJointState()

    for i in range(20):
        C.view(True)
        seq = manip.ManipulationModelling(C, "pivot", [gripper])
        #seq.set\
        #...


        seq.komo.addObjective([1,2], ry.FS.positionDiff, [gripper,"handle"], ry.OT.eq, [1])
        seq.komo.addObjective([1,2], ry.FS.vectorZRel, [gripper, "door"], ry.OT.sos, [1e-1], [0, -1, ])
        seq.no_collision([1,2], obj, palm)

        pose0 = seq.solve()
        if not seq.feasible:
            return False
    
        M1 = manip.ManipulationModelling(C, "pivot", ['l_gripper'])
        M1.setup_point_to_point_motion(qHome, pose0[-1])
        path1 = M1.solve()
        if not M1.feasible:
            return False

        M1.play(C, 4)

if __name__ == "__main__":

    main()