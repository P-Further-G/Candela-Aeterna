#version 330

in vec2 TexCoord;
in vec3 Normal;
in vec3 FragPos;
in vec2 poz;

uniform sampler2D oTexture;

out vec4 Color;


void main()
{
    vec4 basecolor = texture(oTexture, TexCoord);

    vec3 lightDir = normalize(vec3(0, 10, 10) - FragPos);

    vec4 diff = (dot(Normal, lightDir) + 1.0) * vec4(0.5, 0.5, 0.5, 0.5);

    vec4 color = (diff * basecolor);

    vec4 finalcolor = color;

    Color = min(vec4(1.0, 1.0, 1.0, 1.0), finalcolor);


}