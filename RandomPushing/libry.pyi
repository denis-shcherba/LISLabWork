"""rai bindings"""
from __future__ import annotations
import libry
import typing
import numpy
_Shape = typing.Tuple[int, ...]

__all__ = [
    "ArgWord",
    "BotOp",
    "CameraView",
    "CameraViewSensor",
    "Ceres",
    "Config",
    "ConfigurationViewer",
    "ControlMode",
    "FS",
    "Feature",
    "Frame",
    "ImageViewer",
    "ImpType",
    "Ipopt",
    "JT",
    "KOMO",
    "KOMO_Objective",
    "LBFGS",
    "NLP",
    "NLP_Factory",
    "NLP_Solver",
    "NLP_SolverID",
    "NLP_SolverOptions",
    "NLopt",
    "OT",
    "OptBench_Skeleton_Handover",
    "OptBench_Skeleton_Pick",
    "OptBench_Skeleton_StackAndBalance",
    "OptBenchmark_InvKin_Endeff",
    "PathFinder",
    "PointCloudViewer",
    "ST",
    "SY",
    "Simulation",
    "SimulationEngine",
    "Skeleton",
    "SolverReturn",
    "XBall",
    "above",
    "aboveBox",
    "acceleration",
    "accumulatedCollisions",
    "adversarialDropper",
    "alignByInt",
    "angularVel",
    "augmentedLag",
    "bounce",
    "box",
    "boxGraspX",
    "boxGraspY",
    "boxGraspZ",
    "break",
    "bullet",
    "camera",
    "capsule",
    "closeGripper",
    "contact",
    "contactComplementary",
    "contactConstraints",
    "contactStick",
    "cylinder",
    "dampMotion",
    "depthNoise",
    "distance",
    "downUp",
    "dynamic",
    "dynamicOn",
    "dynamicTrans",
    "end",
    "energy",
    "eq",
    "f",
    "forceBalance",
    "free",
    "gazeAt",
    "generic",
    "getStartGoalPath",
    "gradientDescent",
    "hingeX",
    "hingeY",
    "hingeZ",
    "identical",
    "ineq",
    "ineqB",
    "ineqP",
    "inside",
    "insideBox",
    "jointLimits",
    "kinematic",
    "lift",
    "logBarrier",
    "magic",
    "magicTrans",
    "makeFree",
    "marker",
    "mesh",
    "newton",
    "noPenetrations",
    "none",
    "objectImpulses",
    "openGripper",
    "oppose",
    "pairCollision_negScalar",
    "pairCollision_normal",
    "pairCollision_p1",
    "pairCollision_p2",
    "pairCollision_vector",
    "params_add",
    "params_file",
    "params_print",
    "phiTransXY",
    "physics",
    "physx",
    "pointCloud",
    "pose",
    "poseDiff",
    "poseEq",
    "poseRel",
    "position",
    "positionDiff",
    "positionEq",
    "positionRel",
    "push",
    "pushAndPlace",
    "qItself",
    "quad",
    "quasiStatic",
    "quasiStaticOn",
    "quatBall",
    "quaternion",
    "quaternionDiff",
    "quaternionRel",
    "raiPath",
    "relPosY",
    "restingOn",
    "rgbNoise",
    "rigid",
    "rprop",
    "scalarProductXX",
    "scalarProductXY",
    "scalarProductXZ",
    "scalarProductYX",
    "scalarProductYY",
    "scalarProductYZ",
    "scalarProductZZ",
    "sdf",
    "setRaiPath",
    "singleSquaredPenalty",
    "sos",
    "sphere",
    "spline",
    "squaredPenalty",
    "ssBox",
    "ssBoxElip",
    "ssCvx",
    "ssCylinder",
    "stable",
    "stableOn",
    "stableOnX",
    "stableOnY",
    "stablePose",
    "stableRelPose",
    "stableYPhi",
    "stableZero",
    "standingAbove",
    "tau",
    "test",
    "topBoxGrasp",
    "topBoxPlace",
    "touch",
    "touchBoxNormalX",
    "touchBoxNormalY",
    "touchBoxNormalZ",
    "trans3",
    "transAccelerations",
    "transVelocities",
    "transX",
    "transXY",
    "transXYPhi",
    "transY",
    "transYPhi",
    "transZ",
    "universal",
    "vectorX",
    "vectorXDiff",
    "vectorXRel",
    "vectorY",
    "vectorYDiff",
    "vectorYRel",
    "vectorZ",
    "vectorZDiff",
    "vectorZRel",
    "velocity"
]


class ArgWord():
    """
    Members:

      _left

      _right

      _sequence

      _path
    """
    def __eq__(self, other: object) -> bool: ...
    def __getstate__(self) -> int: ...
    def __hash__(self) -> int: ...
    def __index__(self) -> int: ...
    def __init__(self, value: int) -> None: ...
    def __int__(self) -> int: ...
    def __ne__(self, other: object) -> bool: ...
    def __repr__(self) -> str: ...
    def __setstate__(self, state: int) -> None: ...
    @property
    def name(self) -> str:
        """
        :type: str
        """
    @property
    def value(self) -> int:
        """
        :type: int
        """
    __members__: dict # value = {'_left': <ArgWord._left: 0>, '_right': <ArgWord._right: 1>, '_sequence': <ArgWord._sequence: 2>, '_path': <ArgWord._path: 3>}
    _left: libry.ArgWord # value = <ArgWord._left: 0>
    _path: libry.ArgWord # value = <ArgWord._path: 3>
    _right: libry.ArgWord # value = <ArgWord._right: 1>
    _sequence: libry.ArgWord # value = <ArgWord._sequence: 2>
    pass
class BotOp():
    """
    needs some docu!
    """
    def __init__(self, C: Config, useRealRobot: bool) -> None: ...
    def getCameraFxypxy(self, sensorName: str) -> arr: 
        """
        returns camera intrinsics
        """
    def getImageAndDepth(self, sensorName: str) -> tuple: 
        """
        returns image and depth from a camera sensor
        """
    def getImageDepthPcl(self, sensorName: str, globalCoordinates: bool = False) -> tuple: 
        """
        returns image, depth and point cloud (assuming sensor knows intrinsics) from a camera sensor, optionally in global instead of camera-frame-relative coordinates
        """
    def getKeyPressed(self) -> int: 
        """
        get key pressed in window at last sync
        """
    def getTimeToEnd(self) -> float: 
        """
        get time-to-go of the current spline reference that is tracked (use getTimeToEnd()<=0. to check if motion execution is done)
        """
    def get_q(self) -> arr: 
        """
        get the current (real) robot joint vector
        """
    def get_qDot(self) -> arr: 
        """
        get the current (real) robot joint velocities
        """
    def get_qHome(self) -> arr: 
        """
        returns home joint vector (defined as the configuration C when you created BotOp)
        """
    def get_t(self) -> float: 
        """
        returns the control time (absolute time managed by the high freq tracking controller)
        """
    def get_tauExternal(self) -> arr: 
        """
        get the current (real) robot joint torques (external: gravity & acceleration removed) -- each call averages from last call; first call might return nonsense!
        """
    def gripperClose(self, leftRight: ArgWord, force: float = 10.0, width: float = 0.05, speed: float = 0.1) -> None: 
        """
        close gripper
        """
    def gripperCloseGrasp(self, leftRight: ArgWord, objName: str, force: float = 10.0, width: float = 0.05, speed: float = 0.1) -> None: 
        """
        close gripper and indicate what should be grasped -- makes no different in real, but helps simulation to mimic grasping more reliably
        """
    def gripperDone(self, leftRight: ArgWord) -> bool: 
        """
        returns if gripper is done
        """
    def gripperOpen(self, leftRight: ArgWord, width: float = 0.075, speed: float = 0.075) -> None: 
        """
        open gripper
        """
    def gripperPos(self, leftRight: ArgWord) -> float: 
        """
        returns the gripper pos
        """
    def hold(self, floating: bool = False, damping: bool = True) -> None: 
        """
        hold the robot with a trivial PD controller, floating means reference = real, without damping the robot is free floating
        """
    def home(self, C: Config) -> None: 
        """
        drive the robot home (which is defined as the configuration C when you created BotOp); keeps argument C synced
        """
    def move(self, path: arr, times: arr, overwrite: bool = False, overwriteCtrlTime: float = -1.0) -> None: 
        """
        core motion command: set a spline motion reference; if only a single time [T] is given for multiple waypoints, it assumes equal time spacing with TOTAL time T

        By default, the given spline is APPENDED to the current reference spline. The user can also enforce the given spline to overwrite the current reference starting at the given absolute ctrlTime. This allows implementation of reactive (e.g. MPC-style) control. However, the user needs to take care that overwriting is done in a smooth way, i.e., that the given spline starts with a pos/vel that is close to the pos/vel of the current reference at the given ctrlTime.
        """
    def moveAutoTimed(self, path: arr, maxVel: float = 1.0, maxAcc: float = 1.0) -> None: 
        """
        helper to execute a path (typically fine resolution, from KOMO or RRT) with equal time spacing chosen for given max vel/acc
        """
    def moveTo(self, q_target: arr, timeCost: float = 1.0, overwrite: bool = False) -> None: 
        """
        helper to move to a single joint vector target, where timing is chosen optimally based on the given timing cost

        When using overwrite, this immediately steers to the target -- use this as a well-timed reactive q_target controller
        """
    def setCompliance(self, J: arr, compliance: float = 0.5) -> None: 
        """
        set a task space compliant, where J defines the task space Jacobian, and compliance goes from 0 (no compliance) to 1 (full compliance, but still some damping)
        """
    def setControllerWriteData(self, arg0: int) -> None: 
        """
        [for internal debugging only] triggers writing control data into a file
        """
    def sync(self, C: Config, waitTime: float = 0.1) -> int: 
        """
        sync your workspace configuration C with the robot state
        """
    pass
class CameraView():
    def addSensor(self, name: str, frameAttached: str, width: int, height: int, focalLength: float = -1.0, orthoAbsHeight: float = -1.0, zRange: typing.List[float] = [], backgroundImageFile: str = '') -> None: ...
    def computeImageAndDepth(self, visualsOnly: bool = True) -> tuple: ...
    def computePointCloud(self, depth: numpy.ndarray, globalCoordinates: bool = True) -> numpy.ndarray[numpy.float64]: ...
    def computeSegmentation(self) -> numpy.ndarray[numpy.uint8]: ...
    def imageViewer(self) -> ImageViewer: ...
    def pointCloudViewer(self) -> PointCloudViewer: ...
    def segmentationViewer(self) -> ImageViewer: ...
    def selectSensor(self, name: str) -> None: ...
    def updateConfig(self, arg0: Config) -> None: ...
    pass
class CameraViewSensor():
    pass
class Config():
    """
    Core data structure to represent a kinematic configuration.
    """
    def __init__(self) -> None: 
        """
        initializes to an empty configuration, with no frames
        """
    def addConfigurationCopy(self, config: Config, tau: float = 1.0) -> None: ...
    def addFile(self, file_name: str) -> None: 
        """
        add the contents of the file to C
        """
    @staticmethod
    def addFrame(*args, **kwargs) -> typing.Any: 
        """
        add a new frame to C; optionally make this a child to the given parent; use the Frame methods to set properties of the new frame
        """
    @staticmethod
    def addObject(*args, **kwargs) -> typing.Any: 
        """
        TODO remove! use addFrame only
        """
    def attach(self, arg0: str, arg1: str) -> None: 
        """
        change the configuration by creating a rigid joint from frame1 to frame2, adopting their current relative pose. This also breaks the first joint that is parental to frame2 and reverses the topological order from frame2 to the broken joint
        """
    @staticmethod
    def cameraView(*args, **kwargs) -> typing.Any: 
        """
        create an offscreen renderer for this configuration
        """
    def clear(self) -> None: 
        """
        clear all frames and additional data; becomes the empty configuration, with no frames
        """
    def computeCollisions(self) -> None: 
        """
        call the broadphase collision engine (SWIFT++ or FCL) to generate the list of collisions (or near proximities) between all frame shapes that have the collision tag set non-zero
        """
    def copy(self, C2: Config) -> None: 
        """
        make C a (deep) copy of the given C2
        """
    def delFrame(self, frameName: str) -> None: 
        """
        destroy and remove a frame from C
        """
    def equationOfMotion(self, qdot: typing.List[float], gravity: bool) -> tuple: ...
    def eval(self, featureSymbol: FeatureSymbol, frames: StringA = [], scale: arr = array(1.e-05), target: arr = array(0.0078125), order: int = -1) -> tuple: 
        """
        evaluate a feature
        """
    def feature(self, featureSymbol: FeatureSymbol, frameNames: typing.List[str] = [], scale: typing.List[float] = [], target: typing.List[float] = [], order: int = -1) -> Feature: 
        """
        create a feature (a differentiable map from joint state to a vector space), as they're typically used for IK or optimization. See the dedicated tutorial for details. featureSymbol defines which mapping this is (position, vectors, collision distance, etc). many mapping refer to one or several frames, which need to be specified using frameNames
        """
    @staticmethod
    def frame(*args, **kwargs) -> typing.Any: 
        """
        get access to a frame by name; use the Frame methods to set/get frame properties
        """
    def frames(self) -> typing.List[rai::Frame]: ...
    def getCollisions(self, belowMargin: float = 1.0) -> list: 
        """
        return the results of collision computations: a list of 3 tuples with (frame1, frame2, distance). Optionally report only on distances below a margin To get really precise distances and penetrations use the FS.distance feature with the two frame names
        """
    def getDofIDs(self) -> typing.List[int]: ...
    @staticmethod
    def getFrame(*args, **kwargs) -> typing.Any: 
        """
        get access to a frame by name; use the Frame methods to set/get frame properties
        """
    def getFrameDimension(self) -> int: 
        """
        get the total number of frames
        """
    def getFrameNames(self) -> typing.List[str]: 
        """
        get the list of frame names
        """
    @typing.overload
    def getFrameState(self) -> numpy.ndarray[numpy.float64]: 
        """
        get the frame state as a n-times-7 numpy matrix, with a 7D pose per frame

        TODO remove -> use individual frame!
        """
    @typing.overload
    def getFrameState(self, arg0: str) -> numpy.ndarray[numpy.float64]: ...
    def getJointDimension(self) -> int: 
        """
        get the total number of degrees of freedom
        """
    def getJointNames(self) -> StringA: 
        """
        get the list of joint names
        """
    @staticmethod
    def getJointState(*args, **kwargs) -> typing.Any: 
        """
        get the joint state as a numpy vector, optionally only for a subset of joints specified as list of joint names
        """
    def makeObjectsConvex(self) -> None: 
        """
        remake all meshes associated with all frames to become their convex hull
        """
    def makeObjectsFree(self, arg0: typing.List[str]) -> None: 
        """
        TODO remove -> to frame
        """
    @staticmethod
    def report(*args, **kwargs) -> typing.Any: ...
    def selectJoints(self, jointNames: typing.List[str], notThose: bool = False) -> None: 
        """
        redefine what are considered the DOFs of this configuration: only joints listed in jointNames are considered part of the joint state and define the number of DOFs
        """
    def selectJointsByTag(self, jointGroups: typing.List[str]) -> None: 
        """
        redefine what are considered the DOFs of this configuration: only joint that have a tag listed in jointGroups are considered part of the joint state and define the number of DOFs
        """
    @typing.overload
    def setFrameState(self, X: typing.List[float], frames: typing.List[str] = []) -> None: 
        """
        set the frame state, optionally only for a subset of frames specified as list of frame names

        set the frame state, optionally only for a subset of frames specified as list of frame names
        """
    @typing.overload
    def setFrameState(self, X: numpy.ndarray, frames: typing.List[str] = []) -> None: ...
    def setJointState(self, q: arr, joints: list = []) -> None: 
        """
        set the joint state, optionally only for a subset of joints specified as list of joint names
        """
    def setJointStateSlice(self, arg0: typing.List[float], arg1: int) -> None: ...
    @staticmethod
    def simulation(*args, **kwargs) -> typing.Any: 
        """
        create a generic Simulation engine, which can internally call PhysX, Bullet, or just kinematics to forward simulate, allows you to control robot motors by position, velocity, or accelerations,     and allows you go query camera images and depth
        """
    def sortFrames(self) -> None: 
        """
        resort the internal order of frames according to the tree topology. This is important before saving the configuration.
        """
    def stepDynamics(self, qdot: typing.List[float], u_control: typing.List[float], tau: float, dynamicNoise: float, gravity: bool) -> numpy.ndarray[numpy.float64]: ...
    def view(self, pause: bool = False, message: str = None) -> int: 
        """
        open a view window for the configuration
        """
    def view_close(self) -> None: 
        """
        close the view
        """
    def view_getScreenshot(self) -> numpy.ndarray[numpy.uint8]: ...
    def view_playVideo(self, delay: float = 1.0, saveVideoPath: str = None) -> None: ...
    def view_recopyMeshes(self) -> None: ...
    def watchFile(self, arg0: str) -> None: 
        """
        launch a viewer that listents (inode) to changes of a file (made by you in an editor), and reloads, displays and animates the configuration whenever the file is changed
        """
    pass
class ConfigurationViewer():
    pass
class ControlMode():
    """
    Members:

      none

      position

      velocity

      acceleration

      spline
    """
    def __eq__(self, other: object) -> bool: ...
    def __getstate__(self) -> int: ...
    def __hash__(self) -> int: ...
    def __index__(self) -> int: ...
    def __init__(self, value: int) -> None: ...
    def __int__(self) -> int: ...
    def __ne__(self, other: object) -> bool: ...
    def __repr__(self) -> str: ...
    def __setstate__(self, state: int) -> None: ...
    @property
    def name(self) -> str:
        """
        :type: str
        """
    @property
    def value(self) -> int:
        """
        :type: int
        """
    __members__: dict # value = {'none': <ControlMode.none: 0>, 'position': <ControlMode.position: 1>, 'velocity': <ControlMode.velocity: 2>, 'acceleration': <ControlMode.acceleration: 3>, 'spline': <ControlMode.spline: 5>}
    acceleration: libry.ControlMode # value = <ControlMode.acceleration: 3>
    none: libry.ControlMode # value = <ControlMode.none: 0>
    position: libry.ControlMode # value = <ControlMode.position: 1>
    spline: libry.ControlMode # value = <ControlMode.spline: 5>
    velocity: libry.ControlMode # value = <ControlMode.velocity: 2>
    pass
class FS():
    """
    Members:

      position

      positionDiff

      positionRel

      quaternion

      quaternionDiff

      quaternionRel

      pose

      poseDiff

      poseRel

      vectorX

      vectorXDiff

      vectorXRel

      vectorY

      vectorYDiff

      vectorYRel

      vectorZ

      vectorZDiff

      vectorZRel

      scalarProductXX

      scalarProductXY

      scalarProductXZ

      scalarProductYX

      scalarProductYY

      scalarProductYZ

      scalarProductZZ

      gazeAt

      angularVel

      accumulatedCollisions

      jointLimits

      distance

      oppose

      qItself

      aboveBox

      insideBox

      pairCollision_negScalar

      pairCollision_vector

      pairCollision_normal

      pairCollision_p1

      pairCollision_p2

      standingAbove

      physics

      contactConstraints

      energy

      transAccelerations

      transVelocities
    """
    def __eq__(self, other: object) -> bool: ...
    def __getstate__(self) -> int: ...
    def __hash__(self) -> int: ...
    def __index__(self) -> int: ...
    def __init__(self, value: int) -> None: ...
    def __int__(self) -> int: ...
    def __ne__(self, other: object) -> bool: ...
    def __repr__(self) -> str: ...
    def __setstate__(self, state: int) -> None: ...
    @property
    def name(self) -> str:
        """
        :type: str
        """
    @property
    def value(self) -> int:
        """
        :type: int
        """
    __members__: dict # value = {'position': <FS.position: 0>, 'positionDiff': <FS.positionDiff: 1>, 'positionRel': <FS.positionRel: 2>, 'quaternion': <FS.quaternion: 3>, 'quaternionDiff': <FS.quaternionDiff: 4>, 'quaternionRel': <FS.quaternionRel: 5>, 'pose': <FS.pose: 6>, 'poseDiff': <FS.poseDiff: 7>, 'poseRel': <FS.poseRel: 8>, 'vectorX': <FS.vectorX: 9>, 'vectorXDiff': <FS.vectorXDiff: 10>, 'vectorXRel': <FS.vectorXRel: 11>, 'vectorY': <FS.vectorY: 12>, 'vectorYDiff': <FS.vectorYDiff: 13>, 'vectorYRel': <FS.vectorYRel: 14>, 'vectorZ': <FS.vectorZ: 15>, 'vectorZDiff': <FS.vectorZDiff: 16>, 'vectorZRel': <FS.vectorZRel: 17>, 'scalarProductXX': <FS.scalarProductXX: 18>, 'scalarProductXY': <FS.scalarProductXY: 19>, 'scalarProductXZ': <FS.scalarProductXZ: 20>, 'scalarProductYX': <FS.scalarProductYX: 21>, 'scalarProductYY': <FS.scalarProductYY: 22>, 'scalarProductYZ': <FS.scalarProductYZ: 23>, 'scalarProductZZ': <FS.scalarProductZZ: 24>, 'gazeAt': <FS.gazeAt: 25>, 'angularVel': <FS.angularVel: 26>, 'accumulatedCollisions': <FS.accumulatedCollisions: 27>, 'jointLimits': <FS.jointLimits: 28>, 'distance': <FS.distance: 29>, 'oppose': <FS.oppose: 30>, 'qItself': <FS.qItself: 31>, 'aboveBox': <FS.aboveBox: 33>, 'insideBox': <FS.insideBox: 34>, 'pairCollision_negScalar': <FS.pairCollision_negScalar: 35>, 'pairCollision_vector': <FS.pairCollision_vector: 36>, 'pairCollision_normal': <FS.pairCollision_normal: 37>, 'pairCollision_p1': <FS.pairCollision_p1: 38>, 'pairCollision_p2': <FS.pairCollision_p2: 39>, 'standingAbove': <FS.standingAbove: 40>, 'physics': <FS.physics: 41>, 'contactConstraints': <FS.contactConstraints: 42>, 'energy': <FS.energy: 43>, 'transAccelerations': <FS.transAccelerations: 44>, 'transVelocities': <FS.transVelocities: 45>}
    aboveBox: libry.FS # value = <FS.aboveBox: 33>
    accumulatedCollisions: libry.FS # value = <FS.accumulatedCollisions: 27>
    angularVel: libry.FS # value = <FS.angularVel: 26>
    contactConstraints: libry.FS # value = <FS.contactConstraints: 42>
    distance: libry.FS # value = <FS.distance: 29>
    energy: libry.FS # value = <FS.energy: 43>
    gazeAt: libry.FS # value = <FS.gazeAt: 25>
    insideBox: libry.FS # value = <FS.insideBox: 34>
    jointLimits: libry.FS # value = <FS.jointLimits: 28>
    oppose: libry.FS # value = <FS.oppose: 30>
    pairCollision_negScalar: libry.FS # value = <FS.pairCollision_negScalar: 35>
    pairCollision_normal: libry.FS # value = <FS.pairCollision_normal: 37>
    pairCollision_p1: libry.FS # value = <FS.pairCollision_p1: 38>
    pairCollision_p2: libry.FS # value = <FS.pairCollision_p2: 39>
    pairCollision_vector: libry.FS # value = <FS.pairCollision_vector: 36>
    physics: libry.FS # value = <FS.physics: 41>
    pose: libry.FS # value = <FS.pose: 6>
    poseDiff: libry.FS # value = <FS.poseDiff: 7>
    poseRel: libry.FS # value = <FS.poseRel: 8>
    position: libry.FS # value = <FS.position: 0>
    positionDiff: libry.FS # value = <FS.positionDiff: 1>
    positionRel: libry.FS # value = <FS.positionRel: 2>
    qItself: libry.FS # value = <FS.qItself: 31>
    quaternion: libry.FS # value = <FS.quaternion: 3>
    quaternionDiff: libry.FS # value = <FS.quaternionDiff: 4>
    quaternionRel: libry.FS # value = <FS.quaternionRel: 5>
    scalarProductXX: libry.FS # value = <FS.scalarProductXX: 18>
    scalarProductXY: libry.FS # value = <FS.scalarProductXY: 19>
    scalarProductXZ: libry.FS # value = <FS.scalarProductXZ: 20>
    scalarProductYX: libry.FS # value = <FS.scalarProductYX: 21>
    scalarProductYY: libry.FS # value = <FS.scalarProductYY: 22>
    scalarProductYZ: libry.FS # value = <FS.scalarProductYZ: 23>
    scalarProductZZ: libry.FS # value = <FS.scalarProductZZ: 24>
    standingAbove: libry.FS # value = <FS.standingAbove: 40>
    transAccelerations: libry.FS # value = <FS.transAccelerations: 44>
    transVelocities: libry.FS # value = <FS.transVelocities: 45>
    vectorX: libry.FS # value = <FS.vectorX: 9>
    vectorXDiff: libry.FS # value = <FS.vectorXDiff: 10>
    vectorXRel: libry.FS # value = <FS.vectorXRel: 11>
    vectorY: libry.FS # value = <FS.vectorY: 12>
    vectorYDiff: libry.FS # value = <FS.vectorYDiff: 13>
    vectorYRel: libry.FS # value = <FS.vectorYRel: 14>
    vectorZ: libry.FS # value = <FS.vectorZ: 15>
    vectorZDiff: libry.FS # value = <FS.vectorZDiff: 16>
    vectorZRel: libry.FS # value = <FS.vectorZRel: 17>
    pass
class Feature():
    """
    todo doc
    """
    def description(self, arg0: Config) -> str: ...
    def eval(self, arg0: Config) -> tuple: ...
    def setOrder(self, arg0: int) -> Feature: ...
    def setScale(self, arg0: arr) -> Feature: ...
    def setTarget(self, arg0: arr) -> Feature: ...
    pass
class Frame():
    """
    todo doc
    """
    def addAttribute(self, arg0: str, arg1: float) -> Frame: ...
    def addAttributes(self, arg0: dict) -> None: 
        """
        add/set attributes for the frame
        """
    def getAttributes(self) -> dict: 
        """
        get frame attributes
        """
    def getJointState(self) -> arr: ...
    def getMeshPoints(self) -> arr: ...
    @staticmethod
    def getMeshTriangles(*args, **kwargs) -> typing.Any: ...
    def getPosition(self) -> arr: ...
    def getQuaternion(self) -> arr: ...
    def getRelativePosition(self) -> arr: ...
    def getRelativeQuaternion(self) -> arr: ...
    def getRotationMatrix(self) -> arr: ...
    def getSize(self) -> arr: ...
    def info(self) -> dict: ...
    def setColor(self, arg0: arr) -> Frame: ...
    def setContact(self, arg0: int) -> Frame: ...
    @staticmethod
    def setJoint(*args, **kwargs) -> typing.Any: ...
    def setJointState(self, arg0: arr) -> Frame: ...
    def setMass(self, arg0: float) -> Frame: ...
    def setMeshAsLines(self, arg0: typing.List[float]) -> None: ...
    def setParent(self, arg0: Frame, arg1: bool, arg2: bool) -> Frame: ...
    def setPointCloud(self, points: numpy.ndarray, colors: numpy.ndarray[numpy.uint8] = array([], dtype=uint8)) -> None: ...
    def setPose(self, arg0: str) -> None: ...
    def setPosition(self, arg0: arr) -> Frame: ...
    def setQuaternion(self, arg0: arr) -> Frame: ...
    def setRelativePose(self, arg0: str) -> None: ...
    def setRelativePosition(self, arg0: arr) -> Frame: ...
    def setRelativeQuaternion(self, arg0: arr) -> Frame: ...
    def setShape(self, type: ST, size: arr) -> Frame: ...
    def unLink(self) -> Frame: ...
    @property
    def name(self) -> rai::String:
        """
        :type: rai::String
        """
    @name.setter
    def name(self, arg0: rai::String) -> None:
        pass
    pass
class ImageViewer():
    pass
class ImpType():
    """
    Members:

      closeGripper

      openGripper

      depthNoise

      rgbNoise

      adversarialDropper

      objectImpulses

      noPenetrations
    """
    def __eq__(self, other: object) -> bool: ...
    def __getstate__(self) -> int: ...
    def __hash__(self) -> int: ...
    def __index__(self) -> int: ...
    def __init__(self, value: int) -> None: ...
    def __int__(self) -> int: ...
    def __ne__(self, other: object) -> bool: ...
    def __repr__(self) -> str: ...
    def __setstate__(self, state: int) -> None: ...
    @property
    def name(self) -> str:
        """
        :type: str
        """
    @property
    def value(self) -> int:
        """
        :type: int
        """
    __members__: dict # value = {'closeGripper': <ImpType.closeGripper: 0>, 'openGripper': <ImpType.openGripper: 1>, 'depthNoise': <ImpType.depthNoise: 2>, 'rgbNoise': <ImpType.rgbNoise: 3>, 'adversarialDropper': <ImpType.adversarialDropper: 4>, 'objectImpulses': <ImpType.objectImpulses: 5>, 'noPenetrations': <ImpType.noPenetrations: 7>}
    adversarialDropper: libry.ImpType # value = <ImpType.adversarialDropper: 4>
    closeGripper: libry.ImpType # value = <ImpType.closeGripper: 0>
    depthNoise: libry.ImpType # value = <ImpType.depthNoise: 2>
    noPenetrations: libry.ImpType # value = <ImpType.noPenetrations: 7>
    objectImpulses: libry.ImpType # value = <ImpType.objectImpulses: 5>
    openGripper: libry.ImpType # value = <ImpType.openGripper: 1>
    rgbNoise: libry.ImpType # value = <ImpType.rgbNoise: 3>
    pass
class JT():
    """
    Members:

      hingeX

      hingeY

      hingeZ

      transX

      transY

      transZ

      transXY

      trans3

      transXYPhi

      transYPhi

      universal

      rigid

      quatBall

      phiTransXY

      XBall

      free

      generic

      tau
    """
    def __eq__(self, other: object) -> bool: ...
    def __getstate__(self) -> int: ...
    def __hash__(self) -> int: ...
    def __index__(self) -> int: ...
    def __init__(self, value: int) -> None: ...
    def __int__(self) -> int: ...
    def __ne__(self, other: object) -> bool: ...
    def __repr__(self) -> str: ...
    def __setstate__(self, state: int) -> None: ...
    @property
    def name(self) -> str:
        """
        :type: str
        """
    @property
    def value(self) -> int:
        """
        :type: int
        """
    XBall: libry.JT # value = <JT.XBall: 15>
    __members__: dict # value = {'hingeX': <JT.hingeX: 1>, 'hingeY': <JT.hingeY: 2>, 'hingeZ': <JT.hingeZ: 3>, 'transX': <JT.transX: 4>, 'transY': <JT.transY: 5>, 'transZ': <JT.transZ: 6>, 'transXY': <JT.transXY: 7>, 'trans3': <JT.trans3: 8>, 'transXYPhi': <JT.transXYPhi: 9>, 'transYPhi': <JT.transYPhi: 10>, 'universal': <JT.universal: 11>, 'rigid': <JT.rigid: 12>, 'quatBall': <JT.quatBall: 13>, 'phiTransXY': <JT.phiTransXY: 14>, 'XBall': <JT.XBall: 15>, 'free': <JT.free: 16>, 'generic': <JT.generic: 17>, 'tau': <JT.tau: 18>}
    free: libry.JT # value = <JT.free: 16>
    generic: libry.JT # value = <JT.generic: 17>
    hingeX: libry.JT # value = <JT.hingeX: 1>
    hingeY: libry.JT # value = <JT.hingeY: 2>
    hingeZ: libry.JT # value = <JT.hingeZ: 3>
    phiTransXY: libry.JT # value = <JT.phiTransXY: 14>
    quatBall: libry.JT # value = <JT.quatBall: 13>
    rigid: libry.JT # value = <JT.rigid: 12>
    tau: libry.JT # value = <JT.tau: 18>
    trans3: libry.JT # value = <JT.trans3: 8>
    transX: libry.JT # value = <JT.transX: 4>
    transXY: libry.JT # value = <JT.transXY: 7>
    transXYPhi: libry.JT # value = <JT.transXYPhi: 9>
    transY: libry.JT # value = <JT.transY: 5>
    transYPhi: libry.JT # value = <JT.transYPhi: 10>
    transZ: libry.JT # value = <JT.transZ: 6>
    universal: libry.JT # value = <JT.universal: 11>
    pass
class KOMO():
    """
    Constrained solver to optimize configurations or paths. (KOMO = k-order Markov Optimization)
    """
    def __init__(self) -> None: ...
    def addControlObjective(self, times: arr, order: int, scale: float = 1.0, target: arr = array(0.0078125), deltaFromStep: int = 0, deltaToStep: int = 0) -> Objective: ...
    @staticmethod
    def addInteraction_elasticBounce(*args, **kwargs) -> typing.Any: ...
    @staticmethod
    def addModeSwitch(*args, **kwargs) -> typing.Any: ...
    @staticmethod
    def addObjective(*args, **kwargs) -> typing.Any: ...
    def addQuaternionNorms(self, times: arr = array(0.0078125), scale: float = 3.0, hard: bool = True) -> None: ...
    def addTimeOptimization(self) -> None: ...
    def clearObjectives(self) -> None: ...
    def getConstraintViolations(self) -> float: ...
    def getCosts(self) -> float: ...
    def getForceInteractions(self) -> list: ...
    def getFrameState(self, arg0: int) -> arr: ...
    def getPath(self) -> arr: ...
    def getPathFrames(self) -> arr: ...
    def getPathTau(self) -> arr: ...
    def getPath_qAll(self) -> arrA: ...
    def getReport(self) -> dict: ...
    def getT(self) -> int: ...
    def initOrg(self) -> None: ...
    @staticmethod
    def initPhaseWithDofsPath(*args, **kwargs) -> typing.Any: ...
    def initRandom(self, verbose: int = 0) -> None: ...
    def initWithConstant(self, q: arr) -> None: ...
    def initWithPath_qOrg(self, q: arr) -> None: ...
    @staticmethod
    def initWithWaypoints(*args, **kwargs) -> typing.Any: ...
    def nlp(self) -> NLP: 
        """
        return the problem NLP
        """
    def reportProblem(self) -> str: ...
    def setConfig(self, arg0: Config, arg1: bool) -> None: ...
    def setTiming(self, arg0: float, arg1: int, arg2: float, arg3: int) -> None: ...
    def view(self, pause: bool = False, txt: str = None) -> int: ...
    def view_close(self) -> None: ...
    def view_play(self, pause: bool = False, delay: float = 0.1, saveVideoPath: str = None) -> int: ...
    pass
class KOMO_Objective():
    pass
class NLP():
    """
    Representation of a Nonlinear Mathematical Program
    """
    def evaluate(self, arg0: arr) -> typing.Tuple[arr, arr]: 
        """
        query the NLP at a point $x$; returns the tuple $(phi,J)$, which is the feature vector and its Jacobian; features define cost terms, sum-of-square (sos) terms, inequalities, and equalities depending on 'getFeatureTypes'
        """
    def getBounds(self) -> typing.Tuple[arr, arr]: 
        """
        returns the tuple $(b_{lo},b_{up})$, where both vectors are of same dimensionality of $x$ (or size zero, if there are no bounds)
        """
    def getDimension(self) -> int: 
        """
        return the dimensionality of $x$
        """
    def getFHessian(self, arg0: arr) -> arr: 
        """
        returns Hessian of the sum of $f$-terms
        """
    def getFeatureTypes(self) -> typing.List[ObjectiveType]: ...
    def getInitializationSample(self, previousOptima: arr = array(0.0078125)) -> arr: 
        """
        returns a sample (e.g. uniform within bounds) to initialize an optimization -- not necessarily feasible
        """
    def report(self, arg0: int) -> str: 
        """
        displays semantic information on the last query
        """
    pass
class NLP_Factory(NLP):
    def __init__(self) -> None: ...
    def setBounds(self, arg0: arr, arg1: arr) -> None: ...
    def setDimension(self, arg0: int) -> None: ...
    def setEvalCallback(self, arg0: typing.Callable[[arr], typing.Tuple[arr, arr]]) -> None: ...
    @staticmethod
    def setFeatureTypes(*args, **kwargs) -> typing.Any: ...
    def testCallingEvalCallback(self, arg0: arr) -> typing.Tuple[arr, arr]: ...
    pass
class NLP_Solver():
    """
    An interface to portfolio of solvers
    """
    def __init__(self) -> None: ...
    def getOptions(self) -> NLP_SolverOptions: ...
    def getTrace_J(self) -> arr: ...
    def getTrace_costs(self) -> arr: ...
    def getTrace_phi(self) -> arr: ...
    def getTrace_x(self) -> arr: ...
    def setOptions(self, verbose: int = 1, stopTolerance: float = 0.01, stopFTolerance: float = -1.0, stopGTolerance: float = -1.0, stopEvals: int = 1000, maxStep: float = 0.2, damping: float = 1.0, stepInc: float = 1.5, stepDec: float = 0.5, wolfe: float = 0.01, muInit: float = 1.0, muInc: float = 5.0, muMax: float = 10000.0, muLBInit: float = 0.1, muLBDec: float = 0.2) -> NLP_Solver: 
        """
        set solver options
        """
    def setProblem(self, arg0: NLP) -> NLP_Solver: ...
    def setSolver(self, arg0: NLP_SolverID) -> NLP_Solver: ...
    def setTracing(self, arg0: bool, arg1: bool, arg2: bool, arg3: bool) -> NLP_Solver: ...
    def solve(self, resampleInitialization: int = -1) -> SolverReturn: ...
    pass
class NLP_SolverID():
    """
    Members:

      gradientDescent

      rprop

      LBFGS

      newton

      augmentedLag

      squaredPenalty

      logBarrier

      singleSquaredPenalty

      NLopt

      Ipopt

      Ceres
    """
    def __eq__(self, other: object) -> bool: ...
    def __getstate__(self) -> int: ...
    def __hash__(self) -> int: ...
    def __index__(self) -> int: ...
    def __init__(self, value: int) -> None: ...
    def __int__(self) -> int: ...
    def __ne__(self, other: object) -> bool: ...
    def __repr__(self) -> str: ...
    def __setstate__(self, state: int) -> None: ...
    @property
    def name(self) -> str:
        """
        :type: str
        """
    @property
    def value(self) -> int:
        """
        :type: int
        """
    Ceres: libry.NLP_SolverID # value = <NLP_SolverID.Ceres: 10>
    Ipopt: libry.NLP_SolverID # value = <NLP_SolverID.Ipopt: 9>
    LBFGS: libry.NLP_SolverID # value = <NLP_SolverID.LBFGS: 2>
    NLopt: libry.NLP_SolverID # value = <NLP_SolverID.NLopt: 8>
    __members__: dict # value = {'gradientDescent': <NLP_SolverID.gradientDescent: 0>, 'rprop': <NLP_SolverID.rprop: 1>, 'LBFGS': <NLP_SolverID.LBFGS: 2>, 'newton': <NLP_SolverID.newton: 3>, 'augmentedLag': <NLP_SolverID.augmentedLag: 4>, 'squaredPenalty': <NLP_SolverID.squaredPenalty: 5>, 'logBarrier': <NLP_SolverID.logBarrier: 6>, 'singleSquaredPenalty': <NLP_SolverID.singleSquaredPenalty: 7>, 'NLopt': <NLP_SolverID.NLopt: 8>, 'Ipopt': <NLP_SolverID.Ipopt: 9>, 'Ceres': <NLP_SolverID.Ceres: 10>}
    augmentedLag: libry.NLP_SolverID # value = <NLP_SolverID.augmentedLag: 4>
    gradientDescent: libry.NLP_SolverID # value = <NLP_SolverID.gradientDescent: 0>
    logBarrier: libry.NLP_SolverID # value = <NLP_SolverID.logBarrier: 6>
    newton: libry.NLP_SolverID # value = <NLP_SolverID.newton: 3>
    rprop: libry.NLP_SolverID # value = <NLP_SolverID.rprop: 1>
    singleSquaredPenalty: libry.NLP_SolverID # value = <NLP_SolverID.singleSquaredPenalty: 7>
    squaredPenalty: libry.NLP_SolverID # value = <NLP_SolverID.squaredPenalty: 5>
    pass
class NLP_SolverOptions():
    """
    solver options
    """
    def __init__(self) -> None: ...
    def dict(self) -> dict: ...
    def set_damping(self, arg0: float) -> NLP_SolverOptions: ...
    def set_maxStep(self, arg0: float) -> NLP_SolverOptions: ...
    def set_muInc(self, arg0: float) -> NLP_SolverOptions: ...
    def set_muInit(self, arg0: float) -> NLP_SolverOptions: ...
    def set_muLBDec(self, arg0: float) -> NLP_SolverOptions: ...
    def set_muLBInit(self, arg0: float) -> NLP_SolverOptions: ...
    def set_muMax(self, arg0: float) -> NLP_SolverOptions: ...
    def set_stepDec(self, arg0: float) -> NLP_SolverOptions: ...
    def set_stepInc(self, arg0: float) -> NLP_SolverOptions: ...
    def set_stopEvals(self, arg0: int) -> NLP_SolverOptions: ...
    def set_stopFTolerance(self, arg0: float) -> NLP_SolverOptions: ...
    def set_stopGTolerance(self, arg0: float) -> NLP_SolverOptions: ...
    def set_stopTolerance(self, arg0: float) -> NLP_SolverOptions: ...
    def set_verbose(self, arg0: int) -> NLP_SolverOptions: ...
    def set_wolfe(self, arg0: float) -> NLP_SolverOptions: ...
    pass
class OT():
    """
    Members:

      none

      f

      sos

      ineq

      eq

      ineqB

      ineqP
    """
    def __eq__(self, other: object) -> bool: ...
    def __getstate__(self) -> int: ...
    def __hash__(self) -> int: ...
    def __index__(self) -> int: ...
    def __init__(self, value: int) -> None: ...
    def __int__(self) -> int: ...
    def __ne__(self, other: object) -> bool: ...
    def __repr__(self) -> str: ...
    def __setstate__(self, state: int) -> None: ...
    @property
    def name(self) -> str:
        """
        :type: str
        """
    @property
    def value(self) -> int:
        """
        :type: int
        """
    __members__: dict # value = {'none': <OT.none: 0>, 'f': <OT.f: 1>, 'sos': <OT.sos: 2>, 'ineq': <OT.ineq: 3>, 'eq': <OT.eq: 4>, 'ineqB': <OT.ineqB: 5>, 'ineqP': <OT.ineqP: 6>}
    eq: libry.OT # value = <OT.eq: 4>
    f: libry.OT # value = <OT.f: 1>
    ineq: libry.OT # value = <OT.ineq: 3>
    ineqB: libry.OT # value = <OT.ineqB: 5>
    ineqP: libry.OT # value = <OT.ineqP: 6>
    none: libry.OT # value = <OT.none: 0>
    sos: libry.OT # value = <OT.sos: 2>
    pass
class OptBench_Skeleton_Handover():
    def __init__(self, arg0: ArgWord) -> None: ...
    def get(self) -> NLP: ...
    pass
class OptBench_Skeleton_Pick():
    def __init__(self, arg0: ArgWord) -> None: ...
    def get(self) -> NLP: ...
    pass
class OptBench_Skeleton_StackAndBalance():
    def __init__(self, arg0: ArgWord) -> None: ...
    def get(self) -> NLP: ...
    pass
class OptBenchmark_InvKin_Endeff():
    def __init__(self, arg0: str, arg1: bool) -> None: ...
    def get(self) -> NLP: ...
    pass
class PathFinder():
    """
    todo doc
    """
    def __init__(self) -> None: ...
    def setExplicitCollisionPairs(self, collisionPairs: StringA) -> PathFinder: ...
    def setProblem(self, Configuration: Config, starts: arr, goals: arr) -> PathFinder: ...
    def solve(self) -> SolverReturn: ...
    def step(self) -> bool: ...
    pass
class PointCloudViewer():
    pass
class ST():
    """
    Members:

      none

      box

      sphere

      capsule

      mesh

      cylinder

      marker

      pointCloud

      ssCvx

      ssBox

      ssCylinder

      ssBoxElip

      quad

      camera

      sdf
    """
    def __eq__(self, other: object) -> bool: ...
    def __getstate__(self) -> int: ...
    def __hash__(self) -> int: ...
    def __index__(self) -> int: ...
    def __init__(self, value: int) -> None: ...
    def __int__(self) -> int: ...
    def __ne__(self, other: object) -> bool: ...
    def __repr__(self) -> str: ...
    def __setstate__(self, state: int) -> None: ...
    @property
    def name(self) -> str:
        """
        :type: str
        """
    @property
    def value(self) -> int:
        """
        :type: int
        """
    __members__: dict # value = {'none': <ST.none: -1>, 'box': <ST.box: 0>, 'sphere': <ST.sphere: 1>, 'capsule': <ST.capsule: 2>, 'mesh': <ST.mesh: 3>, 'cylinder': <ST.cylinder: 4>, 'marker': <ST.marker: 5>, 'pointCloud': <ST.pointCloud: 6>, 'ssCvx': <ST.ssCvx: 7>, 'ssBox': <ST.ssBox: 8>, 'ssCylinder': <ST.ssCylinder: 9>, 'ssBoxElip': <ST.ssBoxElip: 10>, 'quad': <ST.quad: 11>, 'camera': <ST.camera: 12>, 'sdf': <ST.sdf: 13>}
    box: libry.ST # value = <ST.box: 0>
    camera: libry.ST # value = <ST.camera: 12>
    capsule: libry.ST # value = <ST.capsule: 2>
    cylinder: libry.ST # value = <ST.cylinder: 4>
    marker: libry.ST # value = <ST.marker: 5>
    mesh: libry.ST # value = <ST.mesh: 3>
    none: libry.ST # value = <ST.none: -1>
    pointCloud: libry.ST # value = <ST.pointCloud: 6>
    quad: libry.ST # value = <ST.quad: 11>
    sdf: libry.ST # value = <ST.sdf: 13>
    sphere: libry.ST # value = <ST.sphere: 1>
    ssBox: libry.ST # value = <ST.ssBox: 8>
    ssBoxElip: libry.ST # value = <ST.ssBoxElip: 10>
    ssCvx: libry.ST # value = <ST.ssCvx: 7>
    ssCylinder: libry.ST # value = <ST.ssCylinder: 9>
    pass
class SY():
    """
    Members:

      touch

      above

      inside

      oppose

      restingOn

      poseEq

      positionEq

      stableRelPose

      stablePose

      stable

      stableOn

      dynamic

      dynamicOn

      dynamicTrans

      quasiStatic

      quasiStaticOn

      downUp

      break

      stableZero

      contact

      contactStick

      contactComplementary

      bounce

      push

      magic

      magicTrans

      pushAndPlace

      topBoxGrasp

      topBoxPlace

      dampMotion

      identical

      alignByInt

      makeFree

      forceBalance

      relPosY

      touchBoxNormalX

      touchBoxNormalY

      touchBoxNormalZ

      boxGraspX

      boxGraspY

      boxGraspZ

      lift

      stableYPhi

      stableOnX

      stableOnY

      end
    """
    def __eq__(self, other: object) -> bool: ...
    def __getstate__(self) -> int: ...
    def __hash__(self) -> int: ...
    def __index__(self) -> int: ...
    def __init__(self, value: int) -> None: ...
    def __int__(self) -> int: ...
    def __ne__(self, other: object) -> bool: ...
    def __repr__(self) -> str: ...
    def __setstate__(self, state: int) -> None: ...
    @property
    def name(self) -> str:
        """
        :type: str
        """
    @property
    def value(self) -> int:
        """
        :type: int
        """
    __members__: dict # value = {'touch': <SY.touch: 0>, 'above': <SY.above: 1>, 'inside': <SY.inside: 2>, 'oppose': <SY.oppose: 3>, 'restingOn': <SY.restingOn: 4>, 'poseEq': <SY.poseEq: 5>, 'positionEq': <SY.positionEq: 6>, 'stableRelPose': <SY.stableRelPose: 7>, 'stablePose': <SY.stablePose: 8>, 'stable': <SY.stable: 9>, 'stableOn': <SY.stableOn: 10>, 'dynamic': <SY.dynamic: 11>, 'dynamicOn': <SY.dynamicOn: 12>, 'dynamicTrans': <SY.dynamicTrans: 13>, 'quasiStatic': <SY.quasiStatic: 14>, 'quasiStaticOn': <SY.quasiStaticOn: 15>, 'downUp': <SY.downUp: 16>, 'break': <SY.break: 17>, 'stableZero': <SY.stableZero: 18>, 'contact': <SY.contact: 19>, 'contactStick': <SY.contactStick: 20>, 'contactComplementary': <SY.contactComplementary: 21>, 'bounce': <SY.bounce: 22>, 'push': <SY.push: 23>, 'magic': <SY.magic: 24>, 'magicTrans': <SY.magicTrans: 25>, 'pushAndPlace': <SY.pushAndPlace: 26>, 'topBoxGrasp': <SY.topBoxGrasp: 27>, 'topBoxPlace': <SY.topBoxPlace: 28>, 'dampMotion': <SY.dampMotion: 29>, 'identical': <SY.identical: 30>, 'alignByInt': <SY.alignByInt: 31>, 'makeFree': <SY.makeFree: 32>, 'forceBalance': <SY.forceBalance: 33>, 'relPosY': <SY.relPosY: 34>, 'touchBoxNormalX': <SY.touchBoxNormalX: 35>, 'touchBoxNormalY': <SY.touchBoxNormalY: 36>, 'touchBoxNormalZ': <SY.touchBoxNormalZ: 37>, 'boxGraspX': <SY.boxGraspX: 38>, 'boxGraspY': <SY.boxGraspY: 39>, 'boxGraspZ': <SY.boxGraspZ: 40>, 'lift': <SY.lift: 41>, 'stableYPhi': <SY.stableYPhi: 42>, 'stableOnX': <SY.stableOnX: 43>, 'stableOnY': <SY.stableOnY: 44>, 'end': <SY.end: 46>}
    above: libry.SY # value = <SY.above: 1>
    alignByInt: libry.SY # value = <SY.alignByInt: 31>
    bounce: libry.SY # value = <SY.bounce: 22>
    boxGraspX: libry.SY # value = <SY.boxGraspX: 38>
    boxGraspY: libry.SY # value = <SY.boxGraspY: 39>
    boxGraspZ: libry.SY # value = <SY.boxGraspZ: 40>
    break: libry.SY # value = <SY.break: 17>
    contact: libry.SY # value = <SY.contact: 19>
    contactComplementary: libry.SY # value = <SY.contactComplementary: 21>
    contactStick: libry.SY # value = <SY.contactStick: 20>
    dampMotion: libry.SY # value = <SY.dampMotion: 29>
    downUp: libry.SY # value = <SY.downUp: 16>
    dynamic: libry.SY # value = <SY.dynamic: 11>
    dynamicOn: libry.SY # value = <SY.dynamicOn: 12>
    dynamicTrans: libry.SY # value = <SY.dynamicTrans: 13>
    end: libry.SY # value = <SY.end: 46>
    forceBalance: libry.SY # value = <SY.forceBalance: 33>
    identical: libry.SY # value = <SY.identical: 30>
    inside: libry.SY # value = <SY.inside: 2>
    lift: libry.SY # value = <SY.lift: 41>
    magic: libry.SY # value = <SY.magic: 24>
    magicTrans: libry.SY # value = <SY.magicTrans: 25>
    makeFree: libry.SY # value = <SY.makeFree: 32>
    oppose: libry.SY # value = <SY.oppose: 3>
    poseEq: libry.SY # value = <SY.poseEq: 5>
    positionEq: libry.SY # value = <SY.positionEq: 6>
    push: libry.SY # value = <SY.push: 23>
    pushAndPlace: libry.SY # value = <SY.pushAndPlace: 26>
    quasiStatic: libry.SY # value = <SY.quasiStatic: 14>
    quasiStaticOn: libry.SY # value = <SY.quasiStaticOn: 15>
    relPosY: libry.SY # value = <SY.relPosY: 34>
    restingOn: libry.SY # value = <SY.restingOn: 4>
    stable: libry.SY # value = <SY.stable: 9>
    stableOn: libry.SY # value = <SY.stableOn: 10>
    stableOnX: libry.SY # value = <SY.stableOnX: 43>
    stableOnY: libry.SY # value = <SY.stableOnY: 44>
    stablePose: libry.SY # value = <SY.stablePose: 8>
    stableRelPose: libry.SY # value = <SY.stableRelPose: 7>
    stableYPhi: libry.SY # value = <SY.stableYPhi: 42>
    stableZero: libry.SY # value = <SY.stableZero: 18>
    topBoxGrasp: libry.SY # value = <SY.topBoxGrasp: 27>
    topBoxPlace: libry.SY # value = <SY.topBoxPlace: 28>
    touch: libry.SY # value = <SY.touch: 0>
    touchBoxNormalX: libry.SY # value = <SY.touchBoxNormalX: 35>
    touchBoxNormalY: libry.SY # value = <SY.touchBoxNormalY: 36>
    touchBoxNormalZ: libry.SY # value = <SY.touchBoxNormalZ: 37>
    pass
class Simulation():
    """
    todo doc
    """
    def __init__(self, arg0: Config, arg1: SimulationEngine, arg2: int) -> None: ...
    def addImp(self, arg0: ImpType, arg1: StringA, arg2: arr) -> None: ...
    @staticmethod
    def addSensor(*args, **kwargs) -> typing.Any: ...
    def closeGripper(self, gripperFrameName: str, width: float = 0.05, speed: float = 0.3, force: float = 20.0) -> None: ...
    def depthData2pointCloud(self, arg0: numpy.ndarray[numpy.float32], arg1: typing.List[float]) -> numpy.ndarray[numpy.float64]: ...
    def getGripperIsGrasping(self, gripperFrameName: str) -> bool: ...
    def getGripperWidth(self, gripperFrameName: str) -> float: ...
    def getGroundTruthPosition(self, arg0: str) -> numpy.ndarray[numpy.float64]: ...
    def getGroundTruthRotationMatrix(self, arg0: str) -> numpy.ndarray[numpy.float64]: ...
    def getGroundTruthSize(self, arg0: str) -> numpy.ndarray[numpy.float64]: ...
    def getImageAndDepth(self) -> tuple: ...
    @staticmethod
    def getScreenshot(*args, **kwargs) -> typing.Any: ...
    def getState(self) -> tuple: ...
    def getTimeToMove(self) -> float: ...
    def get_q(self) -> arr: ...
    def get_qDot(self) -> arr: ...
    def loadTeleopCallbacks(self) -> None: ...
    def openGripper(self, gripperFrameName: str, width: float = 0.075, speed: float = 0.3) -> None: ...
    def pushConfigurationToSimulator(self, frameVelocities: arr = []) -> None: 
        """
        set the simulator to the full (frame) state of the configuration
        """
    @staticmethod
    def restoreState(*args, **kwargs) -> typing.Any: ...
    @staticmethod
    def selectSensor(*args, **kwargs) -> typing.Any: ...
    def setMoveto(self, path: arr, t: float, append: bool = True) -> None: 
        """
        set the spline reference to genreate motion
        """
    def setState(self, frameState: arr, frameVelocities: arr = []) -> None: ...
    def step(self, u_control: arr, tau: float = 0.01, u_mode: ControlMode = ControlMode.velocity) -> None: ...
    pass
class SimulationEngine():
    """
    Members:

      physx

      bullet

      kinematic
    """
    def __eq__(self, other: object) -> bool: ...
    def __getstate__(self) -> int: ...
    def __hash__(self) -> int: ...
    def __index__(self) -> int: ...
    def __init__(self, value: int) -> None: ...
    def __int__(self) -> int: ...
    def __ne__(self, other: object) -> bool: ...
    def __repr__(self) -> str: ...
    def __setstate__(self, state: int) -> None: ...
    @property
    def name(self) -> str:
        """
        :type: str
        """
    @property
    def value(self) -> int:
        """
        :type: int
        """
    __members__: dict # value = {'physx': <SimulationEngine.physx: 1>, 'bullet': <SimulationEngine.bullet: 2>, 'kinematic': <SimulationEngine.kinematic: 3>}
    bullet: libry.SimulationEngine # value = <SimulationEngine.bullet: 2>
    kinematic: libry.SimulationEngine # value = <SimulationEngine.kinematic: 3>
    physx: libry.SimulationEngine # value = <SimulationEngine.physx: 1>
    pass
class Skeleton():
    def __init__(self) -> None: ...
    def add(self, arg0: list) -> None: ...
    @staticmethod
    def addEntry(*args, **kwargs) -> typing.Any: ...
    def addExplicitCollisions(self, collisions: StringA) -> None: ...
    def addLiftPriors(self, lift: StringA) -> None: ...
    def enableAccumulatedCollisions(self, enable: bool = True) -> None: ...
    def getKOMO_finalSlice(self, Configuration: Config, lenScale: float, homingScale: float, collScale: float) -> KOMO: ...
    def getKomo_path(self, Configuration: Config, stepsPerPhase: int, accScale: float, lenScale: float, homingScale: float, collScale: float) -> KOMO: ...
    def getKomo_waypoints(self, Configuration: Config, lenScale: float, homingScale: float, collScale: float) -> KOMO: ...
    def getMaxPhase(self) -> float: ...
    def getTwoWaypointProblem(self, t2: int, komoWays: KOMO) -> tuple: ...
    pass
class SolverReturn():
    """
    return of nlp solve call
    """
    def __init__(self) -> None: ...
    def __str__(self) -> str: ...
    def dict(self) -> dict: ...
    @property
    def done(self) -> bool:
        """
        :type: bool
        """
    @done.setter
    def done(self, arg0: bool) -> None:
        pass
    @property
    def eq(self) -> float:
        """
        :type: float
        """
    @eq.setter
    def eq(self, arg0: float) -> None:
        pass
    @property
    def evals(self) -> int:
        """
        :type: int
        """
    @evals.setter
    def evals(self, arg0: int) -> None:
        pass
    @property
    def f(self) -> float:
        """
        :type: float
        """
    @f.setter
    def f(self, arg0: float) -> None:
        pass
    @property
    def feasible(self) -> bool:
        """
        :type: bool
        """
    @feasible.setter
    def feasible(self, arg0: bool) -> None:
        pass
    @property
    def ineq(self) -> float:
        """
        :type: float
        """
    @ineq.setter
    def ineq(self, arg0: float) -> None:
        pass
    @property
    def sos(self) -> float:
        """
        :type: float
        """
    @sos.setter
    def sos(self, arg0: float) -> None:
        pass
    @property
    def time(self) -> float:
        """
        :type: float
        """
    @time.setter
    def time(self, arg0: float) -> None:
        pass
    @property
    def x(self) -> arr:
        """
        :type: arr
        """
    @x.setter
    def x(self, arg0: arr) -> None:
        pass
    pass
def getStartGoalPath(arg0: Config, arg1: arr, arg2: arr) -> arr:
    pass
def params_add(arg0: dict) -> None:
    """
    add/set parameters
    """
def params_file(arg0: str) -> None:
    """
    add parameters from a file
    """
def params_print() -> None:
    """
    print the parameters
    """
def raiPath(*args, **kwargs) -> typing.Any:
    """
    get a path relative to rai base path
    """
def setRaiPath(arg0: str) -> None:
    """
    redefine the rai (or rai-robotModels) path
    """
Ceres: libry.NLP_SolverID # value = <NLP_SolverID.Ceres: 10>
Ipopt: libry.NLP_SolverID # value = <NLP_SolverID.Ipopt: 9>
LBFGS: libry.NLP_SolverID # value = <NLP_SolverID.LBFGS: 2>
NLopt: libry.NLP_SolverID # value = <NLP_SolverID.NLopt: 8>
XBall: libry.JT # value = <JT.XBall: 15>
_left: libry.ArgWord # value = <ArgWord._left: 0>
_path: libry.ArgWord # value = <ArgWord._path: 3>
_right: libry.ArgWord # value = <ArgWord._right: 1>
_sequence: libry.ArgWord # value = <ArgWord._sequence: 2>
above: libry.SY # value = <SY.above: 1>
aboveBox: libry.FS # value = <FS.aboveBox: 33>
acceleration: libry.ControlMode # value = <ControlMode.acceleration: 3>
accumulatedCollisions: libry.FS # value = <FS.accumulatedCollisions: 27>
adversarialDropper: libry.ImpType # value = <ImpType.adversarialDropper: 4>
alignByInt: libry.SY # value = <SY.alignByInt: 31>
angularVel: libry.FS # value = <FS.angularVel: 26>
augmentedLag: libry.NLP_SolverID # value = <NLP_SolverID.augmentedLag: 4>
bounce: libry.SY # value = <SY.bounce: 22>
box: libry.ST # value = <ST.box: 0>
boxGraspX: libry.SY # value = <SY.boxGraspX: 38>
boxGraspY: libry.SY # value = <SY.boxGraspY: 39>
boxGraspZ: libry.SY # value = <SY.boxGraspZ: 40>
break: libry.SY # value = <SY.break: 17>
bullet: libry.SimulationEngine # value = <SimulationEngine.bullet: 2>
camera: libry.ST # value = <ST.camera: 12>
capsule: libry.ST # value = <ST.capsule: 2>
closeGripper: libry.ImpType # value = <ImpType.closeGripper: 0>
contact: libry.SY # value = <SY.contact: 19>
contactComplementary: libry.SY # value = <SY.contactComplementary: 21>
contactConstraints: libry.FS # value = <FS.contactConstraints: 42>
contactStick: libry.SY # value = <SY.contactStick: 20>
cylinder: libry.ST # value = <ST.cylinder: 4>
dampMotion: libry.SY # value = <SY.dampMotion: 29>
depthNoise: libry.ImpType # value = <ImpType.depthNoise: 2>
distance: libry.FS # value = <FS.distance: 29>
downUp: libry.SY # value = <SY.downUp: 16>
dynamic: libry.SY # value = <SY.dynamic: 11>
dynamicOn: libry.SY # value = <SY.dynamicOn: 12>
dynamicTrans: libry.SY # value = <SY.dynamicTrans: 13>
end: libry.SY # value = <SY.end: 46>
energy: libry.FS # value = <FS.energy: 43>
eq: libry.OT # value = <OT.eq: 4>
f: libry.OT # value = <OT.f: 1>
forceBalance: libry.SY # value = <SY.forceBalance: 33>
free: libry.JT # value = <JT.free: 16>
gazeAt: libry.FS # value = <FS.gazeAt: 25>
generic: libry.JT # value = <JT.generic: 17>
gradientDescent: libry.NLP_SolverID # value = <NLP_SolverID.gradientDescent: 0>
hingeX: libry.JT # value = <JT.hingeX: 1>
hingeY: libry.JT # value = <JT.hingeY: 2>
hingeZ: libry.JT # value = <JT.hingeZ: 3>
identical: libry.SY # value = <SY.identical: 30>
ineq: libry.OT # value = <OT.ineq: 3>
ineqB: libry.OT # value = <OT.ineqB: 5>
ineqP: libry.OT # value = <OT.ineqP: 6>
inside: libry.SY # value = <SY.inside: 2>
insideBox: libry.FS # value = <FS.insideBox: 34>
jointLimits: libry.FS # value = <FS.jointLimits: 28>
kinematic: libry.SimulationEngine # value = <SimulationEngine.kinematic: 3>
lift: libry.SY # value = <SY.lift: 41>
logBarrier: libry.NLP_SolverID # value = <NLP_SolverID.logBarrier: 6>
magic: libry.SY # value = <SY.magic: 24>
magicTrans: libry.SY # value = <SY.magicTrans: 25>
makeFree: libry.SY # value = <SY.makeFree: 32>
marker: libry.ST # value = <ST.marker: 5>
mesh: libry.ST # value = <ST.mesh: 3>
newton: libry.NLP_SolverID # value = <NLP_SolverID.newton: 3>
noPenetrations: libry.ImpType # value = <ImpType.noPenetrations: 7>
none: libry.OT # value = <OT.none: 0>
objectImpulses: libry.ImpType # value = <ImpType.objectImpulses: 5>
openGripper: libry.ImpType # value = <ImpType.openGripper: 1>
oppose: libry.SY # value = <SY.oppose: 3>
pairCollision_negScalar: libry.FS # value = <FS.pairCollision_negScalar: 35>
pairCollision_normal: libry.FS # value = <FS.pairCollision_normal: 37>
pairCollision_p1: libry.FS # value = <FS.pairCollision_p1: 38>
pairCollision_p2: libry.FS # value = <FS.pairCollision_p2: 39>
pairCollision_vector: libry.FS # value = <FS.pairCollision_vector: 36>
phiTransXY: libry.JT # value = <JT.phiTransXY: 14>
physics: libry.FS # value = <FS.physics: 41>
physx: libry.SimulationEngine # value = <SimulationEngine.physx: 1>
pointCloud: libry.ST # value = <ST.pointCloud: 6>
pose: libry.FS # value = <FS.pose: 6>
poseDiff: libry.FS # value = <FS.poseDiff: 7>
poseEq: libry.SY # value = <SY.poseEq: 5>
poseRel: libry.FS # value = <FS.poseRel: 8>
position: libry.ControlMode # value = <ControlMode.position: 1>
positionDiff: libry.FS # value = <FS.positionDiff: 1>
positionEq: libry.SY # value = <SY.positionEq: 6>
positionRel: libry.FS # value = <FS.positionRel: 2>
push: libry.SY # value = <SY.push: 23>
pushAndPlace: libry.SY # value = <SY.pushAndPlace: 26>
qItself: libry.FS # value = <FS.qItself: 31>
quad: libry.ST # value = <ST.quad: 11>
quasiStatic: libry.SY # value = <SY.quasiStatic: 14>
quasiStaticOn: libry.SY # value = <SY.quasiStaticOn: 15>
quatBall: libry.JT # value = <JT.quatBall: 13>
quaternion: libry.FS # value = <FS.quaternion: 3>
quaternionDiff: libry.FS # value = <FS.quaternionDiff: 4>
quaternionRel: libry.FS # value = <FS.quaternionRel: 5>
relPosY: libry.SY # value = <SY.relPosY: 34>
restingOn: libry.SY # value = <SY.restingOn: 4>
rgbNoise: libry.ImpType # value = <ImpType.rgbNoise: 3>
rigid: libry.JT # value = <JT.rigid: 12>
rprop: libry.NLP_SolverID # value = <NLP_SolverID.rprop: 1>
scalarProductXX: libry.FS # value = <FS.scalarProductXX: 18>
scalarProductXY: libry.FS # value = <FS.scalarProductXY: 19>
scalarProductXZ: libry.FS # value = <FS.scalarProductXZ: 20>
scalarProductYX: libry.FS # value = <FS.scalarProductYX: 21>
scalarProductYY: libry.FS # value = <FS.scalarProductYY: 22>
scalarProductYZ: libry.FS # value = <FS.scalarProductYZ: 23>
scalarProductZZ: libry.FS # value = <FS.scalarProductZZ: 24>
sdf: libry.ST # value = <ST.sdf: 13>
singleSquaredPenalty: libry.NLP_SolverID # value = <NLP_SolverID.singleSquaredPenalty: 7>
sos: libry.OT # value = <OT.sos: 2>
sphere: libry.ST # value = <ST.sphere: 1>
spline: libry.ControlMode # value = <ControlMode.spline: 5>
squaredPenalty: libry.NLP_SolverID # value = <NLP_SolverID.squaredPenalty: 5>
ssBox: libry.ST # value = <ST.ssBox: 8>
ssBoxElip: libry.ST # value = <ST.ssBoxElip: 10>
ssCvx: libry.ST # value = <ST.ssCvx: 7>
ssCylinder: libry.ST # value = <ST.ssCylinder: 9>
stable: libry.SY # value = <SY.stable: 9>
stableOn: libry.SY # value = <SY.stableOn: 10>
stableOnX: libry.SY # value = <SY.stableOnX: 43>
stableOnY: libry.SY # value = <SY.stableOnY: 44>
stablePose: libry.SY # value = <SY.stablePose: 8>
stableRelPose: libry.SY # value = <SY.stableRelPose: 7>
stableYPhi: libry.SY # value = <SY.stableYPhi: 42>
stableZero: libry.SY # value = <SY.stableZero: 18>
standingAbove: libry.FS # value = <FS.standingAbove: 40>
tau: libry.JT # value = <JT.tau: 18>
topBoxGrasp: libry.SY # value = <SY.topBoxGrasp: 27>
topBoxPlace: libry.SY # value = <SY.topBoxPlace: 28>
touch: libry.SY # value = <SY.touch: 0>
touchBoxNormalX: libry.SY # value = <SY.touchBoxNormalX: 35>
touchBoxNormalY: libry.SY # value = <SY.touchBoxNormalY: 36>
touchBoxNormalZ: libry.SY # value = <SY.touchBoxNormalZ: 37>
trans3: libry.JT # value = <JT.trans3: 8>
transAccelerations: libry.FS # value = <FS.transAccelerations: 44>
transVelocities: libry.FS # value = <FS.transVelocities: 45>
transX: libry.JT # value = <JT.transX: 4>
transXY: libry.JT # value = <JT.transXY: 7>
transXYPhi: libry.JT # value = <JT.transXYPhi: 9>
transY: libry.JT # value = <JT.transY: 5>
transYPhi: libry.JT # value = <JT.transYPhi: 10>
transZ: libry.JT # value = <JT.transZ: 6>
universal: libry.JT # value = <JT.universal: 11>
vectorX: libry.FS # value = <FS.vectorX: 9>
vectorXDiff: libry.FS # value = <FS.vectorXDiff: 10>
vectorXRel: libry.FS # value = <FS.vectorXRel: 11>
vectorY: libry.FS # value = <FS.vectorY: 12>
vectorYDiff: libry.FS # value = <FS.vectorYDiff: 13>
vectorYRel: libry.FS # value = <FS.vectorYRel: 14>
vectorZ: libry.FS # value = <FS.vectorZ: 15>
vectorZDiff: libry.FS # value = <FS.vectorZDiff: 16>
vectorZRel: libry.FS # value = <FS.vectorZRel: 17>
velocity: libry.ControlMode # value = <ControlMode.velocity: 2>
