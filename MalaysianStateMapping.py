# Mapping the States of Malaysia with the State codes found in the NRIC

state_code_dictionary = {}

state_code_dictionary.update(dict.fromkeys([1,21,22,23,24], 'Johor'))
state_code_dictionary.update(dict.fromkeys([2,25,26,27], 'Kedah'))
state_code_dictionary.update(dict.fromkeys([3,28,29], 'Kelantan'))
state_code_dictionary.update(dict.fromkeys([4,30], 'Melaka'))
state_code_dictionary.update(dict.fromkeys([5,31,59], 'Negeri Sembilan'))
state_code_dictionary.update(dict.fromkeys([6,32,33], 'Pahang'))
state_code_dictionary.update(dict.fromkeys([7,34,35], 'Pulau Pinang'))
state_code_dictionary.update(dict.fromkeys([8,36,37,38,39], 'Perak'))
state_code_dictionary.update(dict.fromkeys([9,40], 'Perlis'))
state_code_dictionary.update(dict.fromkeys([10,41,42,43,44], 'Selangor'))
state_code_dictionary.update(dict.fromkeys([11,45,46], 'Terengganu'))
state_code_dictionary.update(dict.fromkeys([12,47,48,49], 'Sabah'))
state_code_dictionary.update(dict.fromkeys([13,50,51,52,53], 'Sarawak'))
state_code_dictionary.update(dict.fromkeys([14,54,55,56,57], 'Kuala Lumpur'))
state_code_dictionary.update(dict.fromkeys([15,58], 'Labuan'))
state_code_dictionary.update(dict.fromkeys([16], 'Putrajaya'))

def set_value(row_number, assigned_value): 
    return assigned_value[row_number]
