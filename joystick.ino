const int AXIS_X  = A1;
const int AXIS_Y  = A2;
const int SW_P    = A3; 
int x             = 488;
int y             = 520;
int s             = 1;
int flag          = 0;

void setup() {
  Serial.begin(9600);
  pinMode(SW_P,INPUT_PULLUP);
}

void loop() 
{
  int i = 1;
  
  while(i)
  {
    int x1 = analogRead(AXIS_X);
    int y1 = analogRead(AXIS_Y);

    int absx = abs(x1-x);
    int absy = abs(y1-y);

    s = digitalRead(SW_P);

    if(s == 0)
    {
      Serial.println("5");
      delay(300);
    }

    if((absx > 400 || absy > 400) && s == 1)
    {
      x = x1;
      y = y1;
      if(abs(x-488) > 10 || abs(y-520) > 400)
      {
        stick(x,y);
      }
      i = 0;
    }
  }

}

int stick(int x, int y)
{
  int subx,suby;

  subx = x - 450;
  suby = y - 500;

  if (subx < 0 && suby > 0)
  {
    Serial.println("2");
  }
  else if (subx > 0 && abs(subx) > 300 && suby > 0)
  {
    Serial.println("-2");
  }
  else if (subx > 0 && suby < 0)
  {
    Serial.println("1");
  }
  else if (subx > 0 && suby > 0)
  {
    Serial.println("-1");
  }
  // 위 : 음수 양수    2
  // 아래 : 양수 양수   -2
  // 오른 : 양수 음수   1
  // 왼 : 양 양     -1
}
