# SHERLOCK AND DATES
for _ in range(int(input())):
    date = input().strip().split()
    if date[0]=='1':
        if date[1]==('January'):
            date[0]='31'
        elif date[1]==('May'):
            date[0]='30'
        elif date[1]==('July'):
            date[0]='30'
        elif date[1]==('October'):
            date[0]='30'
        elif date[1]==('December'):
            date[0]='30'
        elif date[1]==('February'):
            date[0]='31'
        elif date[1]==('April'):
            date[0]='31'
        elif date[1]==('June'):
            date[0]='31'
        elif date[1]==('August'):
            date[0]='31'
        elif date[1]==('September'):
            date[0]='31'
        elif date[1]==('November'):
            date[0]='31'
        elif date[1]=='March':
            y = int(date[2])
            if y%4==0:
                date[0]='29'
                if y%100==0 and y%400!=0:
                    date[0]='28'
            else:
                date[0]='28'
        if date[1]=='January':
            date[2] = str(int(date[2])-1)
            date[1]='December'
        elif date[1]=='February':
            date[1]='January'
        elif date[1]=='March':
            date[1]='February'
        elif date[1]=='April':
            date[1]='March'
        elif date[1]=='May':
            date[1]='April'
        elif date[1]=='June':
            date[1]='May'
        elif date[1]=='July':
            date[1]='June'
        elif date[1]=='August':
            date[1]='July'
        elif date[1]=='September':
            date[1]='August'
        elif date[1]=='October':
            date[1]='September'
        elif date[1]=='November':
            date[1]='October'
        elif date[1]=='December':
            date[1]='November'
    else:
        date[0] = str(int(date[0])-1)
    print(' '.join(date))

        
        
