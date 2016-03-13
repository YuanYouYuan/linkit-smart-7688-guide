#include <Servo.h>
Servo s;
void setup()
{
    s.attach(3);                //將伺服馬達的腳位指定給3號腳位
}

void loop()
{
    for(i = 30; i <= 150; i++)  //20每毫秒正轉一度
    {
        s.write(i);
        delay(20);
    }
    for(i = 150; i >= 30; i--)  //20每毫秒反轉一度
    {
        s.write(i);
        delay(20);
    }
}
