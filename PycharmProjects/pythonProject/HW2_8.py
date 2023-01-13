#!/usr/bin/env python

seq = open("/home/admin27/mg2022/HW2/HW2_8_BRCA2_DNA_seq.txt",'r')

seq_file =str(seq.readlines())

dna_f = ""
for i in seq_file:
        if i.isalpha() and i != 'n':
                dna_f = dna_f + i
dna_f = dna_f[1:]

dna = open('/home/admin27/mg2022/HW2/BRCA2_DNA.txt','w')

print(dna_f, file=dna)

dna.close()

frame1 = []
frame2 = []
frame3 = []
frame2 += [dna_f[0]]
frame3 += [dna_f[0:2]]

frame1 += [dna_f[i:i+3] for i in range(0,len(dna_f),3)]
frame2 += [dna_f[i:i+3] for i in range(1,len(dna_f)-1,3)]
frame3 += [dna_f[i:i+3] for i in range(2,len(dna_f)-2,3)]

comp = ""
for i in dna_f:
        if i == 'a':
                comp += 't'
        elif i == 't':
                comp += 'a'
        elif i == 'g':
                comp += 'c'
        elif i == 'c':
                comp += 'g'

rev = "".join(reversed(comp))

frame_1 = []
frame_2 = []
frame_3 = []

frame_2 += [rev[0]]
frame_3 += [rev[0:2]]

frame_1 += [rev[i:i+3] for i in range(0,len(rev),3)]
frame_2 += [rev[i:i+3] for i in range(1,len(rev)-1,3)]
frame_3 += [rev[i:i+3] for i in range(2,len(rev)-2,3)]

frame = [frame1,frame2,frame3,frame_1,frame_2,frame_3]
check =0
change_frame = []
for seq_str in frame:
        i=0
        check_status =0
        while i < len(seq_str):
                if seq_str[i]  == 'atg' and check_status == 0:
                        start = i
                        check_status = 1
                elif check_status ==1 and (seq_str[i]  == 'tag' or seq_str[i]  == 'tga' or seq_str[i] == 'taa'):
                        end = i
                        break
                i += 1
        seq = seq_str[start:end+1]
        change_frame.append(seq_str)

a=0
longest_lst = []

frame_num = ['+1','+2','+3','-1','-2','-3']
while a < len(change_frame):
        if len(longest_lst) < len(change_frame[a]):
                longest_lst = change_frame[a]
                longest_index = a
        print('FRAME',frame_num[a],' '.join(change_frame[a]).upper())
        a += 1

print('The long FRAME is : ')
print('FRAME',frame_num[longest_index],' '.join(longest_lst).upper())