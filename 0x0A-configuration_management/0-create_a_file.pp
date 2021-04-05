$content = 'I love Puppet'
file {
  '/tmp/holberton':
  owner   => www-data,
  group   => www-data,
  mode    => '0744',
  content => $content,
}
