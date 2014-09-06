SPEC=rubygem-rcodetools.spec

.PHONY: all srpm download

all: download
	rpmbuild -ba ${SPEC}

srpm: download
	rpmbuild -bs ${SPEC}

download:
	spectool -R -g ${SPEC}
