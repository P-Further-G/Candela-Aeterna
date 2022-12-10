#version 330

in vec3 he;
in vec2 te;
out vec4 Color;


void main()
{
    

    Color = vec4(te,0.0,0.0) + vec4(he,0.0) + vec4(1.0, 0.0, 0.0, 1.0);


}