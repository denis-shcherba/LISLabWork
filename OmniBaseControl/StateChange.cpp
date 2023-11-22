#include "../src/SimplexMotion.h"
#include "../src/SimplexMotion_ControlThread.h"

#include <unistd.h>
#include <iostream>
#include <string.h>
#include <fstream>
#include <math.h>


int main(int argc, char **argv){
    // /dev/hidraw1
    if(argc < 4) {
        std::cout << "Please enter Motor USB ports." << std::endl;
        return 0;
    }

    SimplexMotion motor0(argv[0]);
    SimplexMotion motor1(argv[1]);
    SimplexMotion motor2(argv[2]);

    motor0.setPID(300, 0, 200, 100, 2, 0);
    motor1.setPID(300, 0, 200, 100, 2, 0);
    motor2.setPID(300, 0, 200, 100, 2, 0);

    // Updates per seconds
    float ups = 60;

    double endX = 2;
    double endY = 2;
    double endPhi = M_PI;
    double duration = 5;
    double omega = endPhi/duration;

    float wheelSpeeds[3];

    float Xn = endX/duration;
    float Yn = endY/duration;

    std::chrono::steady_clock::time_point begin = std::chrono::steady_clock::now();
    std::chrono::steady_clock::time_point end = std::chrono::steady_clock::now();
    
    double time_passed = 0;
    while (time_passed <= duration)
    {
        if (std::chrono::duration_cast<std::chrono::milliseconds>(end - begin).count() > 1000/ups)
        {
            begin = std::chrono::steady_clock::now();
            
            float Phin = omega*time_passed;
            double y0 = (Yn-sin(Phin)*Xn/cos(Phin))/(sin(Phin)*sin(Phin)/(cos(Phin))+cos(Phin))
            double x0 = (Xn+sin(Phin)*y0)/cos(Phin);

            wheelSpeeds[0] = (-1./3.)*x0 + (1./sqrt(3.))*y0 + 1/3*Phin;
            wheelSpeeds[1] = (-1./3.)*x0 + (-1./sqrt(3.))*y0 + 1/3*Phin;
            wheelSpeeds[2] = (2./3.)*x0 + (1./3.)*Phin;

            motor0.runSpeed(wheelSpeeds[0]);
            motor1.runSpeed(wheelSpeeds[1]);
            motor2.runSpeed(wheelSpeeds[2]);
            time_passed += 1/ups;
            end = std::chrono::steady_clock::now();
        }
        else end = std::chrono::steady_clock::now();
    }

    motor0.runStop();
    motor1.runStop();
    motor2.runStop();
    usleep(500000);
    motor0.runOff();
    motor1.runOff();
    motor2.runOff();

    return 0;
}