local Population = require "Population"
local Electron = require "Electron"

simion.workbench_program()

adjustable _cathode  = -10
adjustable _grid  = -10
adjustable _anode1 = 0--8
adjustable _anode2 = 0--80
adjustable _anode3 = 0--30
adjustable _anode4 = 0--10
adjustable _anode5 = 0--6
adjustable _anode6 = 0
adjustable _sweeper = 0
adjustable _bz_gu = 0
--adjustable _omega = 3.14*10^5
file = io.open("log_file.txt", "w")
n_runs_through_population = 0 -- iterate through the individuals in the current population (generation)
n_runs_through_generations = 0 -- iterate through number of generations
total_generations = 1000

testPopulation = Population(80)
currentIon = 0

function segment.initialize()
	q_over_m= (ion_charge * 1.602176487*10^(-19) ) /(ion_mass*1.66053886*10^(-27) )
	bz_tesla = _bz_gu * 0.0001

	--------------------------------------------------- --genetic algorithm stuff
	-- if ion_number == 1 then
		-- print("Initializing Run.")
		-- currentIon = 0
		-- n_runs_through_population = n_runs_through_population + 1
		-- print("Current Individual: " .. tostring(n_runs_through_population))
		-- if n_runs_through_population == 1 then
			-- n_runs_through_generations = n_runs_through_generations + 1
			-- if n_runs_through_generations > 1 then
				-- print("Calling Genetic Algorithms...")
				-- print("total population: " .. tostring(#testPopulation.Individuals))
				-- print("sample electron data: " .. tostring(testPopulation.Individuals[1].ElectronData))
				-- print("sample electron data: " .. tostring(testPopulation.Individuals[1].ElectronData.Electrons[1]))
				-- testPopulation:Selection()
				-- testPopulation:Crossover()
			-- end
		-- end

		-- print("Current Generation: " .. tostring(n_runs_through_generations))
		
	-- end
	
	-- _anode2 = testPopulation.Individuals[n_runs_through_population].genes[1]
	-- _anode3 = testPopulation.Individuals[n_runs_through_population].genes[2]
	-- _anode4 = testPopulation.Individuals[n_runs_through_population].genes[3]
	-- _anode5 = testPopulation.Individuals[n_runs_through_population].genes[4]
	-- _anode6 = testPopulation.Individuals[n_runs_through_population].genes[5]
	
	
	
	
		------------------------------------non genetic algorithm stuff

end

function segment.fast_adjust()

	adj_elect02 = _cathode
	adj_elect03 = _grid
	adj_elect04 = _anode1
	adj_elect05 = _anode2
	adj_elect06 = _anode3
	adj_elect07 = _anode4
	adj_elect08 = _anode5
	adj_elect11 = _anode6
	adj_elect12 = _sweeper --* sin(_omega * ion_time_of_flight)
	
end



function segment.accel_adjust()

	vx = ion_vx_mm * 1000
	vy = ion_vy_mm * 1000
	
	ionAxSI = (q_over_m * vy * bz_tesla)
	
	ion_ax_mm = ion_ax_mm + ( ionAxSI*10^(-9) )
	
	ionAySI = -(q_over_m * vx * bz_tesla)
	
	ion_ay_mm = ion_ay_mm + ( ionAySI*10^(-9) )
	
end
	
function segment.other_actions()

	sim_update_pe_surface = 1
	
	---------------------------------------------------------genetic algorithm stuff
	-- if ion_pz_mm < 120 then
		-- currentIon = currentIon + 1
		-- -- file:write("good ion number: " .. tostring(ion_number) .. "\n")
		-- ion_splat = 1
		-- elec = Electron()
		-- elec.Position.x = ion_px_mm
		-- elec.Position.y = ion_py_mm
		-- elec.Position.z = ion_pz_mm
		-- elec.Momentum.x = ion_vx_mm
		-- elec.Momentum.y = ion_vy_mm
		-- elec.Momentum.z = ion_vz_mm
		-- testPopulation.Individuals[n_runs_through_population].ElectronData.Electrons[currentIon] = elec
		-- -- file:write(tostring(testPopulation.Individuals[n_runs_through_population]) .. "\n")
		-- -- file:write(tostring(testPopulation.Individuals[n_runs_through_population].ElectronData) .. "\n")
		-- -- file:write(tostring(testPopulation.Individuals[n_runs_through_population].ElectronData.Electrons) .. "\n")
		-- -- file:write(tostring(testPopulation.Individuals[n_runs_through_population].ElectronData.Electrons) .. "\n")
		
		-- -- file:write("current individual electron count: " .. tostring(#testPopulation.Individuals[n_runs_through_population].ElectronData.Electrons) .. "\n")
	-- end
end
	
function segment.terminate()
	
	-------------------------------------------------------genetic algorithm stuff
	
	-- if ion_number == 1 then
		-- testPopulation.Individuals[n_runs_through_population]:EvaluateFitness()
		-- print("Ending Run. Evaluating fitness...")
		
		-- sim_rerun_flym = (n_runs_through_generations == total_generations and n_runs_through_population == #testPopulation.Individuals) and 0 or 1	
		-- print("sim_rerun_flym value: " .. tostring(sim_rerun_flym))
				
		-- if n_runs_through_population == #testPopulation.Individuals then
			-- n_runs_through_population = 0
		-- end
		
		-- if sim_rerun_flym == 0 then
			-- print("run done! ")
			-- testPopulation:GetFittest()
		-- end
		
		-- file:flush()
	-- end	

end

