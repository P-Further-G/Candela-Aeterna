#version 330

in vec3 FragPos;
in vec2 Pos;
flat in int Line;
in float Time;


#define STRIP 0.5
#define SPEED 2.0
#define POINTSIZE 3.4

void main()
{
    float uzunluk = length(Pos - gl_FragCoord.xy);
    float tp = 1.0;
    float red;

    if (mod(FragPos.x - Time*SPEED, STRIP) > STRIP/2) {

        red = 1.0;

    }

    else {

        red = 0.0;

    }

    if (Line == 0 && uzunluk >= POINTSIZE-1) {
        
        if (uzunluk < POINTSIZE) {

            tp = POINTSIZE - uzunluk;
        }

        else {

            tp = 0.0;

        }
    
    }

    gl_FragColor = vec4(red, 0, 0, tp);

}