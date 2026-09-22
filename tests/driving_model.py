import math

DEADZONE=0.12
TURN=3.25
DAMP=0.78

def clamp(v,a,b): return max(a,min(b,v))

def yaw_step(yaw,steer,throttle,speed):
    steer = clamp(steer,-1,1) if abs(steer)>=DEADZONE else 0
    throttle = clamp(throttle,-1,1) if abs(throttle)>=DEADZONE else 0
    if steer and (abs(throttle)>=DEADZONE or speed>0.015):
        reverse=-1 if throttle < -DEADZONE else 1
        factor=clamp(0.35+speed*2.5,0.35,1.0)
        yaw += steer*TURN*reverse*factor
    return yaw

def damp_lateral(yaw,vx,vz):
    r=math.radians(yaw)
    fx,fz=-math.sin(r),math.cos(r)
    longitudinal=vx*fx+vz*fz
    lx=vx-fx*longitudinal
    lz=vz-fz*longitudinal
    return (lx*(1-DAMP), lz*(1-DAMP), longitudinal)

left=yaw_step(0,-1,1,0.12)
right=yaw_step(0,1,1,0.12)
assert left < 0 < right
assert abs(left+right)<1e-9

rev_left=yaw_step(0,-1,-1,0.12)
rev_right=yaw_step(0,1,-1,0.12)
assert rev_left > 0 > rev_right

assert yaw_step(20,0,1,0.12)==20
assert yaw_step(20,1,0,0)==20

lx0,lz0,long0=damp_lateral(0,0.20,0.30)
assert abs(lx0) < 0.20
assert abs(lz0) < 1e-9
assert abs(long0-0.30)<1e-9

# Sweep meaningful steering states, not a maturity counter.
for yaw in (-170,-90,-30,0,30,90,170):
    for steer in (-1,-0.5,0,0.5,1):
        for throttle in (-1,-0.5,0,0.5,1):
            y=yaw_step(yaw,steer,throttle,0.1)
            assert math.isfinite(y)

print("driving_model: PASS")
print("coverage: forward-left, forward-right, reverse-left/right, straight, stationary, lateral damping")
