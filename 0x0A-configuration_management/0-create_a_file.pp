# This manifest creates a file in /tmp that fulfills certain requirements

file { '/tmp/school':
  content => 'I love Puppet',
  group   => 'www-data',
  owner   => 'www-data',
  mode    => '0744',
}
