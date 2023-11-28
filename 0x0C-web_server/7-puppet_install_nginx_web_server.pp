# Puppet file for installing nginx on the webserver

class mginx {
	package { 'nginx':
	  ensure => installed,
	}

	service { 'nginx':
	  ensure  => running,
	  enable  => true,
	  require => Package['nginx']
	}
}
include nginx
