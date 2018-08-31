import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from Spectrometer import Spectrometer
from multiprocessing import Pool

class IonSimulator():
    def __init__(self):
        self.delta_t = 10**-8
        self.spect_length = 0.2
        self.spectrometer = Spectrometer(z_min=-0.1,z_max=0.1,E_max=1000,delay=500*10**-9,ramp=200*10**-9)
        self.particle_charge_C = 1
        self.particle_mass_amu = 1
        self.e_charge = 1.602*10**-19 #in Coulombs
        self.amu_to_kg = 1.66054*10**-27
        self.au_to_momentum = 1.992852*10**-24
        self.KE_Initial_eV = 1
        self.n_particles = 100
        self.data = pd.DataFrame(np.zeros((self.n_particles,7)), columns=['x','y','z','vx','vy','vz','tof'])
        self.ai = 0
        self.polyFitX = []
        self.polyFitY = []
        self.fitCoefs = 0
        self.normalCoefs = 0
        self.Initialize()

    def Initialize(self):
        self.phi = np.random.rand(self.n_particles)*2*np.pi
        self.theta = np.arccos(1-2*np.random.rand(self.n_particles))
        self.KE_Initial_J = self.KE_Initial_eV * self.e_charge
        self.Vo_T = np.sqrt(2*self.KE_Initial_J/(self.amu_to_kg*self.particle_mass_amu))
        self.data['vx'] = self.Vo_T*np.sin(self.theta)*np.cos(self.phi)
        self.data['vy'] = self.Vo_T*np.sin(self.theta)*np.sin(self.phi)
        self.data['vz'] = self.Vo_T*np.cos(self.theta)
        self.data['x'] = (np.random.rand(self.n_particles)*2-1)*10**-3
        self.data['y'] = (np.random.rand(self.n_particles)*2-1)*10**-3
        self.data['z'] = (np.random.rand(self.n_particles)*2-1)*10**-3
        self.data['tof'] = np.zeros(self.n_particles)
        
    def Simulate(self):
        self.Initialize()
        initial_momentum_z_au = self.Get_Pz_o()
        for particle in self.data.index:
            self.Increment(particle)
        self.fitCoefs = np.polyfit(self.data['tof'],initial_momentum_z_au,3)
        print('Poly fit: {0:.2f} + {1:.2f}t + {2:.2f}t**2 + {3:.2f}t**3'.format(self.fitCoefs[3],self.fitCoefs[2],self.fitCoefs[1],self.fitCoefs[0]))
        self.normalCoefs = np.poly1d(self.fitCoefs)
        self.polyFitX = np.linspace(np.amin(self.data['tof']),np.amax(self.data['tof']),50)
        self.polyFitY = self.normalCoefs(self.polyFitX)
    
    def Get_Pz_o(self):
        return self.Vo_T*np.cos(self.theta)*self.particle_mass_amu*self.amu_to_kg/self.au_to_momentum
    
    def Increment(self,particle):
        time_steps = 0
        while self.data.at[particle,'z'] < self.spectrometer.z_max:
            ai = self.spectrometer.Get_E_Field(self.data.at[particle,'z'],self.delta_t*time_steps)*self.particle_charge_C*self.e_charge/(self.particle_mass_amu*self.amu_to_kg)
            ai_next = self.spectrometer.Get_E_Field(self.data.at[particle,'z'],self.delta_t*(time_steps+1))*self.particle_charge_C*self.e_charge/(self.particle_mass_amu*self.amu_to_kg)
            self.data.at[particle,'z'] += self.data.at[particle,'vz']*self.delta_t + 0.5*ai*self.delta_t**2
            self.data.at[particle,'vz'] += 0.5*(ai + ai_next)*self.delta_t
            self.data.at[particle,'x'] += self.data.at[particle,'vx']*self.delta_t
            self.data.at[particle,'y'] += self.data.at[particle,'vy']*self.delta_t
            time_steps += 1
            if self.data.at[particle,'z'] < self.spectrometer.z_min:
                self.data.at[particle,'z'] = np.NaN
                break
        final_time_step = (self.spect_length - self.data.at[particle,'z'])/self.data.at[particle,'vz']
        self.data.at[particle,'x'] += self.data.at[particle,'vx']*final_time_step
        self.data.at[particle,'y'] += self.data.at[particle,'vy']*final_time_step
        self.data.at[particle,'tof'] = self.delta_t*time_steps + final_time_step
        
    def SetCharge(self,charge):
        self.particle_charge_C = charge
        
    def SetMass(self,mass):
        self.particle_mass_amu = mass
        
def unwrap_self_f(arg, **kwarg):
    return IonSimulator.Increment(*arg, **kwarg)

# if __name__ == '__main__':
#     __spec__ = "ModuleSpec(name='builtins', loader=<class '_frozen_importlib.BuiltinImporter'>)"
#     sim = IonSimulator()
#     sim.Simulate()
#     plt.xlabel('tof ($\mu$s)')
#     plt.ylabel('pos (mm)')
#     plt.plot(sim.data['tof']*10**6,np.sqrt(sim.data['x']**2 + sim.data['y']**2)*10**3,'r.')

