#version 330 core

layout(location = 0) in vec3 position;
layout(location = 1) in vec3 normal;
layout(location = 2) in vec2 texcoord;

out vec2 TexCoord;
out vec3 Normal;

uniform mat4 projection;
uniform mat4 modelview;

void main()
{

    vec4 coord = projection * modelview * vec4(position, 1.0);
    gl_Position = coord;
    TexCoord = texcoord;
    Normal = normal;

}