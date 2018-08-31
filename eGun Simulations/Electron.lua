require "math"
local sqrt = math.sqrt

local Electron = {}
Electron.__index = Electron

setmetatable(Electron,{
  __call = function(cls, ...)
    return cls.Create(...)
  end,
})

function Electron.Create()
  local self = setmetatable({},Electron)
  self.Momentum = {}
  self.Momentum.x = 0
  self.Momentum.y = 0
  self.Momentum.z = 0
  self.Position = {}
  self.Position.x = 0
  self.Position.y = 0
  self.Position.z = 0
  return self
end

function Electron:V_Perpendicular()
  local vperp_square = self.Momentum.x*self.Momentum.x + self.Momentum.y*self.Momentum.y
  return sqrt(vperp_square)
end

function Electron:V_Parallel()
  local vpara_square = self.Momentum.z*self.Momentum.z
  return sqrt(vpara_square)
end

function Electron:V_Total()
	vtotal_square = self.Momentum.x*self.Momentum.x + self.Momentum.y*self.Momentum.y + self.Momentum.z*self.Momentum.z
    return sqrt(vtotal_square)
end

return Electron