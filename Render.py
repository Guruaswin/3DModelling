from Chair import *
from OpenGL.GL import *

def Chair():
    glBegin(GL_LINES)
    for edge in chair_edges_vector2:
        for vertex in edge:
            glVertex3fv(chair_vertices_vector3[vertex])
    glEnd()

    glBegin(GL_QUADS)
    for face in chair_faces_vector4:
        x = 0;
        for vertex in face:
            x+=1
            glColor3fv(colors[x])        
            glVertex3fv(chair_vertices_vector3[vertex])
    glEnd()        