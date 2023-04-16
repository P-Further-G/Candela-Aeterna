#version 330

in vec2 TexCoord;
in vec3 Normal;
in vec3 FragPos;
in vec4 fragposlight;

uniform sampler2D oTexture;
uniform sampler2D shadowmap;

out vec4 Color;

float calculateshadow(vec4 fragposlightspace) {

    float shadow = 0.0;
    vec3 depth = fragposlightspace.xyz / fragposlightspace.w;
    if (depth.z <= 1.0) {

        depth = (depth + 1.0) / 2.0;

        float closestDepth = texture(shadowmap, depth.xy).r;
        float currentDepth = depth.z;

        if (currentDepth > closestDepth) {

            shadow = 1.0;
        }

    }

    return  (1.0 - shadow);

}

void main()
{
    vec3 lightcolor = vec3(.9, .9, .9);
    vec4 basecolor = texture(oTexture, TexCoord);


    vec3 ambient = 0.1 * lightcolor;

    vec3 lightDir = normalize(vec3(0, 0, 0) - FragPos);
    float diff = (dot(Normal, lightDir) + 1);
    vec3 diffuse =  1 + (diff * lightcolor * 0);



    float shadow = calculateshadow(fragposlight);

    vec3 result = (ambient + shadow)* diffuse * basecolor.xyz;

    Color = vec4(result, basecolor.w);

}