#include <Servo.h>

Servo servo_gripper;
Servo servo_base;
Servo servo_updown;
Servo servo_frontback;

int degree_base      = 180;           //設定初始角度，請依照您的機械手臂做微調
int degree_updown    = 90;
int degree_frontback = 90;

void setup()
{
    Serial.begin(115200);
    Serial1.begin(57600);             //建立Arduino ATMega32U4與MT7688AN之間的連結
    servo_gripper.attach(3);          //將夾爪的伺服馬達的腳位指定給3號腳位
    servo_updown.attach(5);           //將升降的伺服馬達的腳位指定給5號腳位
    servo_frontback.attach(6);        //將前後的伺服馬達的腳位指定給6號腳位
    servo_base.attach(9);             //將平台的伺服馬達的腳位指定給9號腳位
}


void loop()
{
    if(Serial1.available())
    {
        int command = Serial1.read(); //讀取MT7688AN送來的指令
        if(command == 'o')            //如果是o的話，就打開夾爪
        {
            Serial.println("gripper open");
            servo_gripper.write(160);
        }
        else if(command == 'f')       //如果是f的話，就合起夾爪
        {
            Serial.println("gripper closed");
            servo_gripper.write(30);
        }
        else if(command == 'u')       //如果是u的話，就上升手臂
        {
            degree_updown = (++degree_updown > 180) ? 180 : degree_updown;
            Serial.print("degree_updown");
            Serial.println(degree_updown);
            servo_updown.write(degree_updown);
        }
        else if(command == 'd')       //如果是d的話，就下降手臂
        {
            degree_updown = (--degree_updown < 0) ? 0 : degree_updown;
            Serial.print("degree_updown");
            Serial.println(degree_updown);
            servo_updown.write(degree_updown);
        }
        else if(command == 'a')       //如果是a的話，就前伸手臂
        {
            degree_frontback = (++degree_frontback > 180) ? 180 : degree_frontback;
            Serial.print("degree_frontback: ");
            Serial.println(degree_frontback);
            servo_frontback.write(degree_frontback);
        }
        else if(command == 'b')       //如果是b的話，就後縮手臂
        {
            degree_frontback = (--degree_frontback < 0) ? 0 : degree_frontback;
            Serial.print("degree_frontback: ");
            Serial.println(degree_frontback);
            servo_frontback.write(degree_frontback);
        }
        else if(command == 'l')       //如果是l的話，就左轉平台
        {
            degree_base = (++degree_base > 180) ? 180 : degree_base;
            Serial.print("degree_base: ");
            Serial.println(degree_base);
            servo_base.write(degree_base);
        }
        else if(command == 'r')       //如果是r的話，就右轉平台
        {
            degree_base = (--degree_base < 0) ? 0 : degree_base;
            Serial.print("degree_base: ");
            Serial.println(degree_base);
            servo_base.write(degree_base);
        }
    }
}
