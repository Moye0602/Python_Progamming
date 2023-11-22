from djitellopy import Tello
import time,keyboard
import pandas as pd
import schedule
from Admin import *
from icecream import *
lockspeed,speed,rotdegrees=True,20,5
trainingWheelsOff=1
telloRun=1
"""drone controls:
    ascend/descend q/w
    fwd/back "up"/"down"
    strafe left/right "left"/"right"   
    takeoff "9"
    land "3"
    flip "1"
    toggle speed "space"

"""

def drone_dynamics():
    #replace gyro requests with one request "tello.query_attitude"
    gyro={'pitch':tello.get_pitch(),
        'roll':tello.get_roll(),
        'yaw':tello.get_yaw(),
        'height':tello.get_height()}
    speed={'speed x':tello.get_speed_x(),
        'speed y':tello.get_speed_y(),
        'speed z':tello.get_speed_z()}
    accel={'acceleration x':tello.get_acceleration_x(),
        'acceleration y':tello.get_acceleration_y(),
        'acceleration z':tello.get_acceleration_z()}
    missionDist={'x dim':tello.get_mission_pad_distance_x(),
                 'y dim':tello.get_mission_pad_distance_y(),
                 'z dim':tello.get_mission_pad_distance_z()}
    print(gyro)
    return gyro,speed,accel,missionDist

def land_and_check():
    height=tello.get_height()
    tello.land()
    drop_speed=tello.get_speed_z()
    land_temp=tello.get_temperature()
    droptime=height/drop_speed
    time.sleep(droptime*1.05)
    tello.turn_motor_on()
    while land_temp>initial_state['amb temp']*1.15:
        land_temp=tello.get_temperature()
        time.sleep(5)
    tello.turn_motor_off()
    print('cooldown complete, current temp:',land_temp)

if telloRun and trainingWheelsOff:
    tello = Tello()
    SSID="bc:09:1b:e5:13:98"#"bc:09:1b:e5:13:98"#"60:60:1f:fd:0a:35"
    PASS="F0F597"#"FD0A35"
    #tello.connect_to_wifi(SSID,PASS)
    #tello.get_current_state()
    tello.connect()
    #print(tello.get_battery())
    initial_state={ 'Battery': tello.get_battery(),
                    'Baro':tello.get_barometer(),
                    'Height':tello.get_height(),
                    'amb temp':tello.get_temperature()
                    }
    print(f'Current State: {tello.get_current_state()}')
    print(f'Battery: {tello.get_battery()}%')
    print(tello.get_barometer(),'mmBar')
    print(tello.get_highest_temperature(),'Maxdegrees', tello.get_lowest_temperature(),'Mindegrees')
speed = 20
increase,rate_up=1.1,2
while telloRun:
    try:
        if trainingWheelsOff:
            time.time()
            schedule.every(1).seconds.do(drone_dynamics)
            height=tello.get_height()
            #print(height,height*'#')
            #if tello.get_distance_tof()<40:
            #    tello.move_back(20)
        forward,backwards=keyboard.is_pressed('up'),keyboard.is_pressed('down')
        rotLeft,rotRight=keyboard.is_pressed('a'),keyboard.is_pressed('d')
        left,right=keyboard.is_pressed('left'),keyboard.is_pressed('right')
        ascend,descend=keyboard.is_pressed('w'),keyboard.is_pressed('s')
        speedToggle=keyboard.is_pressed('space')
        lr, fb, ud, yv = 0, 0, 0, 0
        

        if keyboard.is_pressed("left"):
            lr = -speed
        elif keyboard.is_pressed("right"):
            lr = speed

        if keyboard.is_pressed("up"):
            fb = speed
        elif keyboard.is_pressed("down"):
            fb = -speed

        if keyboard.is_pressed("w"):
            ud = speed
        elif keyboard.is_pressed("s"):
            ud = -speed

        if keyboard.is_pressed("a"):
            yv = -speed
        elif keyboard.is_pressed("d"):
            yv = speed
        
        if speedToggle:
            if lockspeed:
                lockspeed=False          
                speed=100 
                lockspeed=100   
                rotdegrees=25       
            else:
                lockspeed=True
                speed=20
                lockspeed=20
                rotdegrees=5
            time.sleep(.15)# buffer needed to prevent rapid switching
            if trainingWheelsOff:
                
                tello.set_speed(speed)
            
        
        flip=keyboard.is_pressed('1')
        takeoff=keyboard.is_pressed('9')
        land=keyboard.is_pressed('3')
        LR={'left':left,'right':right}
        UD={'forward':forward,'back':backwards}
        user={'top':['ascend: '+str(ascend),'left: '+str(left),'rotLeft: '+str(rotLeft),'takeoff: '+str(takeoff),'lockspeed: '+str(lockspeed)],
            'mid':['forward: '+str(forward),'flip: '+str(flip),'backwards: '+str(backwards),'XXXX','speedToggle: '+str(speedToggle)],
            ' '*15+'bot':['descend: '+str(descend),'right: '+str(right),'rotRight: '+str(rotRight),'land: '+str(land),'speed: '+str(speed)]}

    #    user={'top':[ascend,left,flip,takeoff,lockspeed],aaaaaaaadaddaqqeeqqwwwwwsswaaassssdddddddssww
    #          'mid':[forward,'XXXX',backwards,'XXXX',speedToggle],
    #          'bot':[descend,right,'XXXX',land,speed  ]}


        #print('l:',left,'r:',right,'u:',forward,'d:',backwards,'flip:',flip)
        if any([left , right , forward , backwards]):
            
            direction={'left':left,'right':right,'forward':forward,'back':backwards}
            first_true_direction = None
            second_true_direction=None
            for dir in direction:
                if direction[dir] :
                    first_true_direction=dir
                    if first_true_direction in LR:
                        second=UD
                    else:
                        second=LR
                    
            
            for dir in second:
                if second[dir] and dir!=first_true_direction:
                    second_true_direction=dir
                    break
            if flip :
                if trainingWheelsOff:
                    tello.flip(first_true_direction)
            else:
                if trainingWheelsOff:
                    if 0:
                        if first_true_direction or second_true_direction=='forward':
                            tello.move_forward(speed)
                        if first_true_direction or second_true_direction=='back':
                            tello.move_back(speed)
                        if first_true_direction or second_true_direction=='left':
                            tello.move_left(speed)
                        if first_true_direction or second_true_direction=='right':
                            tello.move_right(speed)
                    if first_true_direction:
                        tello.move(first_true_direction,speed)
                        #increase*=rate_up
                        speed*=rate_up
                        if speed>500:
                            speed=500
                        elif speed<lockspeed:
                            speed=lockspeed
                    else:
                        speed/=rate_up**rate_up
                    tello.set_speed(speed)
                    if rotLeft:
                        ic()
                        tello.rotate_counter_clockwise(-rotdegrees)
                    if rotRight:
                        ic()
                        tello.rotate_counter_clockwise(+rotdegrees)
#################################################
                    if 0:
                        if second_true_direction!=None:
                            tello.move(second_true_direction,speed)
                        if any(second_true_direction=='left' or first_true_direction=='left'):
                            
                            tello.rotate_counter_clockwise(rotdegrees)
                        elif any(second_true_direction=='right' or first_true_direction=='right'):
                            tello.rotate_clockwise(rotdegrees)
#################################################
                    #tello.send_rc_control(lr, fb, ud, yv)
                #else:
                    print('move in direction:',first_true_direction,second_true_direction,'@ speed',speed)
        elif land:    
            if trainingWheelsOff:
                land_and_check()#3
            else:
                print('landing drone')
            break
        elif takeoff:
            if trainingWheelsOff:
                tello.takeoff()
            else:
                print('tello.takeoff()')#9

        df = pd.DataFrame(user)
        #if trainingWheelsOff:
        #    print(df,end="\033[F"*len(df))
    except :# Exception as error:
        pass#crayon(error)
        #tello.land()
    #time.sleep(.25)
    
