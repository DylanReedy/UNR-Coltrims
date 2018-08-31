function mergeSort(Array, firstIndex, lastIndex)
	print("hi from mergeSort. Array size: " .. tostring(#Array))
	if firstIndex < lastIndex then
		local midIndex = math.floor((firstIndex + lastIndex)/2)
		mergeSort(Array, firstIndex, midIndex)
		mergeSort(Array, midIndex+1, lastIndex)
		merge(Array, firstIndex, midIndex, lastIndex)
	end
	print("mergesort done. array values in order: ")
	for x=1,#Array do
		print("array values " .. tostring(Array[x].Fitness_Sum))
	end
end

function merge(Array, firstIndex, midIndex, lastIndex)
	print("hi from merge. Array:" .. tostring(#Array))

	for x=1,#Array do
		print("array values " .. tostring(Array[x].Fitness_Sum))
	end
	
	local leftArrayLength = midIndex-firstIndex+1
	local rightArrayLength = lastIndex-midIndex
	local leftArray = {}
	local rightArray = {}
	
	
	for i=1, leftArrayLength do
		leftArray[i] = Array[firstIndex+i-1]
	end
	for i=1, rightArrayLength do
		rightArray[i] = Array[midIndex+i]
	end
	
	leftArray[leftArrayLength+1] = math.huge
	rightArray[rightArrayLength+1] = math.huge
	
	local i=1
	local j=1
		
	for k=firstIndex, lastIndex do
		local valueLeft
		local valueRight
		if(type(leftArray[i])==type(1)) then
			valueLeft = leftArray[i]
		else
			valueLeft = leftArray[i].Fitness_Sum
		end
		if(type(rightArray[j])==type(1)) then
			valueRight = rightArray[j]
		else
			valueRight = rightArray[j].Fitness_Sum
		end
		if valueLeft <= valueRight then
			Array[k] = leftArray[i]
			i=i+1
		else
			Array[k] = rightArray[j]
			j=j+1
		end
	end

	-- normal merge loop
	-- for k=firstIndex, lastIndex do
		-- if leftArray[i]<=rightArray[j] then
			-- Array[k] = leftArray[i]
			-- i=i+1
		-- else
			-- Array[k] = rightArray[j]
			-- j=j+1
		-- end
	-- end
end

-- -- fill A with random numbers between 1 and 100
-- function randArray(A)
	-- for i=1, 100 do
		-- A[i] = math.random(100)
	-- end
-- end

-- -- print all the elements in the array A
-- function printArray(A)
	-- for i=1,#A do
		-- io.write(A[i] .. ", ")
	-- end
	-- io.write("\n")
-- end


-- A = {}

-- -- -- create the original array
-- randArray(A)
-- io.write("Original Array \n")
-- printArray(A)
-- io.write("\n")

-- -- -- sort the array
-- mergeSort(A, 1, #A)
-- io.write("Sorted Array \n")
-- printArray(A)