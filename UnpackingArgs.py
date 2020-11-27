def parrot(volage,state='a stiff',action='voom'):
    print("-- this parrot wouldn't ",action,end='')
    print("if you put ",volage,"volts through it ",end='')
    print("if yes put ",volage,"volts throw it",end='')
    print("E's",state,"!")
    d={"voltage":"4 million","state":"ka","action":"Voom"}
    print(**d)
parrot("4m")