# # differences
# # difference between the differences
# # then extrapolate 
# # ie if the sequence is going up by 1 2 3, the difference-difference is 1, and the difference-difference-difference is 0
# # go until zero, then extrapolate ending to sequence, and differeence sequences 
# # 
# # line2.position1 = line1.position2-line1.position1
# # 
# # 

####   --------------------------------------------------------------------------------  ###

# # quick logic sketch:

# eg = "23 34 50 94 210 482 1077 2327 4864 9829 19209 36438 67557 123497 224466 408029 743317 1354940 2461668 4436846 7899892"
# eg_list = eg.split()
# eg_list_int = []
# gap_list = []
# for i in eg_list:
#     eg_list_int.append(int(i))
# for i in range(len(eg_list_int)-1):
#     gap_list.append(eg_list_int[i+1] - eg_list_int[i])
# print(gap_list)

# # same applied to the resulting lines, maybe?



eg = "23 34 50 94 210 482 1077 2327 4864 9829 19209 36438 67557 123497 224466 408029 743317 1354940 2461668 4436846 7899892"
eg_list = eg.split()
eg_list_int = []
gap_list = []

for i in eg_list:
    eg_list_int.append(int(i))

gap_list = eg_list_int.copy()
gap_list_2d = [gap_list]

while any(gap != 0 for gap in gap_list):
    new_gap_list = [gap_list[i+1] - gap_list[i] for i in range(len(gap_list)-1)]
    gap_list_2d.append(new_gap_list)
    gap_list = new_gap_list

# print('gap_list','\n', gap_list_2d, '\n', 'gap_list')
last_num = []
next_gap = []
next_num = []

for i, gap_list in enumerate(gap_list_2d):
    # print(f"{i}: {gap_list}")
    # print(gap_list_2d[i][-1])
    last_num.append(gap_list_2d[i][-1])
    next_gap.append(gap_list_2d[i][-1])
    # print(next_gap)
for i in range(len(next_gap)):
        next_num.append(
            [next_gap[i] + last_num[i+1]]
            )
    
    # print(i,":", next_gap[i]) 
print(last_num)
print(next_gap)
print(next_num)

    
    
    
    

  
  
  
#   ////////////////////////////////////  //////////////////////////////////  

# from sklearn.linear_model import LinearRegression
     
    
    
# with open ('report.txt') as data:
#     lines = data.readlines()
#     int_lists = [list(map(int, line.split())) for line in lines]
#     # print(int_lists)
#     for sequence in int_lists:
#         differences = [sequence[i + 1] - sequence[i] for i in range(len(sequence)- 1)]
        
#         X = [[diff] for diff in differences]
#         y = differences
            
#         model = LinearRegression()
#         model.fit(X, y)
#         # print(model)
#         print("X:", X)
#         print("y:", y)


# with open('report.txt','r') as lines:
#     for line in lines:

# ////////////////////////////////////////////////////////////////////////////////////////////////




# def find_gaps(sequence):
#     gaps = [sequence[i + 1] - sequence[i] for i in range(len(sequence) - 1)]
#     print(gaps)
    
#     # Check if all differences are zero
#     if all(diff == 0 for diff in gaps):
#         return
    
#     find_gaps(gaps)

# # Example sequence
# eg = "23 34 50 94 210 482 1077 2327 4864 9829 19209 36438 67557 123497 224466 408029 743317 1354940 2461668 4436846 7899892"
# eg_list = [int(i) for i in eg.split()]

# # Start the recursive process
# find_gaps(eg_list)



