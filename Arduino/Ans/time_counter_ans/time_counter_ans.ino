int sevenSegmentPin[] = {2, 3, 4, 5, 8, 9, 10}; //定義七段顯示器腳位
bool pinLevel[10][7] = {
//{b, a, f, g, c, d, e}
  {1, 1, 1, 0, 1, 1, 1}, // 0
  {1, 0, 0, 0, 1, 0, 0}, // 1
  {1, 1, 0, 1, 0, 1, 1}, // 2
  {1, 1, 0, 1, 1, 1, 0}, // 3
  {1, 0, 1, 1, 1, 0, 0}, // 4
  {0, 1, 1, 1, 1, 1, 0}, // 5
  {0, 1, 1, 1, 1, 1, 1}, // 6
  {1, 1, 0, 0, 1, 0, 0}, // 7
  {1, 1, 1, 1, 1, 1, 1}, // 8
  {1, 1, 1, 1, 1, 1, 0}  // 9
};

int count = 0;
long last_time;

void setup() {
  //設定七段顯示器的腳位為輸出模式
  for(int i=0; i<7; i++){
    pinMode(sevenSegmentPin[i], OUTPUT);
  }
  pinMode(7, INPUT);
  display_clear();
}

void loop() {
  if(digitalRead(7)){
    last_time = millis(); //紀錄按下按鈕的時間
    delay(100); //稍微緩衝一下，避免訊號不穩定
    while(digitalRead(7)){ //重複直到按鈕被放開
      if(millis() - last_time >= 1000){ //若現在的時間 - 上次紀錄的時間 >= 1秒鐘
        count = (count + 1) % 10; //計數+1 再 mod 10
        last_time = millis(); //更新紀錄時間為現在
      }
      display_number(count); //顯示數字
    }
  }
  count = 0; //重製計數
  display_clear(); //清空顯示
}

void display_number(int num){
  for(int i=0; i<7; i++){
    digitalWrite(sevenSegmentPin[i], pinLevel[num][i]);
  }
}

void display_clear(){
  for(int i=0; i<7; i++){
    digitalWrite(sevenSegmentPin[i], LOW);
  }
}