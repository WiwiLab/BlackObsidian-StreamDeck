#pragma once

//============================
// BOTONES
//============================

#define BTN_1 "B1"
#define BTN_2 "B2"
#define BTN_3 "B3"
#define BTN_4 "B4"
#define BTN_5 "B5"
#define BTN_6 "B6"

#define BTN_7 "B7"
#define BTN_8 "B8"
#define BTN_9 "B9"

#define BTN_STAR "B*"
#define BTN_0 "B0"
#define BTN_HASH "B#"

#define BTN_A "BA"
#define BTN_B "BB"
#define BTN_C "BC"
#define BTN_D "BD"


//============================
// ENCODER RGB
//============================

#define ENC_MAIN_RIGHT "E1R"
#define ENC_MAIN_LEFT  "E1L"
#define ENC_MAIN_PRESS "E1P"


//============================
// ENCODER KY040
//============================

#define ENC_MEDIA_RIGHT "E2R"
#define ENC_MEDIA_LEFT  "E2L"
#define ENC_MEDIA_PRESS "E2P"


//============================

inline void event(const char* e)
{
    Serial.println(e);
}