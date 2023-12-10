# Deos the same thing in task 2 except in puppet

file { '/root/.ssh/.ssh_config':
  ensure  => file,
  content => "Host 75667-web-01\n\tHostName 54.146.81.93\n\tUser ubuntu\n\tIdentityFile ~/.ssh/school\n\tPasswordAuthentication no\n",
}
