def main():
    print('''
        Once upon a time, there is a special agent named Maggie
        Sommers.  Day in and day out, she goes on dangerous missions 
        and serving her country.  But today, her boss and mom, Ai Mei 
        Chong gives her day off, effective immediately. 
        Our story takes place the following morning, when her alarm 
        rings.  Maggie is the kind of gal that wants to do something
        meaningful with her day, so it\'s up to you what happens next:
        ''')
    
    numPlastics = input(
                        '''
                            Did you recycle a a.) large, b.) little,
                        or c.) no amount of plastics this week?
                        Type large, little, or no.
                        '''
                        )
    
    toMoveOn1 = decision1(numPlastics)

    numPaper = input(
                        '''
                            Did you recycle a a.) large, b.) little,
                        or c.) no amount of paper this week?
                        Type large, little, or no.
                        '''
    )
    
    decision2(numPaper,toMoveOn1)

    print("To be continued...")

def decision1(plastics):
    if plastics.casefold() == 'large':
        print(
            '''
                Maggie enthusiatically turned off her alarm and got up, feeling rebellious.
                "I think I am going to make my own mission," she said to herself.
                With that in mind, she got out of bed and went to get ready
                for the day.
            '''
        )
        return True
    elif plastics.casefold() == 'little':
        print(
            '''
                Maggie sighed and hesitated a bit
                before she turned off the alarm.
                "Nothing to do," she whispered to herself,
                "Dunno if I should get up for this."
                Maggie laid down on the bed, trying to decide.
            '''
        )
        return True
    else:
        print('Maggie groaned, pressed snooze and went back to sleep. The end')
        return False

def decision2(paper, nextSection):
    if paper.casefold() == 'large' and nextSection == True:
        print(
            '''
                Maggie was reviewing some backlog files to see if there was anything
                interesting to do.
                "Hm, missing formula from a university science lab," she muttered to herself,
                "I got a bad feeling about this."
                With that said, Maggie picked up a notebook and started jotting down some
                notes.
            '''
        )
        return True
    elif paper.casefold() == 'little' and nextSection == True:
        print(
            '''
                After debating to herself, Maggie finally got up
                and got dressed.
                "Nothing to do," she whispered to herself,
                "Dunno if I should get up for this."
                Maggie laid down on the bed, trying to decide.
            '''
        )
        return True
    else:
        print(
                '''
                    After recalling that her boss and MOM gave her the day off, 
                    Maggie sighed, she knew better than to disobey orders.
                ''')
        return False

if __name__ == '__main__':
    main()