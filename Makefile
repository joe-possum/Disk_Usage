BINDIR = `echo ~/bin`

default :
	echo BINDIR=${BINDIR}

install :
	script-to-bin du-by-date.py ${BINDIR}
