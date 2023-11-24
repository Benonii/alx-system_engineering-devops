# This manifest installs flask from pip3

package { 'python3-pip':
  enusre => installed,
}

package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
  require  => Package['python3-pip'],
}
