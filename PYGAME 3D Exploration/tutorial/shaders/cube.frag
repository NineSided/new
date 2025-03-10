#version 330 core

uniform float mytime;

layout(location = 0) out vec4 fragColor;

void main() {
    vec3 color = vec3(1.0*sin(mytime), 0, 0);
    fragColor = vec4(color, 1.0);
}