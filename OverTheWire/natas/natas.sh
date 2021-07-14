curl "http://natas"$1".natas.labs.overthewire.org" -H "Authorization: Basic `echo -n "natas$1:$2" | base64`"
