#Using Puppet to make changes to our ssh configuration file

file { 'Ensure file':
  ensure => 'present',
  path   => '/etc/ssh/ssh_config',
  mode   => '0644',
  owner  => 'root',
  group  => 'root'
}
file_line { 'Turn off password auth':
  ensure => 'present',
  path   => '/etc/ssh/ssh_config',
  line   => 'PasswordAuthentication no'
}
file_line { 'Declare identity file':
  ensure => 'present',
  path   => '/etc/ssh/ssh_config',
  line   => 'IdentifyFile ~/.ssh/holberton'
}
