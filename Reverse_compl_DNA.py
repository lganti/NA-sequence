input_seq = 'ATGCTAGCGGTACATGCCTA'

print (input_seq)

reverse_seq = input_seq [::-1]
print (reverse_seq)

rev_comp_seq = []
for x in reverse_seq :
    if x == 'A' :
        rev_comp_seq.append('T')
        #print (x)
        #rev_comp_seq = x
        #print (rev_comp_seq)
    elif x == 'T' :
        rev_comp_seq.append('A')
        #print (x)
        #rev_comp_seq = x
        #print(rev_comp_seq)
    elif x == 'C' :
        rev_comp_seq.append('G')
        #print (x)
        #rev_comp_seq = x
        #print(rev_comp_seq)
    elif x == 'G' :
        rev_comp_seq.append('C')
        #print (x)
        #rev_comp_seq = x
        #print(rev_comp_seq)

#    return ''.join(rev_comp_seq)
print (''.join(rev_comp_seq))