#include <Servo.h>

Servo s;

void setup()
{
    Serial1.begin(57600);             //建立Arduino ATMega32U4與MT7688AN之間的連結
    s.attach(3);                      //將伺服馬達的腳位指定給3號腳位
}

void loop()
{
    if(Serial1.available())
    {
        int command = Serial1.read(); //讀取MT7688AN送來的指令
        if(command == 'o')            //如果是o的話，就打開夾爪
            s.write(160);
        else if(command == 'f')       //如果是f的話，就合起夾爪
            s.write(30);
    }
}
