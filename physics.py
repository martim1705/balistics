# equações do movimento
import math as m 

# constantes 

p = 1.2 # densidade do ar Kg/m^3
A = 0.5 # area do projetil (olhando-o de frente) m^2
C = 0.3 # coeficiente de arrasto 
mass = 0.056 # massa do objeto Kg
g = 9.81 # constante gravítica m/s^2
xi = 2.0
yi = 2.0
delta_t = 0.0033 # intervalo de tempo s 



# componentes da velocidade
vx = 4.0 # exemplo 
vy = 5.0 # exemplo


# vetores 
v_vec = (vx,vy)
# magnitude da velocidade do projetil 
v = m.sqrt(vx**2 + vy**2)

# constante D 
D = (p * A * C) / 2.0

# magnitude da força de arrasto / drag 
F = (D*v**2)

# vetor força de arrasto 

Fx = - (D * v * vx)
Fy = -(D * v * vy) 
Fv = (Fx,Fy)
# 2ª lei de Newton 
sum_forces_in_x = Fx
sum_forces_in_y = -(mass*g) + Fy

# aceleração 
ax = -(D/mass)*v*vx
ay = -g -(D/mass)*v*vy

# mudança da coordernada em x e em y

delta_x = vx*delta_t + (ax * (delta_t**2))/2
delta_y = vy*delta_t + (ay * (delta_t**2))/2

# coordenada no ponto final do intervalo de tempo 

final_x = xi + delta_x
final_y = yi + delta_y
