import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from Spectrometer import Spectrometer

class IonSimulator():
    def __init__(self):
        self.delta_t = 10**-9
        self.spect_length = 0.2
        self.spectrometer = Spectrometer(z_min=-0.1,z_max=0.1,E_max=1000,delay=500*10**-9,ramp=200*10**-9,charge=1,mass=1)
        self.q = 1.602*10**-19 #in Coulombs
        self.m = 3.01071942*10**-26 #in kilograms; ~ water
        self.KE_Initial_eV = 1
        self.KE_Initial_J = self.KE_Initial_eV * self.q
        self.Vo_T = (2*self.KE_Initial_J/self.m)**0.5
        self.n_particles = 100
        self.data = pd.DataFrame(np.zeros((self.n_particles,7)), columns=['x','y','z','vx','vy','vz','tof'])
        self.phi = np.random.rand(self.n_particles,1)*2*np.pi
        self.theta = np.arccos(1-2*np.random.rand(self.n_particles,1))
        self.data['vx'] = self.Vo_T*np.sin(self.theta)*np.cos(self.phi)
        self.data['vy'] = self.Vo_T*np.sin(self.theta)*np.sin(self.phi)
        self.data['vz'] = self.Vo_T*np.cos(self.theta)
        self.data['x'] = (np.random.rand(self.n_particles)*2-1)*10**-3
        self.data['y'] = (np.random.rand(self.n_particles)*2-1)*10**-3
        self.data['z'] = (np.random.rand(self.n_particles)*2-1)*10**-3
        self.data['tof'] = np.zeros(self.n_particles)
        self.ai = 0
        self.polyFitX = []
        self.polyFitY = []

    def Initialize(self):
        self.phi = np.random.rand(self.n_particles,1)*2*np.pi
        self.theta = np.arccos(1-2*np.random.rand(self.n_particles,1))
        self.data['vx'] = self.Vo_T*np.sin(self.theta)*np.cos(self.phi)
        self.data['vy'] = self.Vo_T*np.sin(self.theta)*np.sin(self.phi)
        self.data['vz'] = self.Vo_T*np.cos(self.theta)
        self.data['x'] = (np.random.rand(self.n_particles)*2-1)*10**-3
        self.data['y'] = (np.random.rand(self.n_particles)*2-1)*10**-3
        self.data['z'] = (np.random.rand(self.n_particles)*2-1)*10**-3
        self.data['tof'] = np.zeros(self.n_particles)
        
    def Simulate(self):
        self.Initialize()
        for particle in self.data.index:
            self.Increment(particle)
        fitCoefs = np.polyfit(self.data['tof']*10**6,np.sqrt(self.data['x']**2 + self.data['y']**2)*10**3,4)
        normalCoefs = np.poly1d(fitCoefs)
        self.polyFitX = np.linspace(np.amin(self.data['tof'])*10**6,np.amax(self.data['tof'])*10**6,50)
        self.polyFitY = normalCoefs(self.polyFitX)

    def Increment(self,particle):
        time_steps = 0
        while self.data.at[particle,'z'] < self.spect_length:
            ai = self.spectrometer.GetAccel(self.data.at[particle,'z'],self.delta_t*time_steps)
            self.data.at[particle,'z'] += self.data.at[particle,'vz']*self.delta_t + 0.5*ai*self.delta_t**2
            self.data.at[particle,'vz'] += 0.5*(ai + self.spectrometer.GetAccel(self.data.at[particle,'z'],self.delta_t*time_steps))*self.delta_t
            self.data.at[particle,'x'] += self.data.at[particle,'vx']*self.delta_t
            self.data.at[particle,'y'] += self.data.at[particle,'vy']*self.delta_t
            time_steps += 1
        self.data.at[particle,'tof'] = self.delta_t*time_steps

#sim = IonSimulator()
#sim.Simulate()
##
#plt.xlabel('tof ($\mu$s)')
#plt.ylabel('pos (mm)')
#plt.plot(sim.data['tof']*10**6,np.sqrt(sim.data['x']**2 + sim.data['y']**2)*10**3,'r.')
#
