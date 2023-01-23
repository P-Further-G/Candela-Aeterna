#version 330
layout(location = 0) in vec3 position;
layout(location = 1) in int type;

out vec3 FragPos;
flat out vec3 FlatFragPos;
out vec2 Pos;
out float Time;
flat out int Line;

uniform mat4 projection;
uniform mat4 modelview;
uniform vec2 u_viewport;
uniform float utime;

void main()
{
    FragPos = position;
    FlatFragPos = position;

    vec4 coord = projection * modelview * vec4(position, 1.0);
    gl_Position = coord;
    Pos = (coord.xy / coord.w + 1) / 2 * u_viewport;
    Time = utime;
    Line = type;

}