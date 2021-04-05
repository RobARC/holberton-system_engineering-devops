#create a manifest that kills a process named killmenow.
exec { "Kill":
 comand => 'usr/bin/pkill -9 killmenow',
}  
