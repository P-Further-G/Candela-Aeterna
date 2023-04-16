#version 330
layout(location = 0) in vec3 position;
layout(location = 1) in vec3 normal;
layout(location = 2) in vec2 texcoord;

out vec2 TexCoord;
out vec3 Normal;
out vec3 FragPos;
out vec4 fragposlight;

uniform mat4 projection;
uniform mat4 modelview;

mat4 getmodelview(float x, float y, float z, float rx, float ry) {

    mat4 basic = mat4(1.0, 0.0, 0.0, 0.0, 
                      0.0, 1.0, 0.0, 0.0,
                      0.0, 0.0, 1.0, 0.0, 
                      0.0, 0.0, 0.0, 1.0);

    mat4 rotx = mat4(1.0, 0.0, 0.0, 0.0, 0.0, cos(rx), -sin(rx), 0.0, 0.0, sin(rx), cos(rx), 0.0, 0.0, 0.0, 0.0, 1.0);

    mat4 roty = mat4(cos(ry), 0.0, sin(ry), 0.0, 0.0, 1.0, 0.0, 0.0, -sin(ry), 0.0, cos(ry), 0.0, 0.0, 0.0, 0.0, 1.0);

    basic = (basic *rotx * roty);

    return basic;
}


void main()
{
    mat4 lmv = getmodelview(0, 0, 0, 0.0, 3.1415);
    vec4 coord = projection * modelview * vec4(position, 1.0);
    fragposlight = projection * lmv * vec4(position, 1.0);


    gl_Position = coord;
    TexCoord = texcoord;

    Normal = normalize(mat3(transpose(inverse(modelview))) * normal);
    FragPos = vec3(modelview * vec4(position, 1.0));



}