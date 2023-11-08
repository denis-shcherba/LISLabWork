#include "../src/SimplexMotion.h"
#include "../src/SimplexMotion_ControlThread.h"

#include <unistd.h>
#include <iostream>
#include <string.h>
#include <fstream>

class OmniBase {
    // SimplexMotion_ControlThread motor0;
    // SimplexMotion_ControlThread motor1;
    // SimplexMotion_ControlThread motor2;
    SimplexMotion motor0;
    SimplexMotion motor1;
    SimplexMotion motor2;

  public:
    OmniBase(const char* devPath0, const char* devPath1, const char* devPath2);
    ~OmniBase();
    void calibrate();
    void spinClock(float speed, float seconds);
    void runTorque(float torque);
};

OmniBase::OmniBase(const char* devPath0, const char* devPath1, const char* devPath2) : motor0(devPath0), motor1(devPath1), motor2(devPath2)
{
  /*
  motor1.setCtrlTime( motor0.getCtrlTime() );
  motor2.setCtrlTime( motor1.getCtrlTime() );

  M0.setLogFile("M1.dat");
  M1.setLogFile("M1.dat");
  M2.setLogFile("M2.dat");

  std::ifstream fil("experiment.config");
  double q_ref=0., qDot_ref=0., Kp=.05, Kd=.002, u_b=0.;
  fil >>q_ref >>qDot_ref >>Kp >>Kd >>u_b;
  fil.close();
  std::cout << "USING: " << q_ref << ' ' << qDot_ref << ' ' << Kp << ' ' << Kd << ' ' << u_b << std::endl;

  double q0 = motor0.getPosition();
  q0 += q_ref;
  motor0.setCmd({q0, qDot_ref, Kp, Kd, u_b});

  q0 = motor1.getPosition();
  q0 -= q_ref;
  motor1.setCmd({q0, qDot_ref, Kp, Kd, u_b});

  q0 = motor1.getPosition();
  q0 -= q_ref;
  motor1.setCmd({q0, qDot_ref, Kp, Kd, u_b});

  sleep(5);
  */
}

OmniBase::~OmniBase() {
  motor0.runStop();
  motor1.runStop();
  motor2.runStop();
  usleep(500000);
  motor0.runOff();
  motor1.runOff();
  motor2.runOff();
}

void OmniBase::calibrate() {
  std::cout << "Cogging Calibration... " << std::endl;
  motor0.runCoggingCalibration();
  motor1.runCoggingCalibration();
  motor2.runCoggingCalibration();
}

void OmniBase::runTorque(float torque) {
  motor0.runTorque(torque);
  motor1.runTorque(torque);
  motor2.runTorque(torque);
}

void OmniBase::spinClock(float speed, float seconds) {
  motor0.setPID(300, 0, 200, 100, 2, 0); //low gain... (idk what this does)
  motor0.runSpeed(speed);
  motor1.setPID(300, 0, 200, 100, 2, 0); //low gain... (idk what this does)
  motor1.runSpeed(speed);
  motor2.setPID(300, 0, 200, 100, 2, 0); //low gain... (idk what this does)
  motor2.runSpeed(speed);
  for(uint t=0;t<100;t++) {
    std:cout << t << " pos:" << M.getMotorPosition() <<" vel:" << M.getMotorSpeed() << std::endl;
    usleep(seconds*10000);
  }
}

int main(int argc, char **argv){
  // /dev/hidraw1
  if(argc < 4) {
    std::cout << "Please enter Motor USB ports." << std::endl;
    return 0;
  }

  OmniBase ob(argv[1], argv[2], argv[3]);
  std::cout << "Calibrating..." << std::endl;
  ob.calibrate();
  std::cout << "Turning clockwise..." << std::endl;
  ob.spinClock(15., 1);
  std::cout << "Done." << std::endl;

  return 0;
}