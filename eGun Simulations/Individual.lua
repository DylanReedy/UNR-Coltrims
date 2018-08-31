local Individual = {}
local ElectronData = require("ElectronData")
local math = require("math")
Individual.__index = Individual

setmetatable(Individual, {
  __call = function(cls, ...)
    return cls.Create(...)
  end,
})

function Individual.Create(seed)
  local self = setmetatable({},Individual)
  self.numberOfGenes = 5
  self.MinimumGeneValue = 0
  self.MaximumGeneValue = 500
  self.ElectronData = ElectronData()
  self.Fitness_ElectronCount = 0
  self.Fitness_SpotSize = 0
  self.Fitness_Divergence = 0
  self.Fitness_Sum = 0
  self.genes = {}
  math.randomseed(seed)
  for x = 1,self.numberOfGenes do
	self.genes[x] = math.random(self.MinimumGeneValue,self.MaximumGeneValue)
  end
  self:EvaluateFitness()
  return self
end

-- function Individual.SetElectronData(data)
	-- assert(type(ElectronData()) == type(data))
	-- self.electronData = data
-- end

function Individual:EvaluateFitness()
	--need actual fitness equations here
    self.Fitness_SpotSize = self.ElectronData:GetSpotSize() / 50
    self.Fitness_Divergence = self.ElectronData:GetPerpendicularVelocityRatio() / .2
	self.Fitness_Sum = self.Fitness_Divergence + self.Fitness_SpotSize
end

return Individual

