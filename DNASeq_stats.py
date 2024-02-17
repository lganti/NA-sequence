DNA_Seq = '>ATGTCTACAATCGACTAGG'

count = 0
count_A = 0
count_T = 0
count_C = 0
count_G = 0

if DNA_Seq[0] == '>':
    DNA_Seq = DNA_Seq.replace('>', '')

    for letter in DNA_Seq :
        if letter == 'A' :
            count_A += 1
            count += 1
        elif letter == 'T' :
            count_T += 1
            count += 1
        elif letter == 'C' :
            count_C += 1
            count += 1
        elif letter == 'G' :
            count_G += 1
            count += 1
        else :
            break
    print('DNA Base pair stats:')
    print('Total nuber of base pairs in the input:', count)
    print('A:', count_A)
    print('T:', count_T)
    print('C:', count_C)
    print('G:', count_G)

    GC_content = (count_G + count_C) / (count_A + count_T + count_G + count_C) * 100
    print('GC content of the input sequence is:', round (GC_content, 1), '%')
else :
    print('Input sequence is not in fasta format; Re enter fasta sequence')




