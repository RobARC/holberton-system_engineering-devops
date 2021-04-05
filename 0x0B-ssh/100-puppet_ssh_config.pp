#Using Puppet to make changes to our ssh configuration file
include stdlib

file { 'Turn off password auth':
  ensure => 'present',
  path   => '/etc/ssh/ssh_config',
  line   => 'PasswordAuthentication no'
}

file_line { 'Declare identity file':
  ensure => 'present',
  path   => '/etc/ssh/ssh_config',
  line   => 'IdentifyFile ~/.ssh/holberton'
}

