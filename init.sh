shownums() { for i in {A..D}; do echo -n $i && ls -l CM$i/ | wc -l; done }

alias deleteall='for i in {A..D}; do rm CM$i/*; done'
