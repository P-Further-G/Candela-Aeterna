#version 330
layout(location = 0) in vec3 position;
layout(location = 1) in vec3 normal;
layout(location = 2) in vec2 texcoord;

out vec3 he;
out vec2 te;

uniform mat4 projection;
uniform mat4 modelview;

void main()
{
    
    he = normal;
    te = texcoord;

    vec4 coord = projection * modelview * vec4(position, 1.0);

    gl_Position = coord;


}