class Spectrometer:
    
    def __init__(self,z_min=0,z_max=0,E_max=0,delay=0,ramp=0,charge=1,mass=1):
        self.z_min = z_min
        self.z_max = z_max
        self.z_max = z_max #in m
        self.E_max = E_max  #in Volts/m
        self.ramp = ramp  #in s
        self.delay = delay  #in s
        self.charge_in_e = charge #in e
        self.mass_in_amu = mass
        
    def Mass_In_KG(self):
        return self.mass_in_amu*1.67*10**-27
    
    def Charge_In_C(self):
        return self.charge_in_e*1.602*10**-19

    def E_Field_at_t(self,current_time):
        
        if current_time < self.delay:
            return 0
        elif current_time < self.ramp + self.delay:
            return (current_time - self.delay)*self.E_max/self.ramp
        else:
            return self.E_max

    def GetAccel(self,pos,t):
        field = self.E_Field_at_t(t)
        if pos >= self.z_min and pos <= self.z_max:
            accel = self.Charge_In_C()*field/self.Mass_In_KG()
        else:
            accel = 0
        return accel

