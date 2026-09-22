#!/usr/bin/python3
"""Learning or Reviewing about Lists | by Alta3 Research"""

def main():
    ## create an empty list
    myemptylist = []    # myemptylist = list()

    ## add to our list with a list method
    ## The extend method will add every item to the list
    myemptylist.extend(['192.168.102.55', '10.0.0.1', '172.4.4.3'])
    myemptylist.extend(['i am second'])
    myemptylist.extend(['bringing up the rear!'])

    ## display our list
    print(myemptylist)

if __name__ == "__main__":
    main()
