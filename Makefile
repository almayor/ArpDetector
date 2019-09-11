.PHONY: install uninstall

install: | bindir
	@chmod +x arpdetector.py
	@ln -f arpdetector.py ${HOME}/bin/arpdetector
	@sed -i '' 's%HOMEDIR%${HOME}%g' arpdetector.user.plist
	@ln -f arpdetector.user.plist $(HOME)/Library/LaunchAgents/
	@launchctl load ${HOME}/Library/LaunchAgents/arpdetector.user.plist
	@launchctl start arpdetector.user
	@echo "successfully installed"

bindir:
	@if [ ! -d ${HOME}/bin ]; then \
		mkdir ${HOME}/bin; \
		echo "created directory ${HOME}/bin"; \
	fi

uninstall:
	@rm -f ${HOME}/bin/arpdetector
	@if [ -n "$(ls ${HOME}/bin)" ]; then \
		rmdir ${HOME}/bin 2>/dev/null; \
	fi
	@if [ -e ${HOME}/Library/LaunchAgents/arpdetector.user.plist ]; then \
		launchctl unload ${HOME}/Library/LaunchAgents/arpdetector.user.plist; \
	fi
	@rm -f ${HOME}/Library/LaunchAgents/arpdetector.user.plist
	@echo "successfully uninstalled"
