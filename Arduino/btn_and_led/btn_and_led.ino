void setup() {
  pinMode(2, OUTPUT); //設定2號pin腳為輸出模式
  pinMode(7, INPUT); //設定7號pin腳為輸入模式
}

void loop() {
  bool is_pressed = digitalRead(7);
  digitalWrite(2, is_pressed); //設定2號腳位輸出 is_pressed 的訊號
}