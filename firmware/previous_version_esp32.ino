#include <Keypad.h>
#include <ESP32Encoder.h>


// =========================
// TECLADO 4x4
// =========================

const byte FILAS = 4;
const byte COLUMNAS = 4;

char teclas[FILAS][COLUMNAS] = {
  {'1','2','3','A'},
  {'4','5','6','B'},
  {'7','8','9','C'},
  {'*','0','#','D'}
};

byte pinesFila[FILAS] = {
  13, 12, 14, 27
};

byte pinesColumna[COLUMNAS] = {
  26, 25, 33, 32
};

Keypad teclado = Keypad(
  makeKeymap(teclas),
  pinesFila,
  pinesColumna,
  FILAS,
  COLUMNAS
);


// =========================
// ENCODER KY-040
// =========================

ESP32Encoder encoder1;

#define ENC1_CLK 18
#define ENC1_DT  19
#define ENC1_SW  21



// =========================
// ENCODER NUEVO
// =========================

ESP32Encoder encoder2;

#define ENC2_CLK 23   // Amarillo
#define ENC2_DT  5    // Rojo
#define ENC2_SW  16   // Azul


// Alimentación encoder nuevo
#define ENC2_VCC 22
#define ENC2_GND 17



long anteriorEncoder1 = 0;
long anteriorEncoder2 = 0;



void setup() {

  Serial.begin(115200);


  // Alimentación encoder nuevo
  pinMode(ENC2_VCC, OUTPUT);
  digitalWrite(ENC2_VCC, HIGH);

  pinMode(ENC2_GND, OUTPUT);
  digitalWrite(ENC2_GND, LOW);


  // Botones
  pinMode(ENC1_SW, INPUT_PULLUP);
  pinMode(ENC2_SW, INPUT_PULLUP);


  // Encoders
  encoder1.attachHalfQuad(ENC1_CLK, ENC1_DT);
  encoder1.clearCount();

  encoder2.attachHalfQuad(ENC2_CLK, ENC2_DT);
  encoder2.clearCount();


  Serial.println("Wiwi StreamDeck iniciado");
}



void loop() {


  // =========================
  // TECLADO
  // =========================

  char tecla = teclado.getKey();

  if(tecla) {

    Serial.print("KEY:");
    Serial.println(tecla);

  }



  // =========================
  // ENCODER 1
  // =========================

  long valor1 = encoder1.getCount();

  if(valor1 != anteriorEncoder1) {

    if(valor1 > anteriorEncoder1)
      Serial.println("ENC1:RIGHT");
    else
      Serial.println("ENC1:LEFT");


    anteriorEncoder1 = valor1;

  }


  if(digitalRead(ENC1_SW) == LOW) {

    Serial.println("ENC1:PRESS");
    delay(200);

  }



  // =========================
  // ENCODER 2
  // =========================

  long valor2 = encoder2.getCount();

  if(valor2 != anteriorEncoder2) {

    if(valor2 > anteriorEncoder2)
      Serial.println("ENC2:RIGHT");
    else
      Serial.println("ENC2:LEFT");


    anteriorEncoder2 = valor2;

  }


  if(digitalRead(ENC2_SW) == LOW) {

    Serial.println("ENC2:PRESS");
    delay(200);

  }

}