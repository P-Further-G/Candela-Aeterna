#version 330 core
layout(location = 0) in vec3 position;
layout(location = 1) in vec3 normal;
layout(location = 2) in vec2 texcoord;

out vec2 TexCoord;
out vec3 Normal;
out vec3 FragPos;
out vec4 fragposlight;

uniform mat4 projection;
uniform mat4 model;
uniform mat4 view;
uniform mat4 lightview;
uniform mat4 depth_matrix;


void main()
{

    FragPos = vec3(model * vec4(position, 1.0));
    vec4 coord = projection * view * model * vec4(position, 1.0);
    fragposlight = projection * lightview * vec4(position, 1.0);

    gl_Position = coord;
    TexCoord = texcoord;

    Normal = normalize((transpose(inverse(mat3(model)))) * normal);



}