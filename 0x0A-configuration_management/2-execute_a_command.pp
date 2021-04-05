# kill a process named killmenow
exec { 'kilmenow':
    command => 'pkill -f killmenow',
    path    => '/usr/bin',
}  
