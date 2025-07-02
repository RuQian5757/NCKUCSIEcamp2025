void setup() {
  pinMode(2, OUTPUT); //設定2號pin腳為輸出模式
}

void loop() {
  digitalWrite(2, HIGH); //設定2號腳位輸出高電位
  delay(1000); //等待1秒鐘 (1000毫秒)
  digitalWrite(2, LOW); //設定2號腳位輸出低電位
  delay(1000); //等待1秒鐘 (1000毫秒)
}