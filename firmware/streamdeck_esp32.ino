#include <Keypad.h>
const byte ROWS = 4;
const byte COLS = 4;

char keys[ROWS][COLS] =
{
    {'1','2','3','A'},
    {'4','5','6','B'},
    {'7','8','9','C'},
    {'*','0','#','D'}
};

byte rowPins[ROWS] =
{
    13,
    12,
    14,
    27
};

byte colPins[COLS] =
{
    26,
    25,
    33,
    32
};

Keypad keypad =
Keypad(
    makeKeymap(keys),
    rowPins,
    colPins,
    ROWS,
    COLS
);
#define SERIAL_BAUD 115200

void sendEvent(const char *event)
{
    Serial.println(event);
}

void setup()
{
    Serial.begin(SERIAL_BAUD);

    delay(1000);

    Serial.println("READY");
}

void loop()
{

    char key = keypad.getKey();

    if(key)
    {
        Serial.print("B");
        Serial.println(key);
    }

}