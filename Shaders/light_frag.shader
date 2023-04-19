#version 330

in vec3 FragPos;
flat in vec3 FlatFragPos;
in vec2 Pos;
flat in int Line;
in float Time;


#define STRIP 1.0
#define SPEED 5.0
#define POINTSIZE 3.5

void main()
{
    float uzunluk = length(Pos - gl_FragCoord.xy);
    float tp = 1.0;
    float red;
    float green;
    float blue;


    float sayac = length(FragPos - FlatFragPos);

    if (mod( sayac + Time*SPEED, STRIP) > STRIP/2) {

        red = 0.5568;
        green = 0.898;
        blue = 0.7019;

    }
 
    else {

        red = 0.0;
        green = 0.0;
        blue = 0.0;

    }

    if (Line == 0 && uzunluk >= POINTSIZE-1) {
        
        if (uzunluk < POINTSIZE) {

            tp = POINTSIZE - uzunluk;
        }

        else {

            tp = 0.0;

        }
    
    }

    gl_FragColor = vec4(red, green, blue, tp);

}