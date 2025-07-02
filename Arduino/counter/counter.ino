int sevenSegmentPin[] = {2, 3, 4, 5, 8, 9, 10}; //定義七段顯示器腳位
bool pinLevel[10][7] = {
//{b, a, f, g, c, d, e}
  {1, 1, 1, 0, 1, 1, 1}, // 0
  {1, 0, 0, 0, 1, 0, 0}, // 1
  {1, 1, 0, 1, 0, 1, 1}, // 2
  // TODO
};

int count = 0;

void setup() {
  //設定七段顯示器的腳位為輸出模式
  for(int i=0; i<7; i++){
    pinMode(sevenSegmentPin[i], OUTPUT);
  }
  pinMode(7, INPUT);
  display_clear();
}

void loop() {
  if(digitalRead(7) == HIGH){
    delay(100); //稍微緩衝一下，避免訊號不穩定
    while(digitalRead(7) == HIGH); //重複直到按鈕被放開
    count = (count + 1) % 10;
  }
  display_number(count);
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