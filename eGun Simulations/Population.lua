local Individual = require "Individual"
local MergeSort = require "Mergesort"

local Population = {}
Population.__index = Population

setmetatable(Population, {
	__call = function(cls, ...)
    return cls.Create(...)
  end,
})

function Population.Create(population)
	local self = setmetatable({},Population)
	self.Individuals = {}
	self.FittestIndividuals = {}
	self.numberOfIndividuals = population
	for x=1,self.numberOfIndividuals do
		seed = os.time() / x
		self.Individuals[x] = Individual(seed)
	end
	return self
end

function Population:EvaluateFitness()
	for x=1,self.numberOfIndividuals do
		self.Individuals[x]:EvaluateFitness()
	end
end

function Population:Selection()
	print("hi from selection")
	print("self.individuals: " .. tostring(self.Individuals))
	print("number of individuals: " .. tostring(#self.Individuals))
	mergeSort(self.Individuals, 1, #self.Individuals)
	--sort the population from fittest (1) to least fit (100)
end

function Population:Crossover()
	--currently this requires a population that's a multiple of 4.  needs to be generalized to take any population
	seed = os.time()

	math.randomseed(os.time())
	geneCutoff = math.random(1,self.Individuals[1].numberOfGenes-1)
	totalIndividuals = #self.Individuals

	for x=1,totalIndividuals/4 do
		firstChild = Individual(seed)
		secondChild = Individual(seed*2)
		for y=1,geneCutoff do
			firstChild.genes[y] = self.Individuals[x].genes[y]
			secondChild.genes[y] = self.Individuals[x+totalIndividuals/4].genes[y]
		end
		for y=geneCutoff+1,firstChild.numberOfGenes do
			firstChild.genes[y] = self.Individuals[x+totalIndividuals/4].genes[y]
			secondChild.genes[y] = self.Individuals[x].genes[y]
		end
		self.Individuals[x+totalIndividuals/2] = firstChild
		self.Individuals[x+3*totalIndividuals/4] = secondChild
	end
	--pick random gene value - for each pair of parents, swap genes up to that value. these new individuals are the offspring
	--2 parents create 2 new children, so the pop/2 fittest who survived selection restore the population to full
end

function Population:Mutation()
	--for each child, mutate each gene with random low probability. for this process, just generate a new random number for the potential
end

function Population:GetFittest()
	fittestIndex = 0
	fittestValue = 100
	for x=1,#self.Individuals do
		self.Individuals[x]:EvaluateFitness()
		if self.Individuals[x].Fitness_Sum < fittestValue then
			fittestIndex = x
		end
	end
	
	for x=1,#self.Individuals[fittestIndex].genes do
		print("gene " .. tostring(x) .. ": " .. tostring(self.Individuals[fittestIndex].genes[x]))
	end
	--find the fittest guy	
end

function Population:GetCount()
	return self.numberOfIndividuals
end

return Population