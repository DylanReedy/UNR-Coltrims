local Electron = require "Electron"

-- function string.notstarts(String,Start)
   -- return string.sub(String,1,string.len(Start))~=Start
-- end

-- function string.ends(String,End)
   -- return End=='' or string.sub(String,-string.len(End))==End
-- end

local ElectronData = {}
ElectronData.__index = ElectronData

setmetatable(ElectronData,{
  __call = function(cls, ...)
    return cls.Create(...)
  end,
})

function ElectronData.Create()
  local self = setmetatable({},ElectronData)
  self.Electrons = {}
  return self
end

function ElectronData:GetSpotSize()
  local minValue = 500
  local maxValue = -500
  for x=1,#self.Electrons do
	if self.Electrons[x].Position.x > maxValue then
		maxValue = self.Electrons[x].Position.x
	end
	if self.Electrons[x].Position.y > maxValue then
		maxValue = self.Electrons[x].Position.y
	end
	if self.Electrons[x].Position.x < minValue then
		minValue = self.Electrons[x].Position.x
	end
	if self.Electrons[x].Position.y < minValue then
		minValue = self.Electrons[x].Position.y
	end
  end
  return maxValue-minValue
end

function ElectronData:GetElectronFlux()
  return #self.Electrons
end

function ElectronData:GetPerpendicularVelocityRatio()
	local vperp_sum = 0
	for x=1,#self.Electrons do
		vperp_sum = vperp_sum + (self.Electrons[x]:V_Perpendicular()/self.Electrons[x]:V_Total())
    end
    
	return vperp_sum / self:GetElectronFlux()
end

return ElectronData
