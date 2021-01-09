#This is the main file. Change import to the name of the file desired to run on this data (i.e. foodBankMOG, foodBankLP).
#If attempting to run capacityAllocationLP, add addedCapacity as an argument in the fb.main() call
#LPs need Gurobipy installed
import capacityAllocationLP as fb
import random

def main():
    #Initialize predetermined variables
    supply = 1700000
    capacity = [136623, 14700, 129546, 71980, 76316, 52536, 113140, 89188, 46673, 47568, 40391, 44284, 62410, 34506,
                102663, 119979, 50237, 70136, 277622, 49002, 71118, 10305, 32563, 87649, 99092, 82854, 126447, 145599,
                58713, 140958, 142910, 140709, 117600, 87229, 51116, 124094, 19837, 126328, 12255, 148262, 75962, 58323,
                91208, 46538, 71937, 129929, 85124, 42054, 72728, 120171, 139312, 48970, 120207, 144803, 59662, 83437, 94926,
                216102, 37187, 33700, 93332, 52984, 137926, 104902, 37343, 89077, 76994, 66074, 127934, 90480, 140133, 59650,
                45329, 61434, 61835, 64812, 82972, 14408, 139786, 143630, 47301, 30395, 56469, 56368, 119228, 64745, 41418,
                46917, 62480, 60201, 59233, 54902, 246719, 291318, 86382, 130868, 137089, 65061, 110755, 46295, 66626, 72299,
                40160, 67908, 85875, 134659, 93693, 91317, 60624, 280602, 50405, 57291, 141081, 47260, 35704, 216225, 64950,
                132021, 126573, 132742, 33149, 78848, 56201, 33270, 142742, 52006, 44888, 101175, 113229, 143216, 113701,
                115500, 100945, 104437, 95952, 52782, 98034, 17014, 64538, 122348, 144104, 107432, 106271, 134468, 104892,
                108478, 38450, 93312, 34165, 37565, 130120, 129537, 63613, 205703, 123319, 44379, 58805, 51852, 57663, 81760,
                9002, 41107, 115787, 288538, 124379, 137187, 80913, 123219, 116845, 108739, 100275, 118236, 76070, 105152,
                226464, 111715, 109561, 231470, 51107, 261991, 121792, 69540, 38488, 40975, 250816, 115640, 120817, 45997,
                97011, 87606, 70205, 56468, 81050, 58324, 141706, 197864, 58492, 107948, 132713, 13248, 68607, 166709, 176119,
                118526, 132689, 91107, 60045, 32703, 89108, 149404, 79792, 59525, 58990, 93363, 61574, 141218, 45054, 144962,
                58208, 82718, 192803, 16803, 52854, 41234, 130853, 42411, 49977, 125955, 121410, 42931, 63330, 73131, 70560,
                148741, 147698, 79375, 124778, 35286, 43026, 145961, 59571, 43847, 35019, 58314, 130867, 144261, 178479, 48897,
                129324, 79954, 124891, 41673, 78120, 54526, 43826, 52619, 78720, 141745, 144247, 117461, 96906, 108900, 250881,
                78429, 31313, 124758, 180796, 56106]
    demand = []
    equalityLimit = 0.0001
    agencies = []
    populations = [1019285, 885708, 30257, 13054, 58098, 33138, 27617, 9028, 16145]
    povertyRates = [0.134, 0.128, 0.076, 0.032, 0.042, 0.061, 0.067, 0.067, 0.044]
    totalPop = sum(populations)
    
    #optional variable
    addedCapacity = 500000

    #Populate agencies array with population percents, to use to proportionally distribute amount of agencies.
    #We use the fraction of population to indicate the fraction of the 268 agencies the region gets.
    for pop in populations:
        agencies.append(round((pop/totalPop)*268))
    
    #Populate demand array with demand rate for a region, the amount of times according to the amount of agencies. Each index represents an agency.
    for i in range(len(agencies)):
        demand += [(populations[i]*povertyRates[i])/agencies[i]]*agencies[i]

    #Call function
    fb.main(supply, capacity, demand, equalityLimit, addedCapacity)

if __name__ == "__main__":
    main()