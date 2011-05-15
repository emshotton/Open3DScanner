const int stepper_1 = 2; 
const int stepper_2 = 3;
const int stepper_3 = 4;
const int stepper_4 = 5;


int step_sequence[][4] =   {
                          {1,0,0,0},
                          {0,1,0,0},
                          {0,0,1,0},
                          {0,0,0,1}
                          };


int incomingByte;      // a variable to read incoming serial data into

int step_position = 0;



void rotate_platform(){
   digitalWrite(stepper_1, step_sequence[step_position][0]);
   digitalWrite(stepper_2, step_sequence[step_position][1]);
   digitalWrite(stepper_3, step_sequence[step_position][2]);
   digitalWrite(stepper_4, step_sequence[step_position][3]);
   step_position++;
   if (step_position == 4){
     step_position = 0;
   }
   
}

void setup() {
  // initialize serial communication:
  Serial.begin(9600);
  // initialize the LED pin as an output:
  pinMode(stepper_1, OUTPUT);
  pinMode(stepper_2, OUTPUT);
  pinMode(stepper_3, OUTPUT);
  pinMode(stepper_4, OUTPUT);
}

void loop() {

/*  if (Serial.available() > 0) {
    incomingByte = Serial.read();
    if (incomingByte == 'H') {
      digitalWrite(ledPin, HIGH);
    } 
    if (incomingByte == 'L') {
      digitalWrite(ledPin, LOW);
    }
  }
*/  
 rotate_platform(); 
 delay(200);
}
