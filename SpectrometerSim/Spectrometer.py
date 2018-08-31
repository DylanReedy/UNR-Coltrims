class Spectrometer:
    
    def __init__(self,z_min=0,z_max=0,E_max=0,delay=0,ramp=0):
        self.z_min = z_min #in m
        self.z_max = z_max #in m
        self.E_max = E_max  #in Volts/m
        self.ramp = ramp  #in s
        self.delay = delay  #in s
        
    def Get_E_Field(self,current_z_position,current_time):        
        if current_z_position > self.z_max or current_z_position < self.z_min:
            return 0
        if current_time < self.delay:
            return 0
        elif current_time < self.ramp + self.delay:
            return (current_time - self.delay)*self.E_max/self.ramp
        else:
            return self.E_max

