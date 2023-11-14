#include <Gamepad/gamepad.h>
#include <SimplexMotion/SimplexMotion.h>
#include <SimplexMotion/SimplexMotion_ControlThread.h>

void driveCart()
{
    GamepadInterface G;

    SimplexMotion_ControlThread ML(rai::getParameter<rai::String>("usbLeft"));
    SimplexMotion_ControlThread MR(rai::getParameter<rai::String>("usbRight"));

    MR.setCtrlTime(ML.getCtrlTime());

    ML.setLogFile("ML.dat");
    MR.setLogFile("MR.dat");

    double qDot_ref = 0.;
    double Kp = rai::getParameter<double>("Kp", .05);
    double Kd = rai::getParameter<double>("Kd", .002);
    double u_b = 0.;

    double vel = rai::getParameter<double>("vel", .2);
    double steer = rai::getParameter<double>("steer", .2);

    double q0 = ML.getPosition();
    ML.setCmd({q0, qDot_ref, Kp, Kd, u_b});

    double q1 = MR.getPosition();
    MR.setCmd({q1, qDot_ref, Kp, Kd, u_b});

    for (;;)
    {
        rai::wait(.05);
        // G.gamepadState.waitForNextRevision();
        arr pad = G.gamepadState.get();
        q0 += vel * pad(5);
        q1 -= vel * pad(5);
        q0 -= steer * pad(4);
        q1 -= steer * pad(4);

        ML.setCmd({q0, qDot_ref, Kp, Kd, u_b});
        MR.setCmd({q1, qDot_ref, Kp, Kd, u_b});

        cout << "\r" << pad << std::flush;
        if (G.quitSignal.get())
            break;
    }
}

int main(int argc, char **argv)
{
    rai::initCmdLine(argc, argv);

    cout << "!!! sudo chmod a+rw /dev/hidraw !!!" << endl;

    driveCart();

    cout << "BYE BYE" << endl;

    return 0;
}
