from dataclasses import dataclass

@dataclass
class Motor:
    """
    Class to describe DC motor parameters

    Units:
    max_torque - mNm
    max_current - A
    torque_constant - mNm/A
    speed_constant - rpm/V
    rotor_intertia - gcm^2
    """
    part_num: int
    max_torque: int
    max_current: float
    torque_constant: float 
    speed_constant: float
    rotor_intertia: int

@dataclass
class Wheel:
    """
    Class to describe wheel parameters

    Units:
    radius - m
    """
    radius: float
    coef_friction: float

@dataclass
class Body:
    """
    Class to describe robot body parameters
    """
    radius: float
    mass: float