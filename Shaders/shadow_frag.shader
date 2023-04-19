#version 330 core

in vec2 TexCoord;
in vec3 Normal;
in vec3 FragPos;
in vec4 fragposlight;

uniform sampler2D oTexture;
uniform sampler2D shadowmap;

out vec4 Color;

float calculateshadow(vec4 fragposlightspace) {

    vec3 depth = fragposlightspace.xyz / fragposlightspace.w;

    depth = depth * 0.5 + 0.5;

    float closestDepth = texture(shadowmap, depth.xy).r;
    float currentDepth = depth.z;

    float shadow = currentDepth - 0.0005 > closestDepth ? 1.0 : 0.3;

    return shadow;

}

void main()
{
    vec3 lightcolor = vec3(1.0, 1.0, 1.0);
    float diffuseStrength = 0.5;
    vec4 basecolor = texture(oTexture, TexCoord);

    vec3 ambient = 0.2 * lightcolor;

    vec3 lightDir = normalize(vec3(0, 0, -10) - FragPos);
    float diff = (dot(Normal, lightDir) + 1);
    vec3 diffuse = diff * lightcolor * diffuseStrength * 0;


    float shadow = calculateshadow(fragposlight);
    vec3 result = (ambient + ((1.0 - shadow) + diffuse)) * basecolor.xyz;


    //float value = texture(shadowmap, TexCoord).r;
    Color = vec4(result, basecolor.w);

}