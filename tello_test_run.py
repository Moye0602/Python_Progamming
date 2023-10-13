from djitellopy import Tello
import time,keyboard
import pandas as pd
import schedule
lockspeed,speed,rotdegrees=True,20,5
trainingWheelsOff=0
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

if 0 and  telloRun and trainingWheelsOff==0:
    tello = Tello()
    tello.connect()

    initial_state={ 'Battery': tello.get_battery(),
                'Baro':tello.get_barometer(),
                'Height':tello.get_height(),
                'amb temp':tello.get_temperature()
                                                                }
    print(f'Current State: {tello.get_current_state()}')
    print(f'Battery: {tello.get_battery()}%')
    print(tello.get_barometer())
    print(tello.get_highest_temperature(), tello.get_lowest_temperature())
while telloRun:
    if trainingWheelsOff:
        time.time()
        schedule.every(1).seconds.do(drone_dynamics)
        height=tello.get_height()
        if tello.get_distance_tof()<40:
            tello.move_back(20)
    forward,backwards=keyboard.is_pressed('up'),keyboard.is_pressed('down')
    rotLeft,rotRight=keyboard.is_pressed('a'),keyboard.is_pressed('d')
    left,right=keyboard.is_pressed('left'),keyboard.is_pressed('right')
    ascend,descend=keyboard.is_pressed('w'),keyboard.is_pressed('s')
    speedToggle=keyboard.is_pressed('space')
    
    if speedToggle:
        if lockspeed:
            lockspeed=False          
            speed=100    
            rotdegrees=25       
        else:
            lockspeed=True
            speed=20
            rotdegrees=5
        time.sleep(.15)# buffer needed to prevent rapid switching
        if trainingWheelsOff:
            tello.set_speed(speed)
        
    
    flip=keyboard.is_pressed('1')
    takeoff=keyboard.is_pressed('9')
    land=keyboard.is_pressed('3')
    LR={'l':left,'r':right}
    UD={'u':forward,'d':backwards}
    user={'top':['ascend: '+str(ascend),'left: '+str(left),'rotLeft: '+str(rotLeft),'takeoff: '+str(takeoff),'lockspeed: '+str(lockspeed)],
          'mid':['forward: '+str(forward),'flip: '+str(flip),'backwards: '+str(backwards),'XXXX','speedToggle: '+str(speedToggle)],
          ' '*15+'bot':['descend: '+str(descend),'right: '+str(right),'rotRight: '+str(rotRight),'land: '+str(land),'speed: '+str(speed)]}

#    user={'top':[ascend,left,flip,takeoff,lockspeed],aaaaaaaadaddaqqeeqqwwwwwsswaaassssdddddddssww
#          'mid':[forward,'XXXX',backwards,'XXXX',speedToggle],
#          'bot':[descend,right,'XXXX',land,speed  ]}


    #print('l:',left,'r:',right,'u:',forward,'d:',backwards,'flip:',flip)
    if any([left , right , forward , backwards]):
        
        direction={'l':left,'r':right,'u':forward,'d':backwards}
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
                tello.move(first_true_direction,speed)
                if second_true_direction!=None:
                    tello.move(second_true_direction,speed)
                if any(second_true_direction=='l' or first_true_direction=='l'):
                    
                    tello.rotate_counter_clockwise(rotdegrees)
                elif any(second_true_direction=='r' or first_true_direction=='r'):
                    tello.rotate_clockwise(rotdegrees)
            #else:
            #    print('move in direction:',first_true_direction,second_true_direction,'@ speed',speed)
    elif land:    
        if trainingWheelsOff:
            print('land_and_check()')#3
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
    print(df,end="\033[F"*len(df))
    
