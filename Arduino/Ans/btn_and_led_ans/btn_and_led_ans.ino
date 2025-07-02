void setup() {
  pinMode(2, OUTPUT); //設定2號pin腳為輸出模式
  pinMode(7, INPUT); //設定7號pin腳為輸入模式
}

bool led_control = false;

void loop() {
  if(digitalRead(7)){
    delay(100); //稍微緩衝一下，避免訊號不穩定
    while(digitalRead(7)); //等待直到按鈕放開
    led_control = !led_control; //led_control 反閘 (true -> false, false -> true)
  }
  digitalWrite(2, led_control); //設定2號腳位輸出 led_control 的訊號
}