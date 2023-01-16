#version 330
layout(location = 0) in vec3 position;
layout(location = 1) in vec3 normal;
layout(location = 2) in vec2 texcoord;

out vec2 TexCoord;

uniform mat4 projection;
uniform mat4 modelview;

float outlining = 0.5;

void main()
{

    vec4 coord = projection * modelview * vec4(position + normal*outlining, 1.0);
    gl_Position = coord.xyww;
    TexCoord = texcoord;

}