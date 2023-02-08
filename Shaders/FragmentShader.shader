#version 330

in vec2 TexCoord;
in vec3 Normal;
in vec3 FragPos;
in vec3 Cam_Pos;

uniform sampler2D oTexture;

out vec4 Color;


void main()
{
    vec3 lightcolor = vec3(.9, .9, .9);
    float specularStrength = 0.2;
    float diffuseStrength = 0.5;
    vec4 basecolor = texture(oTexture, TexCoord);


    vec3 ambient = 0.1 * lightcolor;

    vec3 lightDir = normalize(vec3(0,10,0) - FragPos);
    float diff = (dot(Normal, lightDir) + 1);
    vec3 diffuse = diff * lightcolor * diffuseStrength;


    vec3 viewDir = normalize(Cam_Pos - FragPos);
    vec3 reflectDir = reflect(-lightDir, Normal);
    float spec = pow(max(dot(viewDir, reflectDir), 0.0),4);
    vec3 specular = specularStrength * spec * lightcolor;

    vec3 result = (ambient + diffuse + specular) * basecolor.xyz;

    Color = vec4(result, basecolor.w);

}