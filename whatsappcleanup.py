import re
import csv


def msg_cleaner(msg):
#makes sure msg is clean (not blank, not lots a spaces, has letter )
    if re.search("^[^a-zA-Z]*$", msg) == None: 
        return msg.strip('\n')
    return None


csv_data = [] #[[sender, msg]]
raw_txt= open('gc_data.txt', 'r', encoding="utf8")
c = 0

for line in raw_txt:
    if re.search("^[BGJEKOYM][a-z]* [MBPLTAV][a-z]*:", line) != None:
        line_split = re.split(":", line, 1)#one
        sender, msg = line_split[0].strip('\n'), line_split[1].strip('\n') #regex exp allows for assuption
        msg_clean = msg_cleaner(msg)

        if msg_clean != None: 
            #write
            csv_data.append([sender, msg_clean])
            #print('Line {1} written---{0}.'.format(line, c))
        else:
            #dont write
            print('Line {1} passed 1 not written-!-{0}.'.format(line, c))
            print('Line {1} msg--{1}.'.format(c, msg))

    else:
            #dont write
            print('Line {1} not passed 1 not written-!-{0}.'.format(line, c))
            print('Line {1} from sender{2}--{1}.'.format(c, msg, sender))
    c+=1
#end

#acctualy write the file
with open('gc_data.csv', 'w', newline='', encoding='utf') as file:
    writer = csv.writer(file, delimiter=',')
    b=0 
    for row in csv_data:
        writer.writerow(row)
        b+=1

print("{0} Rows written of {1}".format(b, c))
print("{0}% data loss".format(round((((c-b)/c)*100),1)))
