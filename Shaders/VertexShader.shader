#version 330
layout(location = 0) in vec3 position;
layout(location = 1) in vec3 normal;
layout(location = 2) in vec2 texcoord;

out vec2 TexCoord;
out vec3 Normal;
out vec3 FragPos;
out vec3 Cam_Pos;

uniform mat4 projection;
uniform mat4 modelview;

void main()
{

    vec4 coord = projection * modelview * vec4(position, 1.0);

    gl_Position = coord;
    TexCoord = texcoord;
    Normal = normalize(mat3(transpose(inverse(modelview))) * normal);
    FragPos = vec3(modelview * vec4(position, 1.0));
    Cam_Pos = vec3(modelview[0][3], modelview[1][3], modelview[2][3]);

}