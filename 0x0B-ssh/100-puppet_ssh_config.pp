# Deos the same thing in task 2 except in puppet

file { '/root/.ssh/.ssh_config':
  ensure  => file,
  content => "Host 75667-web-01\nHostName 54.146.81.93\nUser ubuntu\nIdentityFile ~/.ssh/school\nPasswordAuthentication no\n",
}
